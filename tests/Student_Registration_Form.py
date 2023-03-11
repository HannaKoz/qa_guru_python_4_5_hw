from selene import browser, have, be
from selene.support.shared import browser


def test_form(browser_size_w1920_h1080):
    first_name = 'Иван'
    second_name = 'Иванов'
    userEmail = 'qa_test@test.ru'
    userNumber = '3334445555'
    address = "Планета Земля"

    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').type(first_name)
    browser.element('#lastName').type(second_name)
    browser.element('#userEmail').type(userEmail)
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type(userNumber)

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

    # Enter address
    browser.element('#currentAddress').type(address)
    browser.element('#react-select-3-input').type('ra')
    browser.element('#react-select-3-option-1').click()
    browser.element('#react-select-4-input').type(' ')
    browser.element('#react-select-4-option-1').click()

    browser.element('[id="submit"]').submit()

    # Inputs control
    browser.element('#example-modal-sizes-title-lg').should(have.text("Thanks"))
    browser.all('//tbody/tr')[0].should(have.text(first_name + " " + second_name))
    browser.all('//tbody/tr')[1].should(have.text(userEmail))
    browser.all('//tbody/tr')[2].should(have.text("Male"))
    browser.element('//tbody/tr[4]/td[2]').should(have.text(userNumber))
    browser.element('//tbody/tr[5]/td[2]').should(have.text("29 August,2001"))
    browser.element('//tbody/tr[6]/td[2]').should(have.text("Commerce"))
    browser.element('//tbody/tr[7]/td[2]').should(have.text("Music"))
    browser.element('//tbody/tr[9]/td[2]').should(have.text(address))
    browser.element('//tbody/tr[10]/td[2]').should(have.text("Uttar Pradesh Lucknow"))

    browser.element('[id="closeLargeModal"]').click()

    # Empty fields control
    browser.element('#firstName').should(be.blank)
    browser.element('#lastName').should(be.blank)
    browser.element('#userEmail').should(be.blank)
    browser.element('#userNumber').should(be.blank)


