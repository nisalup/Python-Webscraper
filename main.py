from Bet365 import Bet365
from WilliamHill import WilliamHill
from selenium import webdriver
from PaddyPower import PaddyPower
from SkyBet import SkyBet
import numpy as np
import pandas as pd



class CoolScrawler:
    def main():
        A = np.zeros((6, 6))

        fbot = Bet365()
        result_PaddyPower = fbot.scrapeBet365()

        fbot1 = WilliamHill()
        result_PaddyPower = fbot1.scrapeWilliamHill()

        fbot2 = PaddyPower()
        result_PaddyPower = fbot2.scrapePaddyPower()

        fbot3 = SkyBet()
        result_SkyBet = fbot3.scrapeSkyBet()


        names = [_ for _ in 'abcdef']
        df = pd.DataFrame(A, indx=names, columns=names)

    if __name__ == "__main__":
        main()




