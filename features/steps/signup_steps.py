from behave import when, then
from features.page_objects.BasePage import click_element_by_css_selector, get_text_alert, send_keys_by_css_selector, get_text_alert
from features.page_objects.header_page import PASSWORD_STRING, SIGNUP_BUTTON, SIGNUP_LINK, SIGNUP_PASSWORD_FIELD, SIGNUP_USER_FIELD
import time
from utils.UUID import crearuuid
UUID = crearuuid()


@when('el usuario se registra con credenciales no registradas en el sistema')
def login_with_valid_credentials(context):
    click_element_by_css_selector(context, SIGNUP_LINK)
    send_keys_by_css_selector(context, SIGNUP_USER_FIELD, UUID)
    send_keys_by_css_selector(context, SIGNUP_PASSWORD_FIELD, PASSWORD_STRING)
    click_element_by_css_selector(context, SIGNUP_BUTTON)


@then('la pagina muesta el pop up de Sign up successful')
def text_sign_up_successful(context):
    alerttext = get_text_alert(context)
    assert alerttext == 'Sign up successful.'
