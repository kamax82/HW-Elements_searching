from selenium.webdriver.common.by import By
from locators import MainPage
from locators import ProductItem
from locators import Catalog
from locators import AdminLogin
from locators import SearchResult


def test_main(browser):
    browser.get('https://demo.opencart.com/')
    browser.find_element(By.CSS_SELECTOR, MainPage.CURRENCY_CHOSE_EUR)
    browser.find_element(By.CSS_SELECTOR, MainPage.SEARCH_BUTTON)
    browser.find_element(By.CSS_SELECTOR, MainPage.DESKTOP_ITEM)
    browser.find_element(By.CSS_SELECTOR, MainPage.CART_BUTTON)
    browser.find_element(By.CSS_SELECTOR, MainPage.PRODUCT_THUMB_1)
    browser.find_element(By.CSS_SELECTOR, MainPage.BOTTOM_SWIPER)
    browser.find_element(By.CSS_SELECTOR, MainPage.FOOTER)


def test_product_item(browser):
    browser.get('https://demo.opencart.com/index.php?route=product/product&path=57&product_id=49')
    browser.find_element(By.CSS_SELECTOR, MainPage.CURRENCY_CHOSE_EUR)
    browser.find_element(By.CSS_SELECTOR, MainPage.SEARCH_BUTTON)
    browser.find_element(By.CSS_SELECTOR, MainPage.DESKTOP_ITEM)
    browser.find_element(By.CSS_SELECTOR, MainPage.CART_BUTTON)
    browser.find_element(By.CSS_SELECTOR, MainPage.FOOTER)
    browser.find_element(By.CSS_SELECTOR, ProductItem.COMPARE_BUTTON)
    browser.find_element(By.CSS_SELECTOR, ProductItem.DISCRIPTION)
    browser.find_element(By.CSS_SELECTOR, ProductItem.PRICE)
    browser.find_element(By.CSS_SELECTOR, ProductItem.QUANTITY_INPUT)
    browser.find_element(By.CSS_SELECTOR, ProductItem.THUMBNAILS_MAIN)
    browser.find_element(By.CSS_SELECTOR, ProductItem.TO_CART_BUTTON)


def test_catalog(browser):
    browser.get('https://demo.opencart.com/index.php?route=product/category&path=20')
    browser.find_element(By.CSS_SELECTOR, MainPage.CURRENCY_CHOSE_EUR)
    browser.find_element(By.CSS_SELECTOR, MainPage.SEARCH_BUTTON)
    browser.find_element(By.CSS_SELECTOR, MainPage.DESKTOP_ITEM)
    browser.find_element(By.CSS_SELECTOR, MainPage.CART_BUTTON)
    browser.find_element(By.CSS_SELECTOR, MainPage.PRODUCT_THUMB_1)
    browser.find_element(By.CSS_SELECTOR, MainPage.FOOTER)
    browser.find_element(By.CSS_SELECTOR, Catalog.CATEGORIES)
    browser.find_element(By.CSS_SELECTOR, Catalog.COMPARE)
    browser.find_element(By.CSS_SELECTOR, Catalog.ITEMS_PER_PAGE)
    browser.find_element(By.CSS_SELECTOR, Catalog.ITEMS_THUMBNAILS)
    browser.find_element(By.CSS_SELECTOR, Catalog.REPRESENT_MODE)
    browser.find_element(By.CSS_SELECTOR, Catalog.SORT_BY_INPUT)


def test_admin_login(browser):
    browser.get('https://demo.opencart.com/admin/')
    browser.find_element(By.CSS_SELECTOR, AdminLogin.FOOTER)
    browser.find_element(By.CSS_SELECTOR, AdminLogin.FORGOTTEN_PASSWORD)
    browser.find_element(By.CSS_SELECTOR, AdminLogin.INPUT_PASSWORD)
    browser.find_element(By.CSS_SELECTOR, AdminLogin.INPUT_USERNAME)
    browser.find_element(By.CSS_SELECTOR, AdminLogin.LOGIN_BUTTON)
    browser.find_element(By.CSS_SELECTOR, AdminLogin.LOGO)


def test_search_result(browser):
    browser.get('https://demo.opencart.com/index.php?route=product/search&search=pod')
    browser.find_element(By.CSS_SELECTOR, MainPage.CURRENCY_CHOSE_EUR)
    browser.find_element(By.CSS_SELECTOR, MainPage.SEARCH_BUTTON)
    browser.find_element(By.CSS_SELECTOR, MainPage.DESKTOP_ITEM)
    browser.find_element(By.CSS_SELECTOR, MainPage.CART_BUTTON)
    browser.find_element(By.CSS_SELECTOR, MainPage.FOOTER)
    browser.find_element(By.CSS_SELECTOR, Catalog.COMPARE)
    browser.find_element(By.CSS_SELECTOR, Catalog.ITEMS_PER_PAGE)
    browser.find_element(By.CSS_SELECTOR, Catalog.ITEMS_THUMBNAILS)
    browser.find_element(By.CSS_SELECTOR, Catalog.SORT_BY_INPUT)
    browser.find_element(By.CSS_SELECTOR, SearchResult.CATEGORIES_SELECTOR)
    browser.find_element(By.CSS_SELECTOR, SearchResult.SEARCH_CRITERIA)
    browser.find_element(By.CSS_SELECTOR, SearchResult.SEARCH_MODIFICATOR)
    browser.find_element(By.CSS_SELECTOR, SearchResult.TO_CART_1)
    browser.find_element(By.CSS_SELECTOR, SearchResult.TO_COMPARE_BUTTON_1)
    browser.find_element(By.CSS_SELECTOR, SearchResult.TO_WISH_LIST_1)
