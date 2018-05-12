from Bet365 import Bet365
from WilliamHill import WilliamHill
from selenium import webdriver
from PaddyPower import PaddyPower
from SkyBet import SkyBet
from Utilities import Utilities
import numpy as np
import pandas as pd
import time
import datetime


class CoolScrawler:
    def main():
        print('================================================')
        print('Started Crawl at ' + str(datetime.datetime.now()))
        print('================================================')

        fbot = Bet365()
        result_Bet365 = fbot.scrapeBet365()

        fbot1 = WilliamHill()
        result_WilliamHill = fbot1.scrapeWilliamHill()

        fbot2 = PaddyPower()
        result_PaddyPower = fbot2.scrapePaddyPower()

        fbot3 = SkyBet()
        result_SkyBet = fbot3.scrapeSkyBet()

        result_dict = {'WilliamHill':result_WilliamHill, 'Bet365':result_Bet365, 'SkyBet':result_SkyBet, 'PaddyPower':result_PaddyPower}
        result_matrix = Utilities.createResultArray(result_dict)

        print('============')
        print('Final Result')
        print('============')
        print(result_matrix)
        saved_file_name = time.strftime("%Y%m%d-%H%M%S") + '_results'
        print(saved_file_name)
        result_matrix.to_csv(Utilities.getResultsPath() + saved_file_name +'.csv', index=True, header=True, sep=' ')




    if __name__ == "__main__":
        main()




