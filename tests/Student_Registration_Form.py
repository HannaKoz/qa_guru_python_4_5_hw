import pytest
from selene import browser, have, be
from selene.support.shared import browser

def test_form(browser_size_w1920_h1080):
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').type('Иван')
    browser.element('#lastName').type('Иванов')
    browser.element('#userEmail').type('qa_test@test.ru')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('3334445555')

    # Choose Birthdate
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('option[value="7"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('option[value="2001"]').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--029"]').click()

    browser.element('#subjectsInput').type('Comm').element('//div[contains(text(),"Commerce")]').click()
    browser.element('[for=hobbies-checkbox-3]').click()
    browser.element('#uploadPicture').send_keys('C:/Users/Hanna/Downloads/Без названия.jpg')

    browser.element('#currentAddress').type("Планета Земля")
    browser.element('#react-select-3-input').type('ra')
    browser.element('#react-select-3-option-1').click()
    browser.element('#react-select-4-input').type(' ')
    browser.element('#react-select-4-option-1').click()

    browser.element('[id="submit"]').submit()

    # Inputs control
    browser.element('#example-modal-sizes-title-lg').should(have.text("Thanks"))
    browser.element('//tbody/tr[1]/td[2]').should(have.text("Иван Иванов"))
    browser.element('//tbody/tr[2]/td[2]').should(have.text("qa_test@test.ru"))
    browser.element('//tbody/tr[3]/td[2]').should(have.text("Male"))
    browser.element('//tbody/tr[4]/td[2]').should(have.text("3334445555"))
    browser.element('//tbody/tr[5]/td[2]').should(have.text("29 August,2001"))
    browser.element('//tbody/tr[6]/td[2]').should(have.text("Commerce"))
    browser.element('//tbody/tr[7]/td[2]').should(have.text("Music"))
    browser.element('//tbody/tr[9]/td[2]').should(have.text("Планета Земля"))

    browser.element('[id="closeLargeModal"]').click()
    # Empty fields check
    assert browser.element('#firstName').should(be.blank)
    assert browser.element('#lastName').should(be.blank)
    assert browser.element('#userEmail').should(be.blank)
    assert browser.element('#userNumber').should(be.blank)
    print('Good job, dude! :D')
