import json
import os
from typing import Set

from dotenv import load_dotenv
from fake_useragent import UserAgent
from undetected_chromedriver import ChromeOptions

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

BOT_DIR = 'bot'

BOT_PATH = os.path.join(BASE_DIR, BOT_DIR)

MONITORING_SITES_FILENAME = 'sites.json'

MONITORING_SITES_PATH = os.path.join(BASE_DIR, MONITORING_SITES_FILENAME)

load_dotenv(dotenv_path=os.path.join(BASE_DIR, '.env'))

BOT_TOKEN = os.getenv('BOT_TOKEN')

SNAPSHOTS_DIR = 'snapshots'

SNAPSHOTS_PATH = os.path.join(BOT_PATH, SNAPSHOTS_DIR)

SITE_SNAPSHOTS_DIR = 'sites'

SITE_SNAPSHOTS_PATH = os.path.join(SNAPSHOTS_PATH, SITE_SNAPSHOTS_DIR)

ADMINS_ID = [int(admin.strip()) for admin in os.getenv('TELEGRAM_ADMINS_IDS').split(',')]

ALLOWED_CHATS_IDS = [int(admin.strip()) for admin in os.getenv('ALLOWED_CHATS_IDS').split(',')]

PROXY_AUTH_NAME = os.getenv('PROXY_AUTH_NAME')

PROXY_AUTH_PASSWORD = os.getenv('PROXY_AUTH_PASSWORD')


def get_newsletter_chats_ids() -> Set[int]:
    newsletter_chats_ids = []
    newsletter_chats_ids.extend(ADMINS_ID)
    newsletter_chats_ids.extend(ALLOWED_CHATS_IDS)
    return set(newsletter_chats_ids)


def get_monitoring_sites() -> dict:
    with open(MONITORING_SITES_PATH) as json_file:
        sites = json.load(json_file)
        lists_sites = sites['lists_sites']
        every_tick_sites = sites['every-tick']

    monitoring_sites = []
    for site in lists_sites.values():
        monitoring_sites.append(site)
        monitoring_sites.extend(every_tick_sites.values())

    result = {
        'lists_sites': lists_sites,
        'every_tick_sites': every_tick_sites,
        'monitoring_sites': monitoring_sites
    }
    return result


def get_webdriver_options() -> ChromeOptions:
    chrome_options = ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument(f"--user-agent={UserAgent().random}")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    return chrome_options


class MessageText:
    NO_PERMISSION = '<b>❌ You dont have enough permissions to use this bot. Correct this with administartions.❌</b>'
    ADMIN_PANEL = 'We glad to see you <b>@{username}</b> in admin panel! To know what sites is monitoring now type <b>/list</b> command'
    ALL_SITES_DETAILS = '''
<b>🧩 Information about monitoring sites 🧩</b>
{sites_details}
'''
    SITE_CHANGED = '''
<b>New changes on website: <a href='{url}'>{name}</a></b>
<b>Category:</b> {category}
<b>Date time:</b> {date_and_time}
<b>Changes:</b>
{changes}
'''
    FAQ = '''
This bot is created to monitor changes on websites 🌐. 
We are utilizing Python, Selenium, and aiogram as the stack for this bot 🤖. 
However, there are a couple of important details that you should understand. Since the bot visits the site very often, there is a chance of getting blocked 🚫. 
It is highly recommended to use proxies to prevent sites from blocking your connection 🔄. 
The more proxies you use, the better for your bot. However, the chance of being blocked for a while is always there. 
So, if you want the most stable and clear work, consider purchasing more proxies 🔒.
Our script only performs the task given to it, and I guarantee its fulfillment if the connection is not blocked. 
Buy more proxies or wait some time until the site unblocks your connection ⌛. 
Please do not claim that the bot does not work correctly or not at all. 
The stability and performance of this bot are directly related to the quantity and quality of proxies you provide for it. 
Thank you for your understanding. 🙏
    '''
