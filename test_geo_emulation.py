import unittest
from decimal import Decimal
from typing import List

from webdriver_factory import WebDriverFactory


class GeoEmulationTEst(unittest.TestCase):

    driver = None
    search_page = None

    @classmethod
    def setUpClass(cls) -> None:
        """Предустановка. Выполняется один раз перед всеми тестами."""
        cls.driver = WebDriverFactory.get_driver()

    def setUp(self) -> None:
        self.driver = GeoEmulationTEst.driver

    @classmethod
    def tearDownClass(cls) -> None:
        """Выполняется один раз после всех тестов"""
        cls.driver.quit()

    def tearDown(self) -> None:
        self.driver.save_screenshot('test-reports/' + self.id() + '.png')

    def test(self):
        self.driver.get('https://browserleaks.com/geo')