from selenium import webdriver
import configparser
import numpy as np
import pandas as pd

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
        fp.set_preference("network.proxy.type", 1)
        fp.set_preference("network.proxy.http", PROXY_HOST)
        fp.set_preference("network.proxy.http_port", int(PROXY_PORT))
        fp.set_preference("network.proxy.https", PROXY_HOST)
        fp.set_preference("network.proxy.https_port", int(PROXY_PORT))
        fp.set_preference("network.proxy.ssl", PROXY_HOST)
        fp.set_preference("network.proxy.ssl_port", int(PROXY_PORT))
        fp.set_preference("network.proxy.ftp", PROXY_HOST)
        fp.set_preference("network.proxy.ftp_port", int(PROXY_PORT))
        fp.set_preference("network.proxy.socks", PROXY_HOST)
        fp.set_preference("network.proxy.socks_port", int(PROXY_PORT))
        fp.set_preference("general.useragent.override",
                          "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A")
        fp.update_preferences()
        return webdriver.Firefox(firefox_profile=fp)

    @staticmethod
    def getWebDriverWithoutProfile():
        config = configparser.ConfigParser()
        config.read('config.ini')
        PROXY_PORT = config['DEFAULT']['PROXY_PORT']
        PROXY_HOST = config['DEFAULT']['PROXY_HOST']
        myProxy = PROXY_HOST + ":" + PROXY_PORT

        proxy = webdriver.common.proxy.Proxy({
            'proxyType': webdriver.common.proxy.ProxyType.MANUAL,
            'httpProxy': myProxy,
            'ftpProxy': myProxy,
            'sslProxy': myProxy
        })

        return webdriver.Firefox(proxy=proxy)

    @staticmethod
    def getWebDriverDefaultWait():

        config = configparser.ConfigParser()
        config.read('config.ini')
        WEB_DRIVER_WAIT = config['DEFAULT']['WEB_DRIVER_WAIT']
        return WEB_DRIVER_WAIT

    @staticmethod
    def createResultArray(result_WilliamHill, result_Bet365, result_SkyBet, result_PaddyPower):

        countries = ['Brazil', 'Germany', 'France', 'Spain', 'Argentina', 'Belgium', 'England', 'Portugal', 'Uruguay',
                     'Croatia', 'Colombia', 'Poland', 'Russia', 'Denmark', 'Mexico', 'Switzerland', 'Egypt', 'Nigeria',
                     'Senegal', 'Serbia', 'Sweden', 'Peru', 'Iceland', 'Japan', 'Costa Rica', 'Morocco', 'South Korea',
                     'Australia', 'Iran', 'Tunisia', 'Panama', 'Saudi Arabia']
        countries = sorted(countries)
        scraped_sites = ['William Hill', 'Bet365', 'SkyBet', 'PaddyPower']

        A = np.zeros((32, 4))

        i = 0
        if len(result_WilliamHill[1]) == 32:

            for item in A.T[0]:
                item = result_WilliamHill[1][i]
                i += 1

        i = 0
        if len(result_Bet365[1]) == 32:

            for item in A.T[1]:
                item = result_Bet365[1][i]
                i += 1

        i = 0
        if len(result_SkyBet[1]) == 32:

            for item in A.T[2]:
                item = result_SkyBet[1][i]
                i += 1

        i = 0
        if len(result_PaddyPower[1]) == 32:

            for item in A.T[3]:
                item = result_PaddyPower[1][i]
                i += 1

        df = pd.DataFrame(A, index=countries, columns=scraped_sites)

        return df

    @staticmethod
    def getResultsPath():
        config = configparser.ConfigParser()
        config.read('config.ini')
        RESULT_PATH = config['DEFAULT']['RESULT_PATH']
        return RESULT_PATH

