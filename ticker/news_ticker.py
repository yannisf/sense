#!/usr/bin/env python3

import requests
import lxml.etree as ET
from sense_hat import SenseHat

guardian = ("https://www.theguardian.com/us/rss", "//item[category/text()='World news']/title/text()", [255,229,0], [5,41,98])
bbc = ("http://feeds.bbci.co.uk/news/business/rss.xml", "//item/title/text()", [255,255,255], [187,25,25])
kathimerini = ("https://www.ekathimerini.com/rss", "//item/title/text()", [0,0,0], [255,255,255])

sources = [guardian, bbc, kathimerini]

def news(tuple):
    content = requests.get(tuple[0]).content
    root = ET.fromstring(content)
    news_list = root.xpath(tuple[1])
    news = '     '.join(news_list[0:9])
    return news



sense = SenseHat()
sense.clear()
sense.set_rotation(180)
scroll_speed = 0.02

for s in sources:
    ticker = news(s)
    sense.show_message(ticker, scroll_speed=scroll_speed, text_colour=s[2], back_colour=s[3])

sense.clear()

