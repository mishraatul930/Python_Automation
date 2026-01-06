from playwright.sync_api import sync_playwright
from pytest_base_url.plugin import base_url


def test_response(playwright:sync_playwright):
    context = playwright.request.new_context(base_url="https://gorest.co.in")
    response = context.get(url = "/public/v2/users", params = {"page": "1"}, headers = {
        "Authorization":"Bearer f85dd0dcd9289f79bb0830d72fb94e33aa4d8d32d14814d9db456e064f574e35"
    })

    print(response)
    assert response.status == 200, "Response is not 200"
    assert response.status_text == "OK", "Response text is not OK"
    res = response.json()
    print(res[0])
    size = len(res)
    assert size == 10, "Number of users is not 10"
    print(res[0]["name"])
    for i in range(0, size):
        if res[i]["name"] == "Gov. Abhaya Kapoor":
            print(res[i]["email"])
        break