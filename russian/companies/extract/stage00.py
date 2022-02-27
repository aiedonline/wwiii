#!/usr/local/python3
import sys, os, time;

from cachetools import Cache;
sys.path.insert(0, os.path.abspath("./"));

from api.cacherequest import *;
from api.data import *;

URL_LIST = "https://en.wikipedia.org/wiki/List_of_companies_of_Russia";
XPATH_COMPANIES = "//tr/td[2]/a[1 and contains(@href, 'wiki')]/@href";
XPATH_LINK_EXT = '//tr[ th[  text() = "Website"  ]]/td[1]/span/a/@href';

def get_links_wiki():
    c = CacheRequest(life=600);
    c.get(URL_LIST);
    return c.elements(XPATH_COMPANIES);

def get_link(url):
    c = CacheRequest(life=600);
    c.get("https://en.wikipedia.org" + url);
    return c.elements(XPATH_LINK_EXT);
    #    

if __name__ == "__main__":
    links = [];
    links_wiki = get_links_wiki();
    count = 0;
    for link_wiki in links_wiki:
        count = count + 1;
        links += get_link(link_wiki);
        time.sleep(5);
    js = JsonHelp();
    js.store(os.path.abspath("./") + "/data/stage00.json", links);
