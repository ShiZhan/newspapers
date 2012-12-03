# Introduction

newspaper data collector

A web crawler for collecting online newspaper data and stores into document database.

Crawler based on [scrapy](https://github.com/scrapy/scrapy) framework.

Task control by creating local index page.

Databases/WIP using [mongodb](http://www.mongodb.org/).

# Spiders

## hbrb

[Hubei Daily](http://hbrb.cnhubei.com/)

1. use <code>generate-index-hbrb.py [from date: yyyymmdd] [to date]</code> to generate index page between specified dates.

2. use <code>python -m SimpleHTTPServer 9080 &</code> to make the index page visible to spider.

3. run <code>scrapy crawl whrb</code> , add parameters, e.g.: "-t json -o foo.json" to collect data.

## whwb

[Wuhan nightly](http://cjmp.cnhan.com/whwb)

Exactly the same with hbrb.

## ckxx

[Can Kao Xiao Xi](http://www.cankaoxiaoxi.com/)

1. use <code>generate-index-ckxx.py [from page] [to page]</code> to grab individual report URLs from [headline pages](http://www.cankaoxiaoxi.com/roll/).

2. same as hbrb and whwb.

3. same as hbrb and whwb.

# Utilities

* escaped-unicode-print.py

  Print collected text (escaped unicode), for checking purpose.

* import-to-mongodb.py [collection] [json file]

  Import json into mongodb "newspaper" database and specified collection.

* json-to-item-in-line.py [json file]

  Convert gathered json to one-line mode, actually the most current scrapy defaults to that.

* run-server

  Simplify the calling of python internal web server <code>python -m SimpleHTTPServer</code> .

