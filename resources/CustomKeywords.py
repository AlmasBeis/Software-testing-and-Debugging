from SeleniumLibrary import SeleniumLibrary
from selenium.common.exceptions import UnexpectedAlertPresentException, NoAlertPresentException
import time
import random

class CustomKeywords:

    def __init__(self):
        self.selib = SeleniumLibrary()

    def open_site(self, url):
        """Открывает сайт"""
        print(f"=== Открываю сайт: {url} ===")
        self.selib.open_browser(url, "chrome")
        self.selib.maximize_browser_window()
        print("=== Браузер открыт ===")

    def sign_up_to_demoblaze(self, username_prefix="user", password="123456"):
        """Регистрирует нового пользователя"""
        unique_username = f"{username_prefix}_{random.randint(1000, 9999)}"
        self.selib.click_element("id=signin2")
        time.sleep(1)
        self.selib.input_text("id=sign-username", unique_username)
        self.selib.input_text("id=sign-password", password)
        self.selib.click_button("xpath=//button[text()='Sign up']")
        time.sleep(1)

        try:
            alert = self.selib.driver.switch_to.alert
            print(f"⚠️ Alert: {alert.text}")
            alert.accept()
        except NoAlertPresentException:
            print("✅ Пользователь успешно зарегистрирован (alert не появился)")

        return unique_username, password

    def login_to_demoblaze(self, username, password):
        """Авторизация на сайте demoblaze"""
        self.selib.click_element("id=login2")
        time.sleep(1)
        self.selib.input_text("id=loginusername", username)
        self.selib.input_text("id=loginpassword", password)
        self.selib.click_button("xpath=//button[text()='Log in']")
        self.selib.wait_until_page_contains("Welcome", timeout=10)

    def verify_login_successful(self, username):
        """Проверяет успешный вход"""
        self.selib.page_should_contain(f"Welcome {username}")
        print(f"⚠️ Alert: {username}")

    def logout_from_demoblaze(self):
        """Выход из аккаунта"""
        time.sleep(1)
        self.selib.click_element("id=logout2")
        self.selib.wait_until_page_contains("Log in", timeout=10)
        print("✅ Пользователь успешно вышел из аккаунта")

    def buy_product_from_demoblaze(self, product_name="Samsung galaxy s6"):
        """Добавляет товар в корзину и оформляет заказ"""

        self.selib.click_link(product_name)
        time.sleep(2)

        self.selib.click_element("xpath=//a[contains(text(), 'Add to cart')]")
        time.sleep(2)

        try:
            alert = self.selib.driver.switch_to.alert
            print(f"🛒 Alert: {alert.text}")
            alert.accept()
        except NoAlertPresentException:
            print("⚠️ Нет alert'а при добавлении товара")

        self.selib.click_link("Cart")
        time.sleep(2)

        self.selib.click_button("xpath=//button[text()='Place Order']")
        time.sleep(1)

        self.selib.input_text("id=name", "QA Tester")
        self.selib.input_text("id=country", "Kazakhstan")
        self.selib.input_text("id=city", "Almaty")
        self.selib.input_text("id=card", "1234 5678 9876 5432")
        self.selib.input_text("id=month", "10")
        self.selib.input_text("id=year", "2025")

        self.selib.click_button("xpath=//button[text()='Purchase']")
        time.sleep(2)

        self.selib.page_should_contain("Thank you for your purchase!")
        self.selib.click_button("xpath=//button[text()='OK']")

        print("✅ Покупка успешно завершена!")

    def close_browser(self):
        """Закрывает браузер"""
        self.selib.close_browser()
