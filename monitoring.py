import datetime
import json
import os.path

from telebot import TeleBot
from telebot.types import InputFile
from selenium.webdriver.common.by import By
from bot.misc.observer import SiteObserver
from seleniumwire import webdriver

from bot.config import SITE_SNAPSHOTS_PATH, SCREENSHOTS_PATH, get_webdriver_options, MONITORING_SITES_PATH, BOT_TOKEN, \
    MessageText, seleniumwire_options, get_newsletter_chats_ids
from bot.misc.snapshots import SiteSnapshot

if __name__ == "__main__":
    with open(MONITORING_SITES_PATH) as json_file:
        sites = json.load(json_file)
        lists_sites = sites['lists_sites']
        every_tick_sites = sites['every-tick']
        monitoring_sites = []
        for site in lists_sites.values():
            monitoring_sites.append(site)
            monitoring_sites.extend(every_tick_sites.values())

    bot = TeleBot(BOT_TOKEN, parse_mode='HTML')

    while True:
        webdriver = webdriver.Chrome(options=get_webdriver_options(), seleniumwire_options=seleniumwire_options)
        for site in every_tick_sites.values():
            pass

        for site in monitoring_sites:
            screenshot_path = os.path.join(SCREENSHOTS_PATH, f'{site["name"]}-screenshot.png')
            snapshot_path = os.path.join(SITE_SNAPSHOTS_PATH, f'{site["name"]}-snapshot.html')
            site_snapshot = SiteSnapshot(screenshot_path=screenshot_path,
                                         snapshot_path=snapshot_path)
            site_observer = SiteObserver(chrom_webdriver=webdriver, site_snapshot=site_snapshot)
            if site_observer.monitor(site['url'], By.XPATH, site['x-path'], site['sleep-time']):
                for chat_id in get_newsletter_chats_ids():
                    bot.send_message(chat_id=chat_id, text=MessageText.SITE_CHANGED.format(
                        url=site['url'],
                        name=site['name'],
                        category=site['category'],
                        date_and_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M'),
                        changes=site_snapshot.get_snapshot(),
                    ))
                    bot.send_photo(chat_id=chat_id, photo=InputFile(screenshot_path))

        webdriver.quit()
