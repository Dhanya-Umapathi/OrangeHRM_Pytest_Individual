"""Author: Suvetha (Expleo)"""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.LoginPage import LoginPage
from Utility import utility_file, console_logger

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:

    """TestLogin class contains test methods to perform login tests."""

    log = console_logger.get_logger()

    @pytest.mark.smoke
    def test_valid_login(self):

        """This test case checks the workflow of logging into the application,
        verifying a valid login."""

        login = LoginPage(self.driver)  # object reference
        username = utility_file.get_config("valid login details", "username")
        password = utility_file.get_config("valid login details", "password")
        login.login(username, password)
        login.assert_login_successful()
        self.log.info("Login successful and verified")
