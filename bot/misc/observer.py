import logging
import time

import validators

from abc import ABC, abstractmethod

from selenium.common import TimeoutException
from seleniumwire.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from bot.misc.snapshots import SiteSnapshot


class Observer(ABC):

    @abstractmethod
    def monitor(self) -> bool:
        pass


class SiteObserver(Observer):
    chrome_driver: Chrome = None
    site_snapshot: SiteSnapshot = None
    loading_timeout = 180

    def __init__(self, chrom_webdriver: Chrome, site_snapshot: SiteSnapshot):
        self.chrome_driver = chrom_webdriver
        self.site_snapshot = site_snapshot
        self.setup_window()

    def monitor(self, url: str, by: str, by_value: str, sleep_time: int) -> bool:
        validators.url(url)
        try:
            self.chrome_driver.get(url)
            time.sleep(sleep_time)
            element = WebDriverWait(self.chrome_driver, self.loading_timeout).until(
                EC.presence_of_element_located((by, by_value)))
            element_content = element.text

        except TimeoutException:
            logging.exception(f'Loading took too much time! {url}')
            return False

        try:
            if self.site_snapshot.get_snapshot() != element_content:
                self.site_snapshot.make_snapshot(element_content)
                ActionChains(self.chrome_driver).move_to_element(
                    self.chrome_driver.find_element(by, by_value)).perform()
                self.chrome_driver.execute_script("document.body.style.zoom='65%'")
                element.screenshot(self.site_snapshot.screenshot_path)
                return True

            return False

        except FileNotFoundError:
            self.site_snapshot.make_snapshot(element_content)

    def setup_window(self, required_width=None, required_height=None):
        if required_width is None:
            required_width = self.chrome_driver.execute_script('return document.body.parentNode.scrollWidth')

        if required_height is None:
            required_height = self.chrome_driver.execute_script('return document.body.parentNode.scrollHeight')

        self.chrome_driver.set_window_size(required_width, required_height)
