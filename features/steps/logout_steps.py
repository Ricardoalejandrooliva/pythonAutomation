from behave import given, when, then
from features.page_objects.BasePage import click_element_by_css_selector, element_displayed, get_text_alert, send_keys_by_css_selector, get_text_alert, wait_until_element_displayed
from features.page_objects.header_page import LOGIN_LINK, USERNAME_FIELD, USERNAME_STRING, PASSWORD_FIELD, PASSWORD_STRING, LOGIN_BTN, LOGOUT_BTN 

@given('el usuario esta logeado')
def login_with_valid_credentials(context):
    click_element_by_css_selector(context, LOGIN_LINK)
    send_keys_by_css_selector(context, USERNAME_FIELD, USERNAME_STRING)
    send_keys_by_css_selector(context, PASSWORD_FIELD, PASSWORD_STRING)
    click_element_by_css_selector(context, LOGIN_BTN)
    

@when('el usuario se deslogea de la pagina')
def logout_click_button(context):
    wait_until_element_displayed(context, LOGOUT_BTN)
    click_element_by_css_selector(context, LOGOUT_BTN)


@then("la pagina muestra el link log in")
def validate_logout(context):
    wait_until_element_displayed(context, LOGIN_LINK)
    login_button_displayed = element_displayed(context, LOGIN_LINK)
    assert login_button_displayed  == True
