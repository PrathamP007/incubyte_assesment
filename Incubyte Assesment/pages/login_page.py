import time
from locators.login_locators import LoginLocators
from utils.config import BASE_URL
from utils.base_page import BasePage
from utils.data_loader import load_json

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.data = load_json("login_data.json")["valid_user"]

    def open_login_page(self):
        self.page.goto(BASE_URL)

    def open_registration_page(self):
        self.click(LoginLocators.REGISTER_BUTTON)

    def fill_registration_form(self):
        d = self.data
        self.fill(LoginLocators.first_name, d["first_name"])
        self.fill(LoginLocators.last_name, d["last_name"])
        self.fill(LoginLocators.address, d["address"])
        self.fill(LoginLocators.city, d["city"])
        self.fill(LoginLocators.state, d["state"])
        self.fill(LoginLocators.zip_code, d["zip_code"])
        self.fill(LoginLocators.phone, d["phone"])
        self.fill(LoginLocators.ssn, d["ssn"])
        self.fill(LoginLocators.username, d["username"])
        self.fill(LoginLocators.password, d["password"])
        self.fill(LoginLocators.confirm_password, d["confirm_password"])

    def click_register_submit(self):
        self.click(LoginLocators.register)

    def click_account_overview(self):
        self.click(LoginLocators.accounts_overview)
 
    def get_account_balance(self):
        balance_value_in_string =self.get_text(LoginLocators.account_balance_value)
        print(balance_value_in_string)
        
    def verify_dashboard(self):
        assert "profile" in self.page.url, "User not redirected to profile builder page!"
