import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def add_chrome_options(user_language: str):
    ''':Метод для расширения опций chrome'''
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    return options

def add_firefox_profile(user_language):
    ''':Метод для расширения опций firefox'''
    fp = webdriver.FirefoxProfile()
    fp.set_preference("intl.accept_languages", user_language)
    return fp

def pytest_addoption(parser):
    parser.addoption(
        '--browser_name',
        action='store',
        default='chrome',
        help="Choose browser: chrome or firefox")

    parser.addoption(
        '--language',
        action='store',
        default=None,
        help="Choose one language of: es, fr, ru, en"
    )


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=add_chrome_options(language))
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=add_firefox_profile(language))
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()