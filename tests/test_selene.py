from selene import browser, be, have


def test_selene():
    browser.open('/lexaeliseev')

    browser.element('[data-tab-item="repositories"]').click()

    browser.element('//h3[@class="wb-break-all"]/a[contains(text(), "HomeWork7")]').should(
        have.text("HomeWork7")).click()

    browser.element('[data-content="Issues"]').click().element(
        '//a[@id="issue_3_link" and contains(text(), "Create Issues")]').should(be.visible).should(
        have.text('Create Issues'))
