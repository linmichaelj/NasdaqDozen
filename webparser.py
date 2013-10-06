__author__ = 'linmichaelj'

import urllib2
import helper
from bs4 import BeautifulSoup
from selenium import webdriver
#requires html5lib

def get_soup(url, selenium):
    if selenium:
        driver = webdriver.Firefox()
        driver.get(url)
        data = driver.page_source

    else:
        usock = urllib2.urlopen(url)
        data = usock.read()
        usock.close()

    return BeautifulSoup(data, "html5lib")


def recommendation_test(symbol):
    soup = get_soup("http://ca.finance.yahoo.com/q/ao?s=" + symbol, False)
    data_tables = soup.findAll("table", {"class": "yfnc_datamodoutline1"})

    recommendations = {}

    #Look at Recommendation Trends Table
    for row in data_tables[3].find("tr").findAll("tr"):
        recommendation = row.find("th", {"align": "left"})
        if recommendation is not None:
            recommendation = recommendation.getText()
            num = row.find("td", {"class": "yfnc_tabledata1"}).getText()

            #add to database, str is used to convert from unicode to string
            recommendations[str(recommendation)] = int(str(num))

    test_result = (recommendations["Strong Buy"] + recommendations["Buy"]) > \
                            (recommendations["Hold"] + recommendations["Underperform"] + recommendations["Sell"])

    return test_result, {"recommendations": recommendations}


def earning_surprise_test(symbol):
    soup = get_soup("http://www.nasdaq.com/symbol/" + symbol + "/earnings-surprise", False)

    surprises = {}

    surprise_table = soup.find("table", {"class": "earningsurprise"})
    for row in surprise_table.findAll("tr"):

        cols = row.findAll("td")
        if len(cols) == 5:
            quarter = str(cols[0].getText())
            surprise = str(cols[4].getText())

            if quarter != "FiscalQuarter End":
                surprises[quarter] = float(surprise)

    test_result = True
    for quart in surprises.keys():
        if surprises[quart] < 0:
            test_result = False

    return test_result, {"EPS Surprise Percentages": surprises}


def eps_forecast_test(symbol):
    soup = get_soup("http://www.nasdaq.com/symbol/" + symbol + "/earnings-forecast", False)

    forecasts_dict = {}
    forecasts_list = []

    forecast_table = soup.find("table", {"class": "earningsurprise"})
    rows = forecast_table.findAll("tr")
    for i in range(1, len(rows)):
        cols = rows[i].findAll("td")
        year = cols[0].getText()
        year = year[len(year)-4:]
        forecast = cols[1].getText()
        forecasts_dict[str(year)] = float(str(forecast))
        forecasts_list.append(float(str(forecast)))

    test_result = False
    if helper.get_years_increasing(forecasts_list) == len(forecasts_list):
        test_result = True

    return test_result, {"EPS_forecast": forecasts_dict}


def industry_test(symbol, pe):
    soup = get_soup("http://finance.yahoo.com/q/in?s=" + symbol + "+Industry", False)

    industry_table = soup.find("table", {"class": "yfnc_datamodoutline1"})
    industry_url = industry_table.findAll('a', href=True)[1].get('href')

    soup = get_soup(industry_url, False)
    stat_table = soup.findAll("table", {"bgcolor":"dcdcdc"})[-1]
    industry_pe = float(str(stat_table.findAll("td", {"bgcolor": "ffffff"})[1].getText()))

    pe_ratios = {
        'industry_pe': float(str(industry_pe)),
        symbol+'_pe': float(str(pe))
    }
    return pe > industry_pe, pe_ratios


def industry_and_alpha_test(symbol):
    soup = get_soup("http://www.barchart.com/quotes/stocks/" + symbol, True)

    alpha = soup.findAll("td", {"class":"qval_shad"})[6].getText()
    pe = soup.findAll("td", {"class": "qval_line"})[2].getText()

    #clean output
    alpha = float(str(alpha).replace("\t", ""))
    pe = float(str(pe).replace("\t", "").replace(",", ""))

    test_results = {
        'alpha_test': (alpha > 0, alpha),
        'industry_test': industry_test(symbol, pe)
    }
    return test_results


def insider_trading_test(symbol):
    soup = get_soup("http://www.nasdaq.com/symbol/" + symbol + "/insider-trades", False)
    net_row = soup.findAll("tr", {"class": "genTablealt"})[1]
    net_trading = str(net_row.find("td", {"class": "right-align"}).getText())
    return net_trading[0] != '(', net_trading


def days_to_cover_test(symbol):
    soup = get_soup("http://www.nasdaq.com/symbol/" + symbol + "/short-interest", False)
    cover_table = soup.find("table", {"class": "dataGrid"})
    day_row = cover_table.find("tr", {"class": "oddgr"})
    days_to_cover = float(str(day_row.findAll("td")[3].getText()))

    return days_to_cover < 2, {"days_to_cover": days_to_cover}


def earnings_growth_test(symbol):
    soup = get_soup("http://finance.yahoo.com/q/ae?s="+symbol, False)
    growth_table = soup.findAll("table", {"cellpadding":2})[-1]
    row = growth_table.findAll("tr")[6]
    earnings_growth = float(str(row.findAll("td")[1].getText()).replace("%",""))

    return earnings_growth>8, {"5_year_growth_est":str(earnings_growth)+"%"}