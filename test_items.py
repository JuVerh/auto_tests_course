import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_is_add_to_basket_present(browser):
    browser.get(link)
    x = browser.find_elements(By.CSS_SELECTOR,".btn-add-to-basket")
    assert x is not None, 'Add to basket button is not displayed'

