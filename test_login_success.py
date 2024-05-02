#from Config.config import BASE_URL
from playwright.sync_api import Playwright, sync_playwright, expect
import time


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(ignore_https_errors=True)
    page = context.new_page()
    page.set_extra_http_headers({
                                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"})

    page.goto("https://dev1-manager.threecolts.com/")

    page.get_by_label("false").click()
    page.get_by_placeholder("Name").click()
    page.get_by_label("false").click()
    page.get_by_placeholder("Name").fill("pbetala@threecolts.com")
    page.get_by_placeholder("Name").press("Tab")
    page.get_by_label("false").click()
    page.get_by_placeholder("**********").click()
    page.get_by_label("false").click()
    page.get_by_placeholder("**********").fill("Test12345678")
    page.get_by_label("false").click()
    time.sleep(5)
    expect(page.get_by_text("Threecolts Manager")).to_be_visible()
    expect(page.get_by_text("pbetala@threecolts.com")).to_be_visible()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_run(playwright)
