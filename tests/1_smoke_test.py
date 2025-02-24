import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.index import HomePage
from utils.config_loader import load_config
from utils.logger import setup_logger

logger = setup_logger()

@pytest.fixture
def setup_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.mark.smoke
def test_homepage_loads(setup_driver):
    """Verify that the homepage loads and displays correct text in key places."""
    config = load_config()
    driver = setup_driver
    home_page = HomePage(driver)
    home_page.open(config["base_url"])
    logger.info("Homepage loaded successfully.")
    assert "Commerce Bank" in driver.title

@pytest.mark.smoke
def test_dropdown_navigation(setup_driver):
    """Verify that clicking the `Wealth` button navigates to the correct page."""
    config = load_config()
    driver = setup_driver
    home_page = HomePage(driver)
    home_page.open(config["base_url"])

    dropdown_locator = (By.ID, "Wealth-tab-md")
    home_page.click(dropdown_locator)

    logger.info("Navigated to Wealth page correctly.")
    assert "Wealth Management" in driver.title
