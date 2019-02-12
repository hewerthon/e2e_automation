from Library import ConfigReader


class RegistrationClass:

    def __init__(self, obj):
        global driver
        driver = obj

    def enter_username(self, username):
        driver.find_element_by_name(ConfigReader.fetch_element_locators('Registration', 'username_name')).send_keys(
            'Hello')

    def enter_password(self, password):
        driver.find_element_by_name(ConfigReader.fetch_element_locators('Registration', 'password_name')).send_keys('Hello')

    def enter_email(self, email):
        driver.find_element_by_name(ConfigReader.fetch_element_locators('Registration', 'email_name')).send_keys('abcd')



