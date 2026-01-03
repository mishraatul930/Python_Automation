from playwright.sync_api import sync_playwright

def test_get(playwright: sync_playwright):
    context = playwright.request.new_context()
    response = context.get("https://gorest.co.in/public/v2/users/7725350", headers={
        "Authorization":"Bearer f85dd0dcd9289f79bb0830d72fb94e33aa4d8d32d14814d9db456e064f574e35"
    })
    print(response)
    assert response.status == 200, "Response is not 200"
    assert response.status_text == "OK", "Response text is not OK"
    print(response.json()["name"])
    assert response.json()["email"] == "rana_nikita@howe-gulgowski.test","Not the right email"

    # OR

    res = response.json()
    print(res.get("email"))
    print(response.headers)
    assert response.headers["content-type"] == "application/json; charset=utf-8"
