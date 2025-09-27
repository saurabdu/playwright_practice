from playwright.sync_api import sync_playwright


def test_coderbyte():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://amazon.in")
        page.get_by_placeholder( "Search Amazon.in").fill("Iphone 17")

