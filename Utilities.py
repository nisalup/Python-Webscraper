from selenium import webdriver
import configparser, numpy as np, pandas as pd, re

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
        fp.set_preference('network.proxy.type', 1)
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
        fp.set_preference('general.useragent.override', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A')
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
    def createResultArray(result_dict):
        regex = re.compile('[^a-zA-Z]')
        countries = [
         'Brazil', 'Germany', 'France', 'Spain', 'Argentina', 'Belgium', 'England', 'Portugal', 'Uruguay',
         'Croatia', 'Colombia', 'Poland', 'Russia', 'Denmark', 'Mexico', 'Switzerland', 'Egypt', 'Nigeria',
         'Senegal', 'Serbia', 'Sweden', 'Peru', 'Iceland', 'Japan', 'Costa Rica', 'Morocco', 'South Korea',
         'Australia', 'Iran', 'Tunisia', 'Panama', 'Saudi Arabia']
        countries = sorted(countries)
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
                        if country == 'southkorea' and result_dict[scraped_site][country] == 'korearepublic':
                            country = 'korearepublic'
                        temp_array.append(result_dict[scraped_site][country])
                    else:
                        temp_array.append('NA')

            else:
                for country in countries:
                    temp_array.append('NA')

            A.append(temp_array)

        print(A)
        np_arr = np.array(A)
        df = pd.DataFrame(np_arr.T, index=countries, columns=scraped_sites)
        return df

    @staticmethod
    def getResultsPath():
        config = configparser.ConfigParser()
        config.read('config.ini')
        RESULT_PATH = config['DEFAULT']['RESULT_PATH']
        return RESULT_PATH

