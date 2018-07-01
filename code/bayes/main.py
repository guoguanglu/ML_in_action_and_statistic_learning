#encoding=utf-8
import bayes
from numpy import *
#bayes.testingNB()
#bayes.spamTest()
import feedparser
ny = feedparser.parse('http://newyork.craigslist.org/stp/index.rss')
sf = feedparser.parse('http://sfbay.craigslist.org/stp/index.rss')
bayes.getTopWords(ny, sf)
