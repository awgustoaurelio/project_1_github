from playwright.sync_api import expect
from time import sleep


def test_ac_ac_iron_man(page):
    page.context.set_default_navigation_timeout(30e3)
    page.context.set_default_timeout(30e3)  
    page.set_viewport_size({"width": 1920, "height": 1080})

    page.goto("https://www.youtube.com")
    page.get_by_placeholder("Search").fill("ac ac iron man")
    sleep(5)
    page.get_by_placeholder("Search").click()
    page.get_by_placeholder("Search").press("Enter")

    expect(page.get_by_text("AC/DC- Shoot to thrill Iron Man").first).to_be_visible(timeout=30e3)