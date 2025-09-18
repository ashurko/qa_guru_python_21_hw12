import allure

from pages.registration_page import RegistrationPage

@allure.title('Успешное заполнение формы')
def test_fill_form():
    registration_page = RegistrationPage()
    registration_page.open()
    (
        registration_page
        .fill_first_name('Anton')
        .fill_last_name('Shurko')
        .fill_email('antonshurko@gmail.com')
        .pick_gender("Male")
        .fill_phone_number('9159379992')
        .fill_birthday('November', '1995', '22')
        .fill_subjects('English')
        .pick_hobby('Sports')
        .upload_picture('test_file.txt')
        .fill_address('Some address')
        .choose_location('NCR', 'Delhi')
        .submit_button()
    )

    registration_page.should_have_registered_user_with(
        'Anton Shurko',
        'antonshurko@gmail.com',
        'Male',
        '9159379992',
        '22 November,1995',
        'English',
        'Sports',
        'test_file.txt',
        'Some address',
        'NCR Delhi'
    )