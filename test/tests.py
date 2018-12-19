import time


class TestPages(object):
    def test_main_page(self, url, email, password, incorrect_email, incorrect_password):
        self.main_page.get_mainpage_url(url)
        assert self.main_page.diprella_header.is_displayed(), "Header isn't displayed"
        assert self.main_page.signin_link.is_displayed(), "Signin url not found"

    def test_login_with_correct_credentials(self, url, email, password, incorrect_email, incorrect_password):
        signin_page = self.main_page.get_mainpage_url(url).click_on_signin_link()
        assert signin_page.diprella_logo.is_displayed(), "Diprella logo isn't shown"
        assert signin_page.signup_link.is_displayed(), "SignUp url isn't shown"
        assert signin_page.facebook_login.is_displayed(), "Facebook signin button isn't shown"
        assert signin_page.google_login.is_displayed(), "Google signin button isn't shown"
        assert signin_page.linkedin_login.is_displayed(), "Linkedin signin button isn't shown"
        assert signin_page.email_field.is_displayed(), "Email input field isn't shown"
        assert signin_page.password_field.is_displayed(), "Password input field isn't shown"
        assert signin_page.signin_button.is_displayed(), "Signin submit button isn't shown"
        workspace = signin_page.enter_email(email).enter_password(password).click_on_signin_button_correct_creds()
        assert workspace.diprella_logo.is_displayed(), "Diprella logo isn't shown"
        assert workspace.course_search.is_displayed(), "Course search field isn't shown"
        assert workspace.lector_menu.is_displayed(), "Lector menu field isn't shown"
        assert workspace.user_menu.is_displayed(), "User menu field isn't shown"
        assert workspace.recommendations.is_displayed(), "Recommended courses isn't shown"
        assert workspace.popular.is_displayed(), "Popular courses isn't shown"

    def test_login_with_incorrect_email(self, url, email, password, incorrect_email, incorrect_password):
        signin_page = self.main_page.get_mainpage_url(url).click_on_signin_link()
        assert signin_page.diprella_logo.is_displayed(), "Diprella logo isn't shown"
        assert signin_page.signup_link.is_displayed(), "SignUp link isn't shown"
        assert signin_page.facebook_login.is_displayed(), "Facebook signin button isn't shown"
        assert signin_page.google_login.is_displayed(), "Google signin button isn't shown"
        assert signin_page.linkedin_login.is_displayed(), "Linkedin signin button isn't shown"
        assert signin_page.email_field.is_displayed(), "Email input field isn't shown"
        assert signin_page.password_field.is_displayed(), "Password input field isn't shown"
        assert signin_page.signin_button.is_displayed(), "Signin submit button isn't shown"
        signin_page.enter_email(incorrect_email).enter_password(password).click_on_signin_button_incorrect_email()
        assert signin_page.incorrect_email_message.is_displayed(), "Message about incorrect email isn't shown"

    def test_login_with_incorrect_pass(self, url, email, password, incorrect_email, incorrect_password):
        signin_page = self.main_page.get_mainpage_url(url).click_on_signin_link()
        assert signin_page.diprella_logo.is_displayed(), "Diprella logo isn't shown"
        assert signin_page.signup_link.is_displayed(), "SignUp link isn't shown"
        assert signin_page.facebook_login.is_displayed(), "Facebook signin button isn't shown"
        assert signin_page.google_login.is_displayed(), "Google signin button isn't shown"
        assert signin_page.linkedin_login.is_displayed(), "Linkedin signin button isn't shown"
        assert signin_page.email_field.is_displayed(), "Email input field isn't shown"
        assert signin_page.password_field.is_displayed(), "Password input field isn't shown"
        assert signin_page.signin_button.is_displayed(), "Signin submit button isn't shown"
        signin_page.enter_email(email).enter_password(incorrect_password).click_on_signin_button_incorrect_pass()
        assert signin_page.incorrect_pass_message.is_displayed(), "Message about incorrect password isn't shown"
