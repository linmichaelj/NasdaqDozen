__author__ = 'linmichaelj'

import Quandl
import helper


def revenue_test(symbol):
    rev_data_frame = Quandl.get('OFDP/DMDRN_' + symbol + '_REV_LAST')
    rev_series = rev_data_frame['Revenues']

    years_increasing = helper.get_years_increasing(rev_series)
    return years_increasing > 2, {"historical_revenue": rev_series}


def eps_test(symbol):
    rev_data_frame = Quandl.get('OFDP/DMDRN_' + symbol + '_EPS_GRO')
    rev_series = rev_data_frame['Growth in Earnings Per Share']

    years_increasing = helper.get_years_greater_than(rev_series, 0)
    return years_increasing > 5, {"historical_epss": rev_series}


def roe_test(symbol):
    rev_data_frame = Quandl.get('OFDP/DMDRN_' + symbol + '_ROE')
    rev_series = rev_data_frame['Return on Equity']

    years_increasing = helper.get_years_increasing(rev_series)
    return years_increasing > 5, {"historical_ROE": rev_series}


def peg_test(symbol):
    rev_data_frame = Quandl.get('OFDP/DMDRN_' + symbol + '_PE_G')
    rev_series = rev_data_frame['PE to Growth Ratio']

    years = helper.get_years_greater_than(rev_series, 1)
    return rev_series[-1] > 1, {"peg_ratio": rev_series[-1]}
