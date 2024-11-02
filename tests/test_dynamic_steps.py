import allure
from allure_commons.types import Severity
from selene import browser, be, have


def test_dynamic_steps(firefox_headless_mode):
    allure.dynamic.tag("web")
    allure.label("owner", "aa.eliseev")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.feature("Задача Issues")
    allure.dynamic.story("Проверка наличия задачи в Issues")
    allure.link("https://github.com", name="github")

    with allure.step("Открываем профиль пользователя на Github"):
        browser.open('/lexaeliseev')

    with allure.step("Переходим на вкладку Репозитории"):
        browser.element('[data-tab-item="repositories"]').click()
    browser.element('//h3[@class="wb-break-all"]/a[contains(text(), "HomeWork7")]').should(
        have.text("HomeWork7")).click()

    with allure.step("Переходим во вкладку Issues"):
        browser.element('[data-content="Issues"]').double_click()

    with allure.step("Проверяем наличие Issues с названием 'Create Issues'"):
        browser.element('//a[@id="issue_3_link" and contains(text(), "Create Issues")]').should(be.visible).should(
            have.text('Create Issues'))