import urllib.request
import urllib.parse
import ssl
import requests
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class ApexSearch :
    ssl._create_default_https_context = ssl._create_unverified_context
    CHROME_DRIVER_DIR = "/usr/local/bin/chromedriver"

    # 请求头，使用cookie实现模拟登录
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.4 Safari/605.1.15',        
        'cookie':"X-Mapping-Server=s13; __cflb=02DiuFQAkRrzD1P1mdm8JatZXtAyjoPD2phHy4GmPc5XJX-Mapping-Server=s13; __cflb=02DiuFQAkRrzD1P1mdm8JatZXtAyjoPD2phHy4GmPc5XJ",
    }
    seacrh_url = "https://api.tracker.gg/api/v2/apex/standard/profile/origin/"
    def SearchMember(self,o_name):
        seacrh_url = self.seacrh_url+o_name
        # session = requests.session()
        # option = webdriver.ChromeOptions()
        # options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # options.add_experimental_option('useAutomationExtension', False)
        # options.add_argument("--disable-blink-features=AutomationControlled")
        # options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36")
        # driver = webdriver.Chrome(options=options, executable_path=r'驱动路径')
        # driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        # driver.execute_cdp_cmd('Network.setUserAgentOverride', {    "userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
        # print(driver.execute_script("return navigator.userAgent;"))

        chrome_options = webdriver.ChromeOptions()
        caps = DesiredCapabilities().CHROME
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--remote-debugging-port=9222")
        chrome_options.add_argument("--headless")  # Runs Chrome in headless mode.
        chrome_options.add_argument('--no-sandbox')  # # Bypass OS security model
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")

        browser = webdriver.Chrome(desired_capabilities=caps, executable_path=self.CHROME_DRIVER_DIR, options=chrome_options)

        browser.get(seacrh_url)
        print(browser.page_source)
        browser.quit()
        # scraper = cfscrape.create_scraper(sess=session,delay=10,)
        # # scraper = cfscrape.create_scraper(delay = 10)
        # header_str = "GET / HTTP/1.1\r\n"
        # cookie_value, user_agent = cfscrape.get_cookie_string(seacrh_url)
        # header_str += "Cookie: %s\r\nUser-Agent: %s\r\n" % (cookie_value, user_agent)
        # request = scraper.post(seacrh_url).content
        # print(header_str)
        # user_info = urllib.request.urlopen(request)
        # if user_info:
        #     return "未找到用户，请使用橘子平台昵称"
        # user_info = user_info.json()
        # print(user_info)
        return "测试"
        pass
