import allure


class TestPages(object):
    @allure.title("Verify the Main Page")
    @allure.description_html("Verifying <b>Main Page</b> that it contains required elements")
    def test_main_page(self, url, email, password, incorrect_email, incorrect_password):
        self.main_page.get_url(url)
        with allure.step("Check that Diprella main page header is present and displayed"):
            assert self.main_page.diprella_header.is_displayed(), "Header isn't displayed"
        with allure.step("Check that Sign in link present in header and displayed"):
            assert self.main_page.signin_link.is_displayed(), "Signin link not found"

    @allure.title("Verify that user can login with the correct credentials")
    @allure.description_html("When <b>user</b> logs into portal, workspace page is loaded")
    def test_login_with_correct_credentials(self, url, email, password, incorrect_email, incorrect_password):
        signin_page = self.main_page.get_url(url).click_on_signin_link()
        with allure.step("Check that Diprella logo is present on the page and displayed"):
            assert signin_page.diprella_logo.is_displayed(), "Diprella logo isn't shown"
        with allure.step("Check that Sign up link is present on the page and displayed"):
            assert signin_page.signup_link.is_displayed(), "Sign Up link isn't shown"
        with allure.step("Check that Facebook signin button is present on the page and displayed"):
            assert signin_page.facebook_login.is_displayed(), "Facebook signin button isn't shown"
        with allure.step("Check that Google signin button is present on the page and displayed"):
            assert signin_page.google_login.is_displayed(), "Google signin button isn't shown"
        with allure.step("Check that LinkedIn signin button is present on the page and displayed"):
            assert signin_page.linkedin_login.is_displayed(), "LinkedIn signin button isn't shown"
        with allure.step("Check that Email input field is present on the page and displayed"):
            assert signin_page.email_field.is_displayed(), "Email input field isn't shown"
        with allure.step("Check that Password field is present on the page and displayed"):
            assert signin_page.password_field.is_displayed(), "Password input field isn't shown"
        with allure.step("Check that Sign in submit button is present on the page and displayed"):
            assert signin_page.signin_button.is_displayed(), "Sign in submit button isn't shown"
        workspace = signin_page.enter_email(email).enter_password(password).click_on_signin_button_correct_creds()
        with allure.step("Check that Diprella logo is present on the page and displayed"):
            assert workspace.diprella_logo.is_displayed(), "Diprella logo isn't shown"
        with allure.step("Check that Course search field is present on the page and displayed"):
            assert workspace.course_search.is_displayed(), "Course search field isn't shown"
        with allure.step("Check that Lector menu is present on the page and displayed"):
            assert workspace.lector_menu.is_displayed(), "Lector menu isn't shown"
        with allure.step("Check that User menu is present on the page and displayed"):
            assert workspace.user_menu.is_displayed(), "User menu isn't shown"
        with allure.step("Check that Recommended courses section is present on the page and displayed"):
            assert workspace.recommendations.is_displayed(), "Recommended courses section isn't shown"
        with allure.step("Check that Recommended courses section is present on the page and displayed"):
            assert workspace.popular.is_displayed(), "Popular courses section isn't shown"

    @allure.title("Verify that user can not login with incorrect email")
    @allure.description_html("When <b>user</b> enter incorrect email, \
    alert message should appears and user should stay on the same page")
    def test_login_with_incorrect_email(self, url, email, password, incorrect_email, incorrect_password):
        signin_page = self.main_page.get_url(url).click_on_signin_link()
        with allure.step("Check that Diprella logo is present on the page and displayed"):
            assert signin_page.diprella_logo.is_displayed(), "Diprella logo isn't shown"
        with allure.step("Check that Sign up link is present on the page and displayed"):
            assert signin_page.signup_link.is_displayed(), "Sign Up link isn't shown"
        with allure.step("Check that Facebook signin button is present on the page and displayed"):
            assert signin_page.facebook_login.is_displayed(), "Facebook signin button isn't shown"
        with allure.step("Check that Google signin button is present on the page and displayed"):
            assert signin_page.google_login.is_displayed(), "Google signin button isn't shown"
        with allure.step("Check that LinkedIn signin button is present on the page and displayed"):
            assert signin_page.linkedin_login.is_displayed(), "LinkedIn signin button isn't shown"
        with allure.step("Check that Email input field is present on the page and displayed"):
            assert signin_page.email_field.is_displayed(), "Email input field isn't shown"
        with allure.step("Check that Password field is present on the page and displayed"):
            assert signin_page.password_field.is_displayed(), "Password input field isn't shown"
        with allure.step("Check that Sign in submit button is present on the page and displayed"):
            assert signin_page.signin_button.is_displayed(), "Sign in submit button isn't shown"
        signin_page.enter_email(incorrect_email).enter_password(password).click_on_signin_button_incorrect_email()
        with allure.step("Check if alert message about appears"):
            assert signin_page.incorrect_email_message.is_displayed(), "Message about incorrect email isn't shown"

    @allure.title("Verify that user can not login with incorrect password")
    @allure.description_html("When <b>user</b> enter incorrect password, \
    alert message should appears and user should stay on the same page")
    def test_login_with_incorrect_pass(self, url, email, password, incorrect_email, incorrect_password):
        signin_page = self.main_page.get_url(url).click_on_signin_link()
        with allure.step("Check that Diprella logo is present on the page and displayed"):
            assert signin_page.diprella_logo.is_displayed(), "Diprella logo isn't shown"
        with allure.step("Check that Sign up link is present on the page and displayed"):
            assert signin_page.signup_link.is_displayed(), "Sign Up link isn't shown"
        with allure.step("Check that Facebook signin button is present on the page and displayed"):
            assert signin_page.facebook_login.is_displayed(), "Facebook signin button isn't shown"
        with allure.step("Check that Google signin button is present on the page and displayed"):
            assert signin_page.google_login.is_displayed(), "Google signin button isn't shown"
        with allure.step("Check that LinkedIn signin button is present on the page and displayed"):
            assert signin_page.linkedin_login.is_displayed(), "LinkedIn signin button isn't shown"
        with allure.step("Check that Email input field is present on the page and displayed"):
            assert signin_page.email_field.is_displayed(), "Email input field isn't shown"
        with allure.step("Check that Password field is present on the page and displayed"):
            assert signin_page.password_field.is_displayed(), "Password input field isn't shown"
        with allure.step("Check that Sign in submit button is present on the page and displayed"):
            assert signin_page.signin_button.is_displayed(), "Sign in submit button isn't shown"
        signin_page.enter_email(email).enter_password(incorrect_password).click_on_signin_button_incorrect_pass()
        with allure.step("Check if alert message about appears"):
            assert signin_page.incorrect_pass_message.is_displayed(), "Message about incorrect password isn't shown"

    @allure.title("Verify that user can not login with incorrect credentials")
    @allure.description_html("When <b>user</b> enter incorrect credentials, \
    alert message should appears and user should stay on the same page")
    def test_login_with_incorrect_credentials(self, url, email, password, incorrect_email, incorrect_password):
        signin_page = self.main_page.get_url(url).click_on_signin_link()
        with allure.step("Check that Diprella logo is present on the page and displayed"):
            assert signin_page.diprella_logo.is_displayed(), "Diprella logo isn't shown"
        with allure.step("Check that Sign up link is present on the page and displayed"):
            assert signin_page.signup_link.is_displayed(), "Sign Up link isn't shown"
        with allure.step("Check that Facebook signin button is present on the page and displayed"):
            assert signin_page.facebook_login.is_displayed(), "Facebook signin button isn't shown"
        with allure.step("Check that Google signin button is present on the page and displayed"):
            assert signin_page.google_login.is_displayed(), "Google signin button isn't shown"
        with allure.step("Check that LinkedIn signin button is present on the page and displayed"):
            assert signin_page.linkedin_login.is_displayed(), "LinkedIn signin button isn't shown"
        with allure.step("Check that Email input field is present on the page and displayed"):
            assert signin_page.email_field.is_displayed(), "Email input field isn't shown"
        with allure.step("Check that Password field is present on the page and displayed"):
            assert signin_page.password_field.is_displayed(), "Password input field isn't shown"
        with allure.step("Check that Sign in submit button is present on the page and displayed"):
            assert signin_page.signin_button.is_displayed(), "Sign in submit button isn't shown"
        signin_page.enter_email(incorrect_email).enter_password(incorrect_password) \
            .click_on_signin_button_incorrect_email()
        with allure.step("Check if alert message about appears"):
            assert signin_page.incorrect_email_message.is_displayed(), "Message about incorrect credentials isn't shown"
