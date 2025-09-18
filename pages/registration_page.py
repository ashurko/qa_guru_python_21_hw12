import os

import allure
from selene import browser, have, be, by


class RegistrationPage:
    @allure.step ('Открываем страницу')
    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')
        browser.execute_script('window.scrollBy(0, 500)')
        return self


    @allure.step ('Заполняем имя')
    def fill_first_name(self, value):
        browser.element('[id="firstName"]').type(value)
        return self


    @allure.step ('Заполняем фамилию')
    def fill_last_name(self, value):
        browser.element('[id="lastName"]').type(value)
        return self


    @allure.step ('Заполняем почту')
    def fill_email(self, value):
        browser.element('[id="userEmail"]').type(value)
        return self


    @allure.step ('Выбираем пол')
    def pick_gender(self, value):
        browser.element('#genterWrapper').element(by.text(value)).click()
        return self

    @allure.step('Заполняем номер телефона')
    def fill_phone_number(self, value):
        browser.element('[id="userNumber"]').type(value)
        return self

    @allure.step('Выбираем дату рождения')
    def fill_birthday (self, month, year, day):
        browser.element('#dateOfBirthInput').click()
        browser.all('.react-datepicker__month-select option').element_by(have.exact_text(month)).click()
        browser.all('.react-datepicker__year-select option').element_by(have.exact_text(year)).click()
        browser.element(f'.react-datepicker__day--0{day}').click()
        return self

    @allure.step('Выбираем предмет')
    def fill_subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()
        return self

    @allure.step('Выбираем хобби')
    def pick_hobby(self, value):
        browser.element('#hobbiesWrapper').element(by.text(value)).click()
        return self

    @allure.step('Загружаем файл')
    def upload_picture(self, value):
        file_path = os.path.join(os.path.dirname(__file__), 'test_file.txt')
        browser.element('#uploadPicture').send_keys(file_path)
        return self

    @allure.step('Заполняем адрес')
    def fill_address(self, value):
        browser.element('#currentAddress').type('Some address')
        return self

    @allure.step('Выбираем локацию')
    def choose_location(self, state, city):
        browser.element('#state input').type(state).press_enter()
        browser.element('#city input').type(city).press_enter()
        return self

    @allure.step('Отправляем форму')
    def submit_button(self):
        browser.element('#submit').click()
        return self

    @allure.step('Проверяем правильность')
    def should_have_registered_user_with(self,
                                         full_name,
                                         email,
                                         gender,
                                         phone_number,
                                         birthday,
                                         subjects,
                                         hobby,
                                         picture_name,
                                         address,
                                         location):
        (browser.all('tbody tr td:nth-child(2)')
        .should(have.exact_texts(
            full_name,
            email,
            gender,
            phone_number,
            birthday,
            subjects,
            hobby,
            picture_name,
            address,
            location
        )))
        return self