__author__ = 'linmichaelj'

import webparser
import quandl
import sys
import pprint


def main():
    if len(sys.argv) < 2:
        sys.exit(0)

    symbol = sys.argv[1]

    test_results = {
        "revenue_test": quandl.revenue_test(symbol),
        "eps_test": quandl.eps_test(symbol),
        "roe_test": quandl.roe_test(symbol),
        "recommendation_test": webparser.recommendation_test(symbol),
        "surprise_test": webparser.earning_surprise_test(symbol),
        "forecast_test": webparser.eps_forecast_test(symbol),
        "earnings_growth_test": webparser.earnings_growth_test(symbol),
        "peg_test": quandl.peg_test(symbol),
        "cover_test": webparser.days_to_cover_test(symbol),
        "insider_test": webparser.insider_trading_test(symbol)
    }

    industry_and_alpha_tests = webparser.industry_and_alpha_test(symbol)
    test_results["industry_test"] = industry_and_alpha_tests["industry_test"]
    test_results["alpha_test"] = industry_and_alpha_tests["alpha_test"]

    if len(sys.argv) > 2 and sys.argv[2] == '-v':
        pprint.pprint(test_results)

    print '------------------------------------------------------'
    print 'Summary'

    count = 0
    for key in test_results.keys():
        if test_results[key][0]:
            print key + ": " + "Pass"
            count += 1
        else:
            print key + ": " + "Fail"
    print "Total Passed: " + str(count)



if __name__ == "__main__":
    main()