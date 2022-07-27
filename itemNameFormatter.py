import re

#The Commodore's Facings  Belt of the Engulfing Spike
def nameFormatForSteamMarket(item_name):
    item_name =item_name.title()
    if(re.search(r"\b\S\b",item_name)):
        item_name = item_name.replace("'S","'s")
    if(re.search(r"\bThe\b",item_name)):
        item_name = item_name.replace("The","the")
    if(re.search(r"\bOf\b",item_name)):
        item_name = item_name.replace("Of","of")
    if(item_name.startswith("the")):
        item_name=item_name.replace("the","").strip()
    og_item_name = item_name
    item_name = item_name.replace(" ","+")
    item_name = item_name.replace("'","%27")
    info_list=[item_name,og_item_name]
    return info_list

def nameFormatForDotaWiki(item_name):
    item_name =item_name.title()
    if(re.search(r"\b\S\b",item_name)):
        item_name = item_name.replace("'S","'s")
    if(re.search(r"\bThe\b",item_name)):
        item_name = item_name.replace("The","the")
    if(re.search(r"\bOf\b",item_name)):
        item_name = item_name.replace("Of","of")
    if(item_name.startswith("the")):
        item_name=item_name.replace("the","").strip()
    item_name = item_name.replace(" ","_")
    item_name = item_name.replace("'","%27")
    return item_name

def nameFormatItemMarket(item_name):
    item_name =item_name.title()
    if(re.search(r"\b\S\b",item_name)):
        item_name = item_name.replace("'S","'s")
    if(re.search(r"\bThe\b",item_name)):
        item_name = item_name.replace("The","the")
    if(re.search(r"\bOf\b",item_name)):
        item_name = item_name.replace("Of","of")
    if(item_name.startswith("the")):
        item_name=item_name.replace("the","").strip()
    item_name = item_name.replace(" ","%20")
    item_name = item_name.replace("'","%27")
    return item_name