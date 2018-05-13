from Bet365 import Bet365
from WilliamHill import WilliamHill
from PaddyPower import PaddyPower
from SkyBet import SkyBet
from Utilities import Utilities
import time
import datetime
from multiprocessing.pool import ThreadPool


class CoolScrawler:
    def __init__(self):
        print('======================')
        print('Cool Crawler Started')
        print('======================')

    def scrape(self):
        print('================================================')
        print('Started Crawl at ' + str(datetime.datetime.now()))
        print('================================================')

        fbot = Bet365()
        # result_Bet365 = fbot.scrapeBet365()

        fbot1 = WilliamHill()
        # result_WilliamHill = fbot1.scrapeWilliamHill()

        fbot2 = PaddyPower()
        # result_PaddyPower = fbot2.scrapePaddyPower()

        fbot3 = SkyBet()
        # result_SkyBet = fbot3.scrapeSkyBet()

        pool = ThreadPool(processes=4)
        thread1 = pool.apply_async(fbot.scrapeBet365, ())
        thread2 = pool.apply_async(fbot1.scrapeWilliamHill, ())
        thread3 = pool.apply_async(fbot2.scrapePaddyPower, ())
        thread4 = pool.apply_async(fbot3.scrapeSkyBet, ())

        result_Bet365 = thread1.get()
        result_WilliamHill = thread2.get()
        result_PaddyPower = thread3.get()
        result_SkyBet = thread4.get()


        result_dict = {'WilliamHill':result_WilliamHill, 'Bet365':result_Bet365, 'SkyBet':result_SkyBet, 'PaddyPower':result_PaddyPower}
        result_matrix = Utilities.createResultArray(result_dict)

        print('============')
        print('Final Result')
        print('============')
        print(result_matrix)
        saved_file_name = time.strftime("%Y%m%d-%H%M%S") + '_results'
        result_matrix.to_csv(Utilities.getResultsPath() + saved_file_name +'.csv', index=True, header=True, sep=';')

    def start(self):
        starttime = time.time()
        while True:
            self.scrape()
            time.sleep(300.0 - ((time.time() - starttime) % 300.0))


c = CoolScrawler()
c.start()


