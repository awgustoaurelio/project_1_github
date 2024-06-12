from playwright.sync_api import expect


def test_moon(page):
    page.context.set_default_navigation_timeout(30e3)
    page.context.set_default_timeout(30e3)  
    page.set_viewport_size({"width": 1920, "height": 1080})

    page.goto("https://ru.wikipedia.org/")
    page.locator(".vector-search-box-input").fill("Луна")
    page.locator("#searchButton").click()
    page.locator(".infobox-image > .no-wikidata > span > .mw-file-description").click()

    expect(page).to_have_url("https://ru.wikipedia.org/wiki/%D0%9B%D1%83%D0%BD%D0%B0#/media/%D0%A4%D0%B0%D0%B9%D0%BB:FullMoon2010.jpg", timeout=30000)