from selenium import webdriver

class Bet365:



    def scrapeBet365(self):
        odds_decoded=[]
        countries_decoded=[]

        myProxy = "178.79.188.251:80"

        proxy = webdriver.common.proxy.Proxy({
            'proxyType': webdriver.common.proxy.ProxyType.MANUAL,
            'httpProxy': myProxy,
            'ftpProxy': myProxy,
            'sslProxy': myProxy
        })

        driver = webdriver.Firefox(proxy=proxy)
        driver.implicitly_wait(6)
        driver.get('https://mobile.bet365.com/#type=Coupon;key=1-172-1-26326924-2-4-0-0-1-0-0-4063-0-0-1-0-0-0-0-0-75-0-0;ip=0;lng=1;anim=1')
        odds = driver.find_elements_by_xpath("//*[contains(@class,'podEventRow')]//*[@class='odds']")
        countries = driver.find_elements_by_xpath("//*[contains(@class,'podEventRow')]//*[@class='opp']")
        for odd in odds:
            data = odd.text
            print(data)
            odds_decoded.append(data)

        for country in countries:
            data = country.text
            data = data[:-5]
            countries_decoded.append(data)

        print(odds_decoded)
        print(countries_decoded)