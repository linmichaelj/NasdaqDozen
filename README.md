Description: 
===========
The **NASDAQ DOZEN" evaluates a stock against the Nasdaq Dozen: http://www.nasdaq.com/investing/dozen/

Getting Started:
==============
To get started I would recommend that you become familar with the dependencies of this project.  The most important thing to take away from this sample code is how to use these dependencies to retreive financial data.  For sample usage of each dependency please look through the project's source.  

Python
-------
This project and the tools we will explore will require Python 2.7.  You can download python here: http://www.python.org/getit/

This is a good resource for learning about python's built in libraries: http://docs.python.org/2/library/
You can use the python interpreter directly or you can use the Pycharm IDE found here: http://www.jetbrains.com/pycharm/

Quandl
------
Quandl is a fantastic api for querying financial data.  

The requirements for this dependency is numpy and pandas which can be downloaded here: http://www.numpy.org/ and here http://pandas.pydata.org/
These depedencies are the math libraries necessary to process the data

Quandl itself can be downloaded by following the install instructions listed here: https://github.com/quandl/Python 
Quandl API documentation can be found here: http://www.quandl.com/help/packages/python
And Stock Related API calls can be found here: http://www.quandl.com/help/api-for-stock-data

BeautifulSoup
--------------
BeautifulSoup is the parser that can be used to scrape data from websites.  BeautifulSoup4 can be downloaded here: http://www.crummy.com/software/BeautifulSoup/bs4/doc/ this site also has great documentation.

html5lib packages
--------------
The html5lib parser is required by BeautifulSoup (See line 20 in webparser.py).  html5lib can be downloaded here: https://pypi.python.org/pypi/html5lib

Selenium Web Driver
-------------------
When urllib2 cannot be used to scrape the data properly due to javascript in the html page, Selenium can be used to have the browser render and fetch the html.  Selenium can be downloaded here: https://pypi.python.org/pypi/selenium

We only use a small portion of Selenium's huge feature set.  It is complex and full understanding is not required to get the full benefit of this project.  However if you are interested documentation can be found here: http://selenium-python.readthedocs.org/en/latest/

Firefox
----------
This is the browser used by the Selenium Web Driver (See line 11 in webparser.py). Firefox can be downloaded from here: http://www.mozilla.org/en-US/firefox/new/



Running the Project
===================
After installing the dependencies detailed in theGetting Started section you can run the project through the following commands:
python nasdaqdozen.py [STOCK_SYMBOL]  --> will output the results of each test and a final score
python nasdaqdozen.py [STOCK_SYMBOL] -v   --> will output the results of each test as well as the data fetched to draw that conclusion

On windows this should be run from the cmd and in linux/Mac it should be run from the command line.  Make sure that you are in the correct directory! 
Note that in windows python may need to be added to the environment variable PATH
