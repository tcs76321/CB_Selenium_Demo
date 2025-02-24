# import pytest
# from selenium import webdriver
# from pages.index import HomePage
# from utils.config_loader import load_config
# from utils.logger import setup_logger
#
# logger = setup_logger()
#
# @pytest.fixture
# def setup_driver():
#     driver = webdriver.Chrome()
#     yield driver
#     driver.quit()