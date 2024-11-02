import allure
from allure_commons.types import Severity
from selene import browser, be, have


def test_dynamic_steps():
    with allure.step("Открываем профиль пользователя на Github"):
        browser.open('/lexaeliseev')

    with allure.step("Переходим на вкладку Репозитории"):
        browser.element('[data-tab-item="repositories"]').click()
    browser.element('//h3[@class="wb-break-all"]/a[contains(text(), "HomeWork7")]').should(
        have.text("HomeWork7")).click()

    with allure.step("Переходим во вкладку Issues"):
        browser.element('[data-content="Issues"]').click()

    with allure.step("Проверяем наличие Issues с названием 'Create Issues'"):
        browser.element('//a[@id="issue_3_link" and contains(text(), "Create Issues")]').should(be.visible).should(
            have.text('Create Issues'))


def test_decorators_steps():
    open_page('/lexaeliseev')
    click_repo("HomeWork7")
    click_issues()
    check_value("Create Issues", 'Create Issues')


@allure.step("Открываем профиль {endpoint} на Github")
def open_page(endpoint):
    browser.open(endpoint)


@allure.tag("web")
@allure.label("owner", "aa.eliseev")
@allure.severity(Severity.CRITICAL)
@allure.feature("Задача Issues")
@allure.story("Проверка наличия задачи в Issues")
@allure.link("https://github.com", name="github")
@allure.step("Переходим на вкладку {name}")
def click_repo(name):
    browser.element('[data-tab-item="repositories"]').click()
    browser.element(f'//h3[@class="wb-break-all"]/a[contains(text(), "{name}")]').should(
        have.text(f"{name}")).click()


@allure.step("Переходим в таб Issues")
def click_issues():
    browser.element('[data-content="Issues"]').click()


@allure.step("Проверяем наличие Issues")
def check_value(issue_name, value):
    browser.element(f'//a[@id="issue_3_link" and contains(text(), "{issue_name}")]').should(be.visible).should(
        have.text(f"{value}"))