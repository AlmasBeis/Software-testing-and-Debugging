from SeleniumLibrary import SeleniumLibrary
from selenium.common.exceptions import UnexpectedAlertPresentException, NoAlertPresentException
import time
import random
from variables import NAME, COUNTRY, CITY, MONTH, YEAR, CREDIT_CARD
from locators import (
    SIGNUP_BUTTON, SIGNUP_USERNAME_INPUT, SIGNUP_PASSWORD_INPUT, SIGNUP_SUBMIT_BUTTON,
    LOGIN_BUTTON, LOGIN_USERNAME_INPUT, LOGIN_PASSWORD_INPUT, LOGIN_SUBMIT_BUTTON,
    LOGOUT_BUTTON, CART_LINK, HOME_LINK, ADD_TO_CART_BUTTON,
    PLACE_ORDER_BUTTON, ORDER_NAME_INPUT, ORDER_COUNTRY_INPUT, ORDER_CITY_INPUT,
    ORDER_CARD_INPUT, ORDER_MONTH_INPUT, ORDER_YEAR_INPUT, PURCHASE_BUTTON, PURCHASE_OK_BUTTON
)

class CustomKeywords:

    def __init__(self):
        self.selib = SeleniumLibrary()

    def open_site(self, url, browser):
        """Открывает сайт"""
        print(f"=== Открываю сайт: {url} ===")
        self.selib.open_browser(url, browser)
        self.selib.maximize_browser_window()
        print("=== Браузер открыт ===")

    def sign_up_to_demoblaze(self, username_prefix="user", password="123456"):
        """Регистрирует нового пользователя"""
        unique_username = f"{username_prefix}_{random.randint(1000, 9999)}"
        self.selib.click_element(SIGNUP_BUTTON)
        time.sleep(1)
        self.selib.input_text(SIGNUP_USERNAME_INPUT, unique_username)
        self.selib.input_text(SIGNUP_PASSWORD_INPUT, password)
        self.selib.click_button(SIGNUP_SUBMIT_BUTTON)
        time.sleep(4)

        try:
            alert = self.selib.driver.switch_to.alert
            print(f"⚠️ Alert: {alert.text}")
            alert.accept()
        except NoAlertPresentException:
            print("✅ Пользователь успешно зарегистрирован (alert не появился)")

        return unique_username, password

    def login_to_demoblaze(self, username, password):
        """Авторизация на сайте demoblaze"""
        self.selib.click_element(LOGIN_BUTTON)
        time.sleep(1)
        self.selib.input_text(LOGIN_USERNAME_INPUT, username)
        self.selib.input_text(LOGIN_PASSWORD_INPUT, password)
        self.selib.click_button(LOGIN_SUBMIT_BUTTON)
        self.selib.wait_until_page_contains("Welcome", timeout=20)

    def verify_login_successful(self, username):
        """Проверяет успешный вход"""
        self.selib.page_should_contain(f"Welcome {username}")
        print(f"⚠️ Alert: {username}")

    def logout_from_demoblaze(self):
        """Выход из аккаунта"""
        time.sleep(1)
        self.selib.click_element(LOGOUT_BUTTON)
        self.selib.wait_until_page_contains("Log in", timeout=10)
        print("✅ Пользователь успешно вышел из аккаунта")

    def add_to_cart(self, product_name="Iphone 6 32gb"):
        """Добавляет товар в корзину"""

        self.selib.click_link(product_name)
        time.sleep(2)

        self.selib.click_element(ADD_TO_CART_BUTTON)
        time.sleep(2)
        try:
            alert = self.selib.driver.switch_to.alert
            print(f"🛒 Alert: {alert.text}")
            alert.accept()
        except NoAlertPresentException:
            print("⚠️ Нет alert'а при добавлении товара")

        time.sleep(2)
        self.selib.click_link(HOME_LINK)

    def buy_product_from_demoblaze(self):
        """Добавляет оформляет заказ из корзины"""

        self.selib.click_link(CART_LINK)
        time.sleep(2)

        self.selib.click_button(PLACE_ORDER_BUTTON)
        time.sleep(1)

        self.selib.input_text(ORDER_NAME_INPUT, NAME)
        self.selib.input_text(ORDER_COUNTRY_INPUT, COUNTRY)
        self.selib.input_text(ORDER_CITY_INPUT, CITY)
        self.selib.input_text(ORDER_CARD_INPUT, CREDIT_CARD)
        self.selib.input_text(ORDER_MONTH_INPUT, MONTH)
        self.selib.input_text(ORDER_YEAR_INPUT, YEAR)

        self.selib.click_button(PURCHASE_BUTTON)
        time.sleep(2)

        self.selib.page_should_contain("Thank you for your purchase!")
        self.selib.click_button(PURCHASE_OK_BUTTON)

        print("✅ Покупка успешно завершена!")

    def add_and_buy_product_from_demoblaze(self, product_name="Samsung galaxy s6"):
        """Добавляет товар в корзину и оформляет заказ"""

        self.selib.click_link(product_name)
        time.sleep(2)

        self.selib.click_element(ADD_TO_CART_BUTTON)
        time.sleep(2)

        try:
            alert = self.selib.driver.switch_to.alert
            print(f"🛒 Alert: {alert.text}")
            alert.accept()
        except NoAlertPresentException:
            print("⚠️ Нет alert'а при добавлении товара")

        self.selib.click_link(CART_LINK)
        time.sleep(2)

        self.selib.click_button(PLACE_ORDER_BUTTON)
        time.sleep(1)

        self.selib.input_text(ORDER_NAME_INPUT, "QA Tester")
        self.selib.input_text(ORDER_COUNTRY_INPUT, "Kazakhstan")
        self.selib.input_text(ORDER_CITY_INPUT, "Almaty")
        self.selib.input_text(ORDER_CARD_INPUT, "1234 5678 9876 5432")
        self.selib.input_text(ORDER_MONTH_INPUT, "10")
        self.selib.input_text(ORDER_YEAR_INPUT, "2025")

        self.selib.click_button(PURCHASE_BUTTON)
        time.sleep(2)

        self.selib.page_should_contain("Thank you for your purchase!")
        self.selib.click_button(PURCHASE_OK_BUTTON)

        print("✅ Покупка успешно завершена!")

    def close_browser(self):
        """Закрывает браузер"""
        self.selib.close_browser()
