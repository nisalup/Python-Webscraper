from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from Utilities import Utilities
import re

class SkyBet:

    def scrapeSkyBet(self):
        print('Scraping From SkyBet started.')
        odds_decoded = []
        countries_decoded = []
        scrape_results = {}
        regex = re.compile('[^a-zA-Z]')
        driver = webdriver.Firefox()
        try:
            driver.get('https://m.skybet.com/football/competitions')
            driver.implicitly_wait(2)
            WebDriverWait(driver, int(Utilities.getWebDriverDefaultWait())).until(EC.presence_of_element_located((By.CLASS_NAME, 'js-page__cookies-accept')))
            cookie_agreement_button_xpath = "//a[contains(@class,'js-page__cookies-accept')]"
            cookie_agreement_button = driver.find_element_by_xpath(cookie_agreement_button_xpath)
            cookie_agreement_button.click()
            driver.implicitly_wait(2)
            first_selection_button_xpath = "//li[contains(@class, 'accordion--generic') and contains(.//span, 'World Cup 2018')]"
            first_selection_button = driver.find_element_by_xpath(first_selection_button_xpath)
            first_selection_button.click()
            driver.implicitly_wait(2)
            outright_button_xpath = "//a[contains(@data-toggle-tab,'competitions-world-cup-2018-outrights')]"
            outright_button_button = driver.find_element_by_xpath(outright_button_xpath)
            outright_button_button.click()
            driver.implicitly_wait(2)
            table_load_button_xpath = "//a[contains(@data-analytics, '[Competitions] - World Cup 2018') and .//span='World Cup 2018 Winner']"
            table_load_button = driver.find_element_by_xpath(table_load_button_xpath)
            table_load_button.click()
            driver.implicitly_wait(2)
            load_more_button_xpath = "//a[@class='_1ey6ouwa']"
            load_more_button = driver.find_element_by_xpath(load_more_button_xpath)
            load_more_button.click()
            driver.implicitly_wait(5)
            odds = driver.find_elements_by_xpath("//div[@class='_1m5cvgr']/div[2]/div/div/div[2]/div/span")
            countries = driver.find_elements_by_xpath("//div[@class='_1m5cvgr']/div[2]/div/div/div/div[not(contains(@class,'_1v3logkf'))]")
            for odd in odds:
                data = odd.text
                data = data.strip()
                odds_decoded.append(data)

            for country in countries:
                data = country.text
                data = data.strip()
                data = regex.sub('', data).lower()
                data = re.sub(r'\s+', '', data)
                if data == 'korearepublic':
                    data = 'southkorea'
                countries_decoded.append(data)

        except NoSuchElementException as ex:
            print('Exception at SkyBet.py')
            print('The element could not be located or the xpath has changed.')
            print('If this is not the case, try increasing the timeout to allow more time for the website to load.')
            print('Error Message:')
            print(ex)
        except TimeoutException as ex:
            print('Exception at SkyBet.py')
            print('The connection has been lost. Proxy addresses change regularly, so try with a new address')
            print('Error Message:')
            print(ex)
        except Exception as ex:
            print('Exception at SkyBet.py')
            print('Unchecked Error Occured')
            print(ex)

        if len(countries_decoded) == len(odds_decoded):
            i = 0
            for item in countries_decoded:
                scrape_results[item] = odds_decoded[i]
                i += 1

        print('Scrape results from SkyBet:')
        print(scrape_results)
        print('Scraping From SkyBet ended.')
        driver.quit()

        return scrape_results