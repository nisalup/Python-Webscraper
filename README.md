# Python-Webscraper
Python Webscraping code for different kinds of websites including country restricted, javascript enabled sites.
> This is a dynamic webscraper that crawls data from 4 different websites. One of them is a regualar website , another a dynamic website, another a website with country restrictions and one with anti bot html in the code.
> I just made this as requirement of an interview assignment and this may not be fully developed yet, but I do intened to add to this in the future.
> This is just a test program, always respect robots texts. And, my xpaths could stop working any moment. I am trying to figure a way to improve on that.

## Running the script
- Uses Python 3.6
- You will need selenium webdriver (install using pip)
- Before running the script, edit the config.ini file and add a proxy ip and port. You can get one here: https://free-proxy-list.net/uk-proxy.html, if the connection is slow, increase the wait time.
- And of course, mozilla installed in your PC

## What it does
> This is just information for the evaluation. This information, and the xpaths will of course change soon. 
- There are 4 websites in the scripts that are scrawled.
  ### WilliamHill
  This is a website that can be scraped without using selenium, by using requests in python. Straightforward.
  
  ### PaddyPower
  This website uses country restrictions. The actual scrape was quite easy, but I needed to have firefox configured to use a seperate profile along with a proxy. And I think they also track the original IP of the request, as I keep getting blocked after some time.
  
  ### SkyBet
  This is a javascript enabled website, which connects fine with the default selenium webdriver. However for the scraping, it had to been done using longer xpath as there were no identifiables classes or ids.
  
  ### Bet365
  For this website, I used a firefox driver with proxy enabled. 
  
 ## What I am working on
 Trying to access all these websites just by using the homepage and then navigating my way to where I want to go. Some implementation is done on skybet, but not from the homepage.
