#The purpose of this prgoram is to create a web scrapper that
#will eventually act as a ticker for the stock discord channel
# "Price Going Up? (On a Tuesday)"

import unittest
import pandas as pd
import selenium
import array as arr
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv


# Fucntion to hold website 
def return_Website():
    return "https://finviz.com"

#Function to open browser to webpage
def setUp():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(return_Website())
    print(driver.title)
    return driver

#Function to search stocks
def searchStocks(stock_name):
    search = browser.find_element_by_xpath("/html/body/table[1]/tbody/tr[1]/td/table/tbody/tr/td[1]/table/tbody/tr[2]/td/div/form/input")
    search.send_keys(stock_name)
    search.send_keys(Keys.RETURN)
    print("\n")
    print("What would you like to see about " + stock_name + "?")
    print("1. The whole table")
    print("2. Your preferred list")
    response = input("Please select one of the two options: ")
    if response == "1":
        table = browser.find_element_by_class_name("snapshot-table2")
        print()        
        print(table.text)
        return response
    if response == "2":
        return response
        
#Function to get list of stocks
def inquiryList():
    #Creates an empty list
    list = []
    #Number of elements as input
    n = int(input("Enter the numbe of stocks you would like to review: "))
    #Iterating till the range
    for i in range(0, n):
        stock = input("Enter the ticker symbol or company name: ")
        list.append(stock)
    print(list)
    return n, list

# The following functions hold 
# Data table informatioono 
def column_1_val():
    index = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[1]/td[2]")
    market_cap = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[2]/td[2]/b")
    income = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[3]/td[2]/b")
    sales = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[4]/td[2]/b")
    book_sh = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[5]/td[2]/b")
    cash_sh = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[6]/td[2]/b") 
    dividend = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[7]/td[2]/b")
    dividend_percent = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[8]/td[2]/b")
    employees = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[9]/td[2]/b")
    optionable = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[10]/td[2]/b")
    shortfall = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[11]/td[2]/b")
    recom = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[12]/td[2]/b")
    colum_1_info = [index.text, market_cap.text, income.text, sales.text, book_sh.text, cash_sh.text, dividend.text,
    dividend_percent.text, employees.text, optionable.text, shortfall.text, recom.text]
    return colum_1_info

def column_1_str():
    index_string = "Index: "
    market_cap_string = "Market Cap: "
    income_string = "Income: "
    sales_string = "Sales: "
    book_sh_string = "Book/sh: "
    cash_sh_string = " Cash/sh: "
    dividend_string = " Dividend: "
    dividend_percent_string = " Dividend %: "
    employees_string = " Employees: "
    optionable_string = " Optionable: "
    shortfall_string = " Shortfall: "
    recom_string = " Recom: "
    colum_1_string = [index_string, market_cap_string, income_string, sales_string, book_sh_string, cash_sh_string, dividend_string,
    dividend_percent_string, employees_string, optionable_string, shortfall_string, recom_string]
    return colum_1_string

def column_2_val():
    p_e = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[1]/td[4]/b")
    forward_p_e = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[2]/td[4]/b")
    peg = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[3]/td[4]/b")
    p_s = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[4]/td[4]/b")
    p_b = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[5]/td[4]/b")
    p_c = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[6]/td[4]/b")
    p_fcf = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[7]/td[4]/b")
    quick_ratio = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[8]/td[4]/b")
    current_ratio = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[9]/td[4]/b")
    debt_eq = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[10]/td[4]/b/span")
    lt_debt_eq = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[11]/td[4]/b/span")
    sma_20 = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[12]/td[4]/b/span")
    column_2_info = [p_e.text, forward_p_e.text, peg.text, p_s.text, p_b.text, p_c.text, p_fcf.text, 
    quick_ratio.text, current_ratio.text, debt_eq.text, lt_debt_eq.text, sma_20.text]
    return column_2_info

def column_2_str():
    p_e_string = "P/E: "
    forward_p_e_string = "Forward P/E: "
    peg_string = "PEG: "
    p_s_string = "P/S: "
    p_b_string = "P/B: "
    p_c_string = "P/C: "
    p_fcf_string = "P/FCF: "
    quick_ratio_string = "Quick Ratio: "
    current_ratio_string = "Current Ratio: "
    debt_eq_string = "Debt/Eq: "
    lt_debt_eq_string = "LT Debt/Eq: "
    sma_20_string = "SMA20: "
    column_2_string = [p_e_string, forward_p_e_string, peg_string, p_s_string, p_b_string, p_c_string,
    p_fcf_string, quick_ratio_string, current_ratio_string, debt_eq_string, lt_debt_eq_string, sma_20_string]
    return column_2_string

def column_3_val():
    eps_ttm = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[12]/td[4]/b/span")
    eps_next_y = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[2]/td[6]/b")
    eps_next_q = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[3]/td[6]/b")
    eps_this_y = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[2]/td[6]/b")
    eps_next_y_percent = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[5]/td[6]/b")
    eps_next_5y = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[6]/td[6]/b")
    eps_past_5y = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[7]/td[6]/b")
    sales_past_5y = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[8]/td[6]/b")
    sales_q_q = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[9]/td[6]/b/span")
    eps_q_q = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[10]/td[6]/b/span")
    earnings = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[11]/td[6]/b")
    sma_50 = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[12]/td[6]/b")
    column_3_info = [eps_ttm.text, eps_next_y.text, eps_next_q.text, eps_this_y.text, eps_next_y_percent.text,
    eps_next_5y.text, eps_past_5y.text, sales_past_5y.text, sales_q_q.text, eps_q_q.text, earnings.text, sma_50.text]
    return column_3_info

def column_3_str():
    eps_ttm_string = "EPS (ttm): "
    eps_next_y_string = "EPS next Y: "
    eps_next_q_string = "EPS Next Q: "
    eps_this_y_string = "EPS This Y: "
    eps_next_y_percent_string = "EPS Next Year: "
    eps_next_5y_string = "EPS Next 5Y: "
    eps_past_5y_string = "EPS Past 5Y: "
    sales_past_5y_string = "Sales past 5Y: "
    sales_q_q_string = "Sales Q/Q: "
    eps_q_q_string = "EPS Q/Q: "
    earnings_string = "Earnings: "
    sma_50_string = "SMA50: "
    column_3_string = [eps_ttm_string, eps_next_y_string, eps_next_q_string, eps_this_y_string, eps_next_y_percent_string,
    eps_next_5y_string, eps_past_5y_string, sales_past_5y_string, sales_q_q_string, eps_q_q_string, earnings_string, sma_50_string]
    return column_3_string

def column_4_val():
    insider_own = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[1]/td[8]/b")
    insider_trans = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[2]/td[8]/b")
    inst_own = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[3]/td[8]/b")
    inst_trans = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[4]/td[8]/b")
    roa = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[5]/td[8]/b")
    roe = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[6]/td[8]/b")
    roi = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[7]/td[8]/b")
    gross_margin = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[8]/td[8]/b")
    open_margin = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[9]/td[8]/b")
    profit_margin = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[10]/td[8]/b")
    payout = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[11]/td[8]/b")
    sma_200 = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[12]/td[8]/b/span")
    column_4_info = [insider_own.text, insider_trans.text, inst_own.text, inst_trans.text, roa.text,
    roe.text, roi.text, gross_margin.text, open_margin.text, profit_margin.text, payout.text, sma_200.text]
    return column_4_info

def column_4_str():
    insider_own_string = "Insider Own: "
    insider_trans_string = "Insider Trans: "
    inst_own_string = "Inst Own: "
    inst_trans_string = "Inst Trans: "
    roa_string = "ROA: "
    roe_string = "ROE: "
    roi_string = "ROI: "
    gross_margin_string = "Gross Margin: "
    open_margin_string = "Open Margin: "
    profit_margin_string = "Profit Margin: "
    payout_string = "Payout: "
    sma_200_string = "SMA200: "
    column_4_string = [insider_own_string, insider_trans_string, inst_own_string, inst_trans_string, roa_string,
    roe_string, roi_string, gross_margin_string, open_margin_string, profit_margin_string, payout_string, sma_200_string]
    return column_4_string

    
def column_5_val():
    shs_outstand = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[1]/td[10]/b")
    shs_float = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[2]/td[10]/b")
    short_float = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[3]/td[10]/b")
    short_ratio = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[4]/td[10]/b")
    target_price = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[5]/td[10]/b/span")
    fifty_two_week_range = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[6]/td[10]/b/small")
    fifty_two_week_high = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[7]/td[10]/b/span")
    fifty_two_week_low = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[8]/td[10]/b/span")
    rsi_fourteen = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[9]/td[10]/b")
    rel_volume = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[10]/td[10]/b")
    avg_volume = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[11]/td[10]/b")
    the_volume = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[12]/td[10]/b")
    column_5_info = [shs_outstand.text, shs_float.text, short_float.text, short_ratio.text, target_price.text,
    fifty_two_week_range.text, fifty_two_week_high.text, fifty_two_week_low.text,
    rsi_fourteen.text, rel_volume.text, avg_volume.text, the_volume.text]
    return column_5_info

def column_5_str():
    shs_outstand_string = "Shs Outstand: "
    shs_float_string = "Shs Float: "
    short_float_string = "Short Float: "
    short_ratio_string = "Short Ratio: "
    target_price_string = "Target Price: "
    fifty_two_week_range_string = "52W Range: "
    fifty_two_week_high_string = "52W High: "
    fifty_two_week_low_string = "52W Low: "
    rsi_fourteen_string = "RSI (14): " 
    rel_volume_string = "Rel Volume: "
    avg_volume_string = "Avg Volume: "
    the_volume_string = "Volume: "
    column_5_string = [shs_outstand_string, shs_float_string, short_float_string, short_ratio_string, target_price_string,
    fifty_two_week_range_string, fifty_two_week_high_string, fifty_two_week_low_string,
    rsi_fourteen_string, rel_volume_string, avg_volume_string, the_volume_string]
    return column_5_string

def column_6_val():
    perf_week = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[1]/td[12]/b/span")
    perf_month = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[2]/td[12]/b/span")
    perf_quarter = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[3]/td[12]/b/span")
    perf_half_y = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[4]/td[12]/b/span")
    perf_year = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[5]/td[12]/b/span")
    perf_ytd = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[6]/td[12]/b/span")
    beta = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[7]/td[12]/b")
    atr = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[8]/td[12]/b")
    volatility = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[9]/td[12]/b/small")
    prev_close = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[10]/td[12]/b")
    the_price = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[11]/td[12]/b")
    change = browser.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[12]/td[12]/b/span")
    column_6_info = [perf_week.text, perf_month.text, perf_quarter.text, perf_half_y.text, perf_year.text,
    perf_ytd.text, beta.text, atr.text, volatility.text, prev_close.text, the_price.text, change.text]
    return column_6_info


def column_6_str():
    perf_week_string = "Perf Week: "
    perf_month_string = "Perf Month: "
    perf_quarter_string = "Perf Quarter: "
    perf_half_y_string = "Perf Half Y: "
    perf_year_string = "Perf Year: "
    perf_ytd_string = "Perf YTD: "
    beta_string = "Beta: "
    atr_string = "ATR: "
    volatility_string = "Volatility: "
    prev_close_string = "Prev Close: "
    the_price_string = "Price: "
    change_string = "Change: "
    column_6_string = [perf_week_string, perf_month_string, perf_quarter_string, perf_half_y_string, perf_year_string,
    perf_ytd_string, beta_string, atr_string, volatility_string, prev_close_string, the_price_string, change_string]
    return column_6_string

def table_Menu():
    print("\nPlease Select the elements from each column that you wish to review:\n\n")
    print("   Column 1      Column 2          Column 3          Column 4           Columh 5         Column 6")
    print("  ----------    -----------       -----------       -----------        -----------      ------------")
    print("1. Index        1. P/E            1. EPS (ttm)      1. Insider Own    1. Shs Outstand   1. Perf Week")
    print("2. Market Cap   2. Forward P/E    2. EPS next Y     2. Insider Trans  2. Shs Float      2. Perf Month")
    print("3. Income       3. PEG            3. EPS next Q     3. Inst Own       3. Short Float    3. Perf Quarter")
    print("4. Sales        4. P/S            4. EPS this Y     4. Inst Trans     4. Short Ratioo   4. Perf Half Y")
    print("5. Book/sh      5. P/B            5. EPS next Y %   5. ROA            5. Target Price   5. Perf Year")
    print("6. Cash/sh      6. P/C            6. EPS next 5Y    6. ROE            6. 52W Range      6. Perf YTD")
    print("7. Dividend     7. P/FCF          7. EPS past 5Y    7. ROI            7. 52W High       7. Beta")
    print("8. Dividend %   8. Quick Ratio    8. Sales past 5Y  8. Gross Margin   8. 52W Low        8. ATR")
    print("9. Employees    9. Current Ratio  9. Sals Q/Q       9. Open Margin    9. RSI (14)       9. Volatility")
    print("10. Optionable  10. Debt/Eq        10. EPS Q/Q       10. Profit Margin 10. Rel Volumne   10. Prev Close")
    print("11. Shortable   11. Lt Debt/Eq    11. Earnings      11. Payout        11. Avg Volume    11. Price")
    print("12. Recom       12. SMA20         12. SMA50         12. SMA200        12. Volume        12. Change\n\n")

def preferred_column_list():
    str_arr_col_1 = input("Please select the elements from column 1: ").split(" ")
    col_1 = [int(num) for num in str_arr_col_1]
    str_arr_col_2 = input("Please select the elements from column 2: ").split(" ")
    col_2 = [int(num) for num in str_arr_col_2]
    str_arr_col_3 = input("Please select the elements from column 3: ").split(" ")
    col_3 = [int(num) for num in str_arr_col_3]
    str_arr_col_4 = input("Please select the elements from column 4: ").split(" ")
    col_4 = [int(num) for num in str_arr_col_4]
    str_arr_col_5 = input("Please select the elements from column 5: ").split(" ")
    col_5 = [int(num) for num in str_arr_col_5]
    str_arr_col_6 = input("Please select the elements from column 6: ").split(" ")
    col_6 = [int(num) for num in str_arr_col_6]
    return col_1, col_2, col_3, col_4, col_5, col_6

def table_iterator():
    if(len(colu_1) != 0):
        store_column_1_values = column_1_val()
        store_column_1_strings = column_1_str()
        for i in range(len(colu_1)):
            value = colu_1[i]
            value = int(value)
            value = value -1
            print(store_column_1_strings[value] + store_column_1_values[value] + " ", end='')
    if(len(colu_2) != 0):
        print()
        store_column_2_values = column_2_val()
        store_column_2_strings = column_2_str()
        for i in range(len(colu_2)):
            value = colu_2[i]
            value = int(value)
            value = value -1
            print(store_column_2_strings[value] + store_column_2_values[value] + " ", end='')
    if(len(colu_3) != 0):
        print()
        store_column_3_values = column_3_val()
        store_column_3_strings = column_3_str()
        for i in range(len(colu_3)):
            value = colu_3[i]
            value = int(value)
            value = value -1
            print(store_column_3_strings[value] + store_column_3_values[value] + " ", end='')
    if(len(colu_4) != 0):
        print()
        store_column_4_values = column_4_val() 
        store_column_4_strings = column_4_str()
        for i in range(len(colu_4)):
            value = int(colu_4[i])
            value = value -1
            print(store_column_4_strings[value] + store_column_4_values[value] + " ", end='')
    if(len(colu_5) != 0):
        print()
        store_column_5_values = column_5_val() 
        store_column_5_strings = column_5_str()
        for i in range(len(colu_5)):
            value = int(colu_5[i])
            value = value -1
            print(store_column_5_strings[value] + store_column_5_values[value] + " ", end='')
    if(len(colu_6) != 0):
        print()
        store_column_6_values = column_6_val() 
        store_column_6_strings = column_6_str()
        for i in range(len(colu_6)):
            value = int(colu_6[i])
            value = value -1
            print(store_column_6_strings[value] + store_column_6_values[value] + " ", end='')
            
# Still needs to be fixed. 
def table_iterator_for_saving(i):
    File = open(list[i]+".csv", 'w+')
    Data = csv.writer(File)
    if(len(colu_1) != 0):
        store_column_1_values = column_1_val() 
        store_column_1_strings = column_1_str()
        Data.writerows([store_column_1_strings])
        Data.writerows([store_column_1_values])
        for i in range(len(colu_1)):
            value = colu_1[i]
            value = int(value)
            value = value -1
            print(store_column_1_strings[value] + store_column_1_values[value] + " ", end='')
    if(len(colu_2) != 0):
        print()
        store_column_2_values = column_2_val()
        store_column_2_strings = column_2_str()
        Data.writerows([store_column_2_strings])
        Data.writerows([store_column_2_values])
        for i in range(len(colu_2)):
            value = colu_2[i]
            value = int(value)
            value = value -1
            print(store_column_2_strings[value] + store_column_2_values[value]+ " ", end='')
    if(len(colu_3) != 0):
        print()
        store_column_3_values = column_3_val()
        store_column_3_strings = column_3_str()
        Data.writerows([store_column_3_strings])
        Data.writerows([store_column_3_values])
        for i in range(len(colu_3)):
            value = colu_3[i]
            value = int(value)
            value = value -1
            print(store_column_3_strings[value] + store_column_3_values[value]+ " ", end='')
    if(len(colu_4) != 0):
        print()
        store_column_4_values = column_4_val()
        store_column_4_strings = column_4_str()
        Data.writerows([store_column_4_strings])
        Data.writerows([store_column_4_values])
        for i in range(len(colu_4)):
            value = colu_4[i]
            value = int(value)
            value = value -1
            print(store_column_4_strings[value] + store_column_4_values[value]+ " ", end='')
    if(len(colu_5) != 0):
        print()
        store_column_5_values = column_5_val()
        store_column_5_strings = column_5_str()
        Data.writerows([store_column_5_strings])
        Data.writerows([store_column_5_values])
        for i in range(len(colu_5)):
            value = colu_5[i]
            value = int(value)
            value = value -1
            print(store_column_5_strings[value] + store_column_5_values[value]+ " ", end='')
    if(len(colu_6) != 0):
        print()
        store_column_6_values = column_6_val()
        store_column_6_strings = column_6_str()
        Data.writerows([store_column_6_strings])
        Data.writerows([store_column_6_values])
        for i in range(len(colu_6)):
            value = colu_6[i]
            value = int(value)
            value = value -1
            print(store_column_6_strings[value] + store_column_6_values[value]+ " ", end='')
    File.close()

browser = setUp()
#This is an example of a tuple
#a functionality that allows us to return
#two things from a function
n, list = inquiryList()
resume = "Y"
i = 0

#While Loop for multiple stock searches
while resume == "Y" and i <= n:
    stock_name = list[i]
    response = searchStocks(stock_name)
    if response == "2":
        table_Menu()
        colu_1, colu_2, colu_3, colu_4, colu_5, colu_6 = preferred_column_list()
        save_keys = input("\nWould yuo like to save this data (Y/N): ")
        if(save_keys == "Y" or save_keys == "y"):
            table_iterator_for_saving(i)
        else:
            table_iterator()
    question = input("\n\nWould yoou like to search another stock (Y/N)? ")
    if(question == "Yes" or question == "Y" or question == "yes" or question == 'y'):
        resume = "Y"
        i+=1
        continue
    if(question == "No" or question == "N" or question == "no" or question == "n"):
        resume = "N"
        browser.quit()
        break
    while(question != "Yes" or question != "yes" or question != "Y" or question != "y" 
        or question != "N" or question != "n" or question != "No" or question != "no"):
            print("Invalid response: Please enter \"Yes\", \"Y\", \"No\", or \"N\"")
            question = input("Would yoou like to search another stock (Y/N)? ")
            if(question == "Yes" or question == "Y" or question == "yes" or question == 'y'):
                break
            if(question == "No" or question == "N" or question == "no" or question == "n"):
                break