import allure
from selene import browser, be, have
from allure_commons.types import Severity


def test_dynamic_labels():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Задача Issues")
    allure.dynamic.story("Неавторизованный пользователь не может создать задачу в Issues")
    allure.link("https://github.com", name="github")
    allure.label("owner", "aa.eliseev")


@allure.severity(Severity.CRITICAL)
@allure.tag("web")
@allure.label("owner", "aa.eliseev")
@allure.feature("Задача Issues")
@allure.story("Авторизованный пользователь может создать задачу в Issues")
@allure.link("https://github.com", name="github")
def test_decorators_labels():
    pass



# 52:39