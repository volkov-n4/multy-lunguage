from selenium.webdriver.common.by import By


def test_add_button_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    cart_button = len(browser.find_elements(By.CSS_SELECTOR, '.btn-add-to-basket'))
    assert cart_button == 1, 'The element not found on the page or elements more then 1'
