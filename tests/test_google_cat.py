from playwright.sync_api import expect


def test_google_cat(page):
    page.context.set_default_navigation_timeout(30e3)
    page.context.set_default_timeout(30e3)  
    page.set_viewport_size({"width": 1920, "height": 1080})

    page.goto("https://www.google.com")
    page.locator("#APjFqb").fill("Big good cat")
    page.locator("input.gNO89b").first.click()
    page.get_by_text("Картинки").first.click()
  
    expect(page.get_by_text("Картинки").first).to_have_attribute("selected", "")