from posixpath import split
from unicodedata import decimal
import requests
from bs4 import BeautifulSoup as bs
import itemNameFormatter
from decimal import *

def steamMarketScraping(item_link):
    name_list=[]
    name_list=itemNameFormatter.nameFormatForSteamMarket(item_link)
    item_name = itemNameFormatter.nameFormatItemMarket(item_link)
    steam_market_url = f"https://steamcommunity.com/market/search?appid=570&q={name_list[0]}"
    steam_item_market_url =f"https://steamcommunity.com/market/listings/570/{item_name}"
    response = requests.get(steam_market_url)
    soup = bs(response.text,"lxml")
    item_quantity = soup.find("span",{"class":"market_listing_num_listings_qty"}).text.strip()
    item_prices = soup.find("span",{"class":"normal_price"}).text.strip()
    splitLine = item_prices.splitlines()
    price_before_steam_tax = splitLine[1]
    price_after_steam_tax = splitLine[2]
    info_list=[item_quantity,price_after_steam_tax,price_before_steam_tax,steam_item_market_url,name_list[1]]
    return info_list

def dotaWikiScraping(item_link):
    dota_wiki_url = f"https://dota2.fandom.com/wiki/{itemNameFormatter.nameFormatForDotaWiki(item_link)}"
    response = requests.get(dota_wiki_url)
    soup = bs(response.text,"lxml")
    general_info = soup.find("td",{"style":"display:flex; align-items:center; text-align:left;"}).text
    splitLine = general_info.split(":")
    hero_name = splitLine[0].replace("Rarity","").strip()
    item_rarity = splitLine[1].replace("Slot","").strip()
    item_slot = splitLine[2].replace(r"\n","").strip()
    info_list=[hero_name,item_slot,item_rarity,dota_wiki_url]
    return info_list

def steamxCutCalculator(price_after_tax="0.0",price_before_tax="0.0"):
    a=float(price_after_tax.replace("$","").replace("USD","").strip())
    b=float(price_before_tax.replace("$","").replace("USD","").strip())
    getcontext().prec = len(price_after_tax)-8
    steams_cut = Decimal(a)-Decimal(b)
    return(f"${steams_cut} USD")

def itemInfo(user_input):
    wiki_data=[]
    steam_data=[]
    all_data=[]
    wiki_data=dotaWikiScraping(user_input)
    steam_data=steamMarketScraping(user_input)
    all_data=wiki_data+steam_data
    return all_data