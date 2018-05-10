from Bet365 import Bet365
from WilliamHill import WilliamHill
from selenium import webdriver

fbot = Bet365()
fbot.scrapeBet365()

fbot1 = WilliamHill()
fbot1.scrapeWilliamHill()



