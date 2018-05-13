from selenium import webdriver
import configparser, numpy as np, pandas as pd, re
from Website import Website
import re
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class Utilities:

    @staticmethod
    def removeEscapeData(scrapedString):
        scrapedString = scrapedString.replace('\t', '')
        scrapedString = scrapedString.replace('\n', '')
        scrapedString = scrapedString.strip()
        return scrapedString

    @staticmethod
    def getWebDriver():
        fp = webdriver.FirefoxProfile()
        config = configparser.ConfigParser()
        config.read('config.ini')
        PROXY_PORT = config['DEFAULT']['PROXY_PORT']
        PROXY_HOST = config['DEFAULT']['PROXY_HOST']
        fp.set_preference('network.proxy.type', 0)
        fp.set_preference('network.proxy.http', PROXY_HOST)
        fp.set_preference('network.proxy.http_port', int(PROXY_PORT))
        fp.set_preference('network.proxy.https', PROXY_HOST)
        fp.set_preference('network.proxy.https_port', int(PROXY_PORT))
        fp.set_preference('network.proxy.ssl', PROXY_HOST)
        fp.set_preference('network.proxy.ssl_port', int(PROXY_PORT))
        fp.set_preference('network.proxy.ftp', PROXY_HOST)
        fp.set_preference('network.proxy.ftp_port', int(PROXY_PORT))
        fp.set_preference('network.proxy.socks', PROXY_HOST)
        fp.set_preference('network.proxy.socks_port', int(PROXY_PORT))
        fp.set_preference("general.useragent.override", "whater_useragent")
        fp.set_preference("general.useragent.override", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A")
        fp.update_preferences()
        return webdriver.Firefox(firefox_profile=fp)

    @staticmethod
    def getWebDriverWithoutProfile():
        config = configparser.ConfigParser()
        config.read('config.ini')
        PROXY_PORT = config['DEFAULT']['PROXY_PORT']
        PROXY_HOST = config['DEFAULT']['PROXY_HOST']
        myProxy = PROXY_HOST + ':' + PROXY_PORT
        proxy = webdriver.common.proxy.Proxy({'proxyType':webdriver.common.proxy.ProxyType.MANUAL,
         'httpProxy':myProxy,
         'ftpProxy':myProxy,
         'sslProxy':myProxy})
        return webdriver.Firefox(proxy=proxy)

    @staticmethod
    def getWebDriverDefaultWait():
        config = configparser.ConfigParser()
        config.read('config.ini')
        WEB_DRIVER_WAIT = config['DEFAULT']['WEB_DRIVER_WAIT']
        return WEB_DRIVER_WAIT

    @staticmethod
    def getWebDriverJSDisabled():
        fp = webdriver.FirefoxProfile()
        fp.set_preference("browser.download.folderList", 2)
        fp.set_preference("javascript.enabled", False)

        browser = webdriver.Firefox(firefox_profile=fp)
        browser.get("about:config")
        actions = ActionChains(browser)
        actions.send_keys(Keys.RETURN)
        actions.send_keys("javascript.enabled")
        actions.perform()
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.RETURN)
        actions.send_keys(Keys.F5)
        actions.perform()
        return browser

    @staticmethod
    def createResultArray(result_dict):
        regex = re.compile('[^a-zA-Z]')
        countries_raw = [
         'Brazil', 'Germany', 'France', 'Spain', 'Argentina', 'Belgium', 'England', 'Portugal', 'Uruguay',
         'Croatia', 'Colombia', 'Poland', 'Russia', 'Denmark', 'Mexico', 'Switzerland', 'Egypt', 'Nigeria',
         'Senegal', 'Serbia', 'Sweden', 'Peru', 'Iceland', 'Japan', 'Costa Rica', 'Morocco', 'South Korea',
         'Australia', 'Iran', 'Tunisia', 'Panama', 'Saudi Arabia']
        countries = sorted(countries_raw)
        for i, country in enumerate(countries):
            country = regex.sub('', country).lower()
            countries[i] = re.sub('\\s+', '', country)

        scraped_sites = ['WilliamHill', 'Bet365', 'SkyBet', 'PaddyPower']
        A = []
        for scraped_site in scraped_sites:
            if len(scraped_site) > 0:
                temp_array = []
                for country in countries:
                    if country in result_dict[scraped_site]:
                        temp_array.append(result_dict[scraped_site][country])
                    else:
                        temp_array.append('NA')

            else:
                for country in countries:
                    temp_array.append('NA')

            A.append(temp_array)

        np_arr = np.array(A)
        df = pd.DataFrame(np_arr.T, index=countries_raw, columns=scraped_sites)
        return df

    @staticmethod
    def getResultsPath():
        config = configparser.ConfigParser()
        config.read('config.ini')
        RESULT_PATH = config['DEFAULT']['RESULT_PATH']
        return RESULT_PATH

    @staticmethod
    def processResultData(odds, countries, websiteID):

        regex = re.compile('[^a-zA-Z]')
        odds_decoded = []
        countries_decoded = []
        scrape_results = {}
        for odd in odds:
            data = ''
            if websiteID == Website.WILLIAMHILL:
                data = Utilities.removeEscapeData(odd.text)
            else:
                data = odd.text
            data = data.strip()
            odds_decoded.append(data)

        for country in countries:
            data = ''
            if websiteID == Website.WILLIAMHILL:
                data = Utilities.removeEscapeData(country.text)
            else:
                data = country.text
            data = data.strip()
            data = regex.sub('', data).lower()
            data = re.sub(r'\s+', '', data)
            if data == 'korearepublic' and websiteID == Website.SKYBET:
                data = 'southkorea'
            countries_decoded.append(data)


        if len(countries_decoded) == len(odds_decoded):
            i = 0
            for item in countries_decoded:
                scrape_results[item] = odds_decoded[i]
                i += 1

        return scrape_results

