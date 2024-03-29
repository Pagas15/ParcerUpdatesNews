import datetime
import os.path

from telebot import TeleBot
from selenium.webdriver.common.by import By
from bot.misc.observer import SiteObserver
from seleniumwire.undetected_chromedriver.v2 import Chrome

from bot.config import SITE_SNAPSHOTS_PATH, get_webdriver_options, BOT_TOKEN, \
    MessageText, seleniumwire_options, get_newsletter_chats_ids, get_monitoring_sites
from bot.misc.snapshots import SiteSnapshot

if __name__ == "__main__":
    sites = get_monitoring_sites()

    bot = TeleBot(BOT_TOKEN, parse_mode='HTML')

    while True:
        webdriver = Chrome(options=get_webdriver_options(), seleniumwire_options=seleniumwire_options)
        for site in sites['monitoring_sites']:
            snapshot_path = os.path.join(SITE_SNAPSHOTS_PATH, f'{site["name"]}-snapshot.html')
            site_snapshot = SiteSnapshot(snapshot_path=snapshot_path)
            site_observer = SiteObserver(chrom_webdriver=webdriver, site_snapshot=site_snapshot)
            if site_observer.monitor(site['url'], By.XPATH, site['x-path'], site['sleep-time']):
                if site['chats'] is None:
                    chats = get_newsletter_chats_ids()
                else:
                    chats = site['chats']

                for chat_id in chats:
                    changes_text = '\n\n'.join(site_snapshot.get_snapshot().split('\n'))
                    bot.send_message(chat_id=chat_id, text=MessageText.SITE_CHANGED.format(
                        url=site['url'],
                        name=site['name'],
                        category=site['category'],
                        date_and_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M'),
                        changes=changes_text,
                    ))

        webdriver.quit()
