#!/usr/bin/env python
import re
import sys
import time
import urllib2
from lxml import html

valid_date = re.compile('^[0-9]+$')

if len(sys.argv) < 3:
    print "input as \'command\' [from page] (<) [to page]."
    print "page will be grabbed from http://www.cankaoxiaoxi.com/roll"
    exit(1)

from_page = sys.argv[1]
to_page   = sys.argv[2]

if (not valid_date.search(from_page)) or (not valid_date.search(to_page)) or (int(to_page) - int(from_page))<0:
    print "invalid parameter."
    exit(1)

print "<h1>Grabbed www.cankaoxiaoxi.com link from page %s to %s. </h1><br/>" % (from_page, to_page)
# 2012/12/1: http://www.cankaoxiaoxi.com/roll/?page=1 ~ http://www.cankaoxiaoxi.com/roll/?page=3461
for page in range(int(from_page), int(to_page) + 1):
    page_url = "http://www.cankaoxiaoxi.com/roll/?page=" + str(page)
    print "<h2>read from %s </h2><br/>" % page_url
    content = urllib2.urlopen(page_url).read()

    try:
        content_dom = html.fromstring(content)
        for report_url in content_dom.xpath("id('tab-cont-1')/div[1]/ul/li/a/attribute::href"):
            print "<a href=\"%s\">report</a><br/>" % report_url
    except Exception, e:
        raise e

    time.sleep(2)
