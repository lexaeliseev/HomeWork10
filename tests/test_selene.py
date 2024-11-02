import allure
from allure_commons.types import Severity
from selene import browser, be, have


@allure.tag("web")
@allure.label("owner", "aa.eliseev")
@allure.severity(Severity.CRITICAL)
@allure.feature("Задача Issues")
@allure.story("Проверка наличия задачи в Issues")
@allure.link("https://github.com", name="github")

def test_selene(firefox_headless_mode):
    browser.open('/lexaeliseev')

    browser.element('[data-tab-item="repositories"]').double_click()

    browser.element('//h3[@class="wb-break-all"]/a[contains(text(), "HomeWork7")]').should(
        have.text("HomeWork7")).click()

    browser.element('[data-content="Issues"]').click().element(
        '//a[@id="issue_3_link" and contains(text(), "Create Issues")]').should(be.visible).should(
        have.text('Create Issues'))
