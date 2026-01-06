import string
import json
from playwright.sync_api import sync_playwright
import random

def test_post_file(playwright:sync_playwright):
    email = "".join(random.choices(string.ascii_uppercase + string.digits, k=5)) + "@gmail.com"
    # data = {
    #         "name": "Atul Mishra",
    #         "email": "mishraatul"+email,
    #         "gender": "male",
    #         "status": "active"
    # }
    # DATA FROM EXTERNAL JSON FILE
    with open(".\\Playwright_Python\\JSONFile\\CreateUser.json", 'r') as read_file:
        data = json.load(read_file)
        data["email"] = "mishraatul"+email


    context = playwright.request.new_context(base_url="https://gorest.co.in")
    response = context.post(url = "/public/v2/users", params = {"page": "1"}, headers = {
        "Authorization":"Bearer f85dd0dcd9289f79bb0830d72fb94e33aa4d8d32d14814d9db456e064f574e35"
    }, data = data)

    print(response)
    assert response.status == 201, "Response is not 200"
    assert response.status_text == "Created", "Response text is not OK"
    res = response.json()
    print(res)
    assert res["email"] == data["email"], "Email not matching"