#!/usr/bin/env python
import sys, re

valid_date = re.compile('^(19|20)[0-9][0-9](0[1-9]|1[012])(0[1-9]|[12][0-9]|3[01])$')

from_date = sys.argv[1]
to_date   = sys.argv[2]

if (not valid_date.search(from_date)) or (not valid_date.search(to_date)) or (int(to_date) - int(from_date))<0:
    print "invalid parameter, input as \'command\' yyyymmdd (<) yyyymmdd."
    sys.exit(1)

print "<h1>Generate cjmp.cnhan.com link from " + from_date + " to " + to_date + "</h1><br/>"

days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
yyyy = int(from_date[:4])
while yyyy <= int(to_date[:4]):
    for mm in range(12):
        days = days_in_month[mm]
        mm += 1
        for dd in range(days):
            dd += 1
            date = '%04d%02d%02d' % (yyyy, mm, dd)
            if int(date) >= int(from_date) and int(date) <= int(to_date):
                # need 'YYYY-MM/DD'
                date_link = '%04d-%02d/%02d' % (yyyy, mm, dd)
                print "<a href=\"http://cjmp.cnhan.com/whwb/html/" + date_link + "/node_22.htm\">" + date + "</a>"
    yyyy += 1
