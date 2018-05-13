from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from Utilities import Utilities
from Website import Website

class PaddyPower:

    def scrapePaddyPower(self):
        print('Scraping From PaddyPower started.')
        scrape_results = {}
        driver = Utilities.getWebDriverWithoutProfile()
        try:
            driver.get('https://www.paddypower.com/football?tab=world-cup-2018')
            privacy_element = WebDriverWait(driver, int(Utilities.getWebDriverDefaultWait())).until(EC.presence_of_element_located((By.CLASS_NAME, 'ssc-privacyPolicyBannerButton')))
            load_more_element = WebDriverWait(driver, int(Utilities.getWebDriverDefaultWait())).until(EC.presence_of_element_located((By.CLASS_NAME, 'outright-item-grid-list__show-more')))
            driver.implicitly_wait(5)
            privacy_element.click()
            driver.implicitly_wait(8)
            load_more_element.click()
            driver.implicitly_wait(2)
            odds = driver.find_elements_by_xpath("//div[contains(@class, 'card-container') and contains(.//div, 'World Cup Outrights')]//div[contains(@class, 'grid outright-item')]//button[contains(@class, 'btn-odds')]")
            countries = driver.find_elements_by_xpath("//div[contains(@class, 'card-container') and contains(.//div, 'World Cup Outrights')]//div[contains(@class, 'grid outright-item')]//p[contains(@class, 'outright-item__runner-name')]")
            scrape_results = Utilities.processResultData(odds, countries, Website.PADDYPOWER)

        except NoSuchElementException as ex:
            print('Exception at PaddyPower.py')
            print('The element could not be located or the xpath has changed.')
            print('If this is not the case, try increasing the timeout to allow more time for the website to load.')
            print('Error Message:')
            print(ex)
        except TimeoutException as ex:
            print('Exception at PaddyPower.py')
            print('The connection has been lost. Proxy addresses change regularly, so try with a new address')
            print('Error Message:')
            print(ex)
        except Exception as ex:
            print('Exception at PaddyPower.py')
            print('Unchecked Error Occured')
            print(ex)


        print('Scrape results from PaddyPower:')
        print(scrape_results)
        print('Scraping From PaddyPower ended.')
        driver.quit()

        return scrape_results