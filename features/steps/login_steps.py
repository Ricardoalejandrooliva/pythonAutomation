from behave import given, then, when
from features.page_objects.BasePage import wait_until_element_displayed, wait_until_text_is_present
from features.page_objects.login_page import LOGIN_LINK
from utils.Driver import launch_browser
from page_objects.login_page import USERNAME_FIELD, PASSWORD_FIELD, LOGIN_BTN, USERNAME, PASSWORD
from page_objects.BasePage import send_keys_by_css_selector, click_element_by_css_selector, get_element_text


@given('el usuario este en la pagina https://www.demoblaze.com/')
def navigate_to_saucelabs(context):
    launch_browser(context, 'Chrome')
    context.driver.maximize_window()
    context.driver.get('https://www.demoblaze.com/')


@when('el usuario inicia sesión con credenciales válidas')
def login_with_valid_credentials(context):
    click_element_by_css_selector(context, LOGIN_LINK)
    send_keys_by_css_selector(context, USERNAME_FIELD, USERNAME)
    send_keys_by_css_selector(context, PASSWORD_FIELD, PASSWORD)
    click_element_by_css_selector(context, LOGIN_BTN)
    

@then('el nombre del usuario aparece en la página')
def user_name(context):
    wait_until_text_is_present(context, "#nameofuser", "Welcome oliri")
    welcomeUserName = get_element_text(context, "#nameofuser")
    assert welcomeUserName == "Welcome oliri"
