import allure
from allure_commons.types import Severity
from selene import browser, be, have


@allure.tag("web")
@allure.label("owner", "a.eliseev")
@allure.severity(Severity.CRITICAL)
@allure.feature("Задача Issues")
@allure.story("Проверка наличия задачи в Issues")
@allure.link("https://github.com", name="github")
def test_decorators_steps():
    open_page('/lexaeliseev')
    click_repo("HomeWork7")
    click_issues()
    check_value("Create Issues", 'Create Issues')


@allure.step("Открываем профиль {endpoint} на Github")
def open_page(endpoint):
    browser.open(endpoint)


@allure.step("Переходим в репозиторий {name}")
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
