import os
import uuid
from typing import Generator

import pytest
from playwright.sync_api import APIRequestContext, Playwright

# -------------------------------------------------------------------
# Environment validation
# -------------------------------------------------------------------

GITHUB_API_TOKEN = os.getenv("GITHUB_API_TOKEN")
GITHUB_USER = os.getenv("GITHUB_USER")

assert GITHUB_API_TOKEN, "GITHUB_API_TOKEN is not set"
assert GITHUB_USER, "GITHUB_USER is not set"

GITHUB_REPO = f"test-repo-{uuid.uuid4().hex[:8]}"


# -------------------------------------------------------------------
# Fixtures
# -------------------------------------------------------------------

@pytest.fixture(scope="session")
def api_request_context(
    playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"Bearer {GITHUB_API_TOKEN}",
    }

    context = playwright.request.new_context(
        base_url="https://api.github.com",
        extra_http_headers=headers,
    )

    yield context
    context.dispose()


@pytest.fixture(scope="session", autouse=True)
def create_test_repository(
    api_request_context: APIRequestContext,
) -> Generator[None, None, None]:
    response = api_request_context.post(
        "/user/repos",
        json={"name": GITHUB_REPO, "private": False},
    )

    if not response.ok:
        pytest.fail(f"Failed to create test repository: {response.text()}")

    yield

    delete_response = api_request_context.delete(
        f"/repos/{GITHUB_USER}/{GITHUB_REPO}"
    )
    assert delete_response.ok, "Failed to delete test repository"


# -------------------------------------------------------------------
# Tests
# -------------------------------------------------------------------

@pytest.mark.parametrize(
    "title, body",
    [
        ("[Bug] report 1", "Bug description"),
        ("[Feature] request 1", "Feature description"),
    ],
)
def test_should_create_issue(
    api_request_context: APIRequestContext,
    title: str,
    body: str,
) -> None:
    response = api_request_context.post(
        f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues",
        json={"title": title,"body": body,},
    )

    assert response.ok, f"Issue creation failed: {response.text()}"

    created_issue = response.json()

    assert created_issue["title"] == title
    assert created_issue["body"] == body
    assert "number" in created_issue
