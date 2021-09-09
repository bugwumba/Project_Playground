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
from selenium.common.exceptions import TimeoutException
import time
import csv

# pylint: disable=no-member

class Stock():

    # The following functions hold 
    # Data table informatioono 
    def column_1_val(self):
        delay = 10
        try:
            index = WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/table[2]/tbody/tr[1]/td[2]")))
        except TimeoutException:
            print("Loading took too much time! Please check your network connectivity")
            self.driver.quit()
            exit()
        market_cap = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[2]/td[2]/b")
        income = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[3]/td[2]/b")
        sales = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[4]/td[2]/b")
        book_sh = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[5]/td[2]/b")
        cash_sh = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[6]/td[2]/b") 
        dividend = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[7]/td[2]/b")
        dividend_percent = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[8]/td[2]/b")
        employees = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[9]/td[2]/b")
        optionable = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[10]/td[2]/b")
        shortfall = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[11]/td[2]/b")
        recom = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[12]/td[2]/b")
        colum_1_info = [index.text, market_cap.text, income.text, sales.text, book_sh.text, cash_sh.text, dividend.text,
        dividend_percent.text, employees.text, optionable.text, shortfall.text, recom.text]
        return colum_1_info

    def column_1_str(self):
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

    def column_2_val(self):
        delay = 10
        try:
            p_e = WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/table[2]/tbody/tr[1]/td[4]/b")))
        except TimeoutException:
            print("Loading took too much time! Please check your network connectivity")
            self.driver.quit()
            exit()
        forward_p_e = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[2]/td[4]/b")
        peg = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[3]/td[4]/b")
        p_s = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[4]/td[4]/b")
        p_b = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[5]/td[4]/b")
        p_c = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[6]/td[4]/b")
        p_fcf = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[7]/td[4]/b")
        quick_ratio = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[8]/td[4]/b")
        current_ratio = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[9]/td[4]/b")
        debt_eq = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[10]/td[4]/b/span")
        lt_debt_eq = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[11]/td[4]/b/span")
        sma_20 = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[12]/td[4]/b/span")
        column_2_info = [p_e.text, forward_p_e.text, peg.text, p_s.text, p_b.text, p_c.text, p_fcf.text, 
        quick_ratio.text, current_ratio.text, debt_eq.text, lt_debt_eq.text, sma_20.text]
        return column_2_info

    def column_2_str(self):
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

    def column_3_val(self):
        delay = 10
        try:
            eps_ttm = WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/table[2]/tbody/tr[12]/td[4]/b/span")))
        except TimeoutException:
            print("Loading took too much time! Please check your network connectivity")
            self.driver.quit()
            exit()
        eps_next_y = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[2]/td[6]/b")
        eps_next_q = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[3]/td[6]/b")
        eps_this_y = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[2]/td[6]/b")
        eps_next_y_percent = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[5]/td[6]/b")
        eps_next_5y = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[6]/td[6]/b")
        eps_past_5y = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[7]/td[6]/b")
        sales_past_5y = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[8]/td[6]/b")
        sales_q_q = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[9]/td[6]/b/span")
        eps_q_q = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[10]/td[6]/b/span")
        earnings = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[11]/td[6]/b")
        sma_50 = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[12]/td[6]/b")
        column_3_info = [eps_ttm.text, eps_next_y.text, eps_next_q.text, eps_this_y.text, eps_next_y_percent.text,
        eps_next_5y.text, eps_past_5y.text, sales_past_5y.text, sales_q_q.text, eps_q_q.text, earnings.text, sma_50.text]
        return column_3_info

    def column_3_str(self):
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

    def column_4_val(self):
        delay = 10
        try:
            insider_own = WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/table[2]/tbody/tr[1]/td[8]/b")))
        except TimeoutException:
            print("Loading took too much time! Please check your network connectivity")
            self.driver.quit()
            exit()
        insider_trans = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[2]/td[8]/b")
        inst_own = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[3]/td[8]/b")
        inst_trans = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[4]/td[8]/b")
        roa = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[5]/td[8]/b")
        roe = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[6]/td[8]/b")
        roi = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[7]/td[8]/b")
        gross_margin = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[8]/td[8]/b")
        open_margin = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[9]/td[8]/b")
        profit_margin = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[10]/td[8]/b")
        payout = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[11]/td[8]/b")
        sma_200 = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[12]/td[8]/b/span")
        column_4_info = [insider_own.text, insider_trans.text, inst_own.text, inst_trans.text, roa.text,
        roe.text, roi.text, gross_margin.text, open_margin.text, profit_margin.text, payout.text, sma_200.text]
        return column_4_info

    def column_4_str(self):
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

        
    def column_5_val(self):
        delay = 10
        try:
            shs_outstand = WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/table[2]/tbody/tr[1]/td[10]/b")))
        except TimeoutException:
            print("Loading took too much time! Please check your network connectivity")
            self.driver.quit()
            exit()
        shs_float = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[2]/td[10]/b")
        short_float = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[3]/td[10]/b")
        short_ratio = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[4]/td[10]/b")
        target_price = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[5]/td[10]/b/span")
        fifty_two_week_range = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[6]/td[10]/b/small")
        fifty_two_week_high = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[7]/td[10]/b/span")
        fifty_two_week_low = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[8]/td[10]/b/span")
        rsi_fourteen = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[9]/td[10]/b")
        rel_volume = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[10]/td[10]/b")
        avg_volume = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[11]/td[10]/b")
        the_volume = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[12]/td[10]/b")
        column_5_info = [shs_outstand.text, shs_float.text, short_float.text, short_ratio.text, target_price.text,
        fifty_two_week_range.text, fifty_two_week_high.text, fifty_two_week_low.text,
        rsi_fourteen.text, rel_volume.text, avg_volume.text, the_volume.text]
        return column_5_info

    def column_5_str(self):
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

    def column_6_val(self):
        delay = 10
        try:
            perf_week = WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/table[2]/tbody/tr[1]/td[12]/b/span")))
        except TimeoutException:
            print("Loading took too much time! Please check your network connectivity")
            self.driver.quit()
            exit()
        perf_month = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[2]/td[12]/b/span")
        perf_quarter = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[3]/td[12]/b/span")
        perf_half_y = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[4]/td[12]/b/span")
        perf_year = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[5]/td[12]/b/span")
        perf_ytd = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[6]/td[12]/b/span")
        beta = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[7]/td[12]/b")
        atr = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[8]/td[12]/b")
        volatility = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[9]/td[12]/b/small")
        prev_close = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[10]/td[12]/b")
        the_price = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[11]/td[12]/b")
        change = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[12]/td[12]/b/span")
        column_6_info = [perf_week.text, perf_month.text, perf_quarter.text, perf_half_y.text, perf_year.text,
        perf_ytd.text, beta.text, atr.text, volatility.text, prev_close.text, the_price.text, change.text]
        return column_6_info


    def column_6_str(self):
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


class Stock_Table_Menu(Stock):

    def table_Menu(self):
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
        print("10. Optionable  10. Ebt/Eq        10. EPS Q/Q       10. Profit Margin 10. Rel Volumne   10. Prev Close")
        print("11. Shortable   11. Lt Debt/Eq    11. Earnings      11. Payout        11. Avg Volume    11. Price")
        print("12. Recom       12. SMA20         12. SMA50         12. SMA200        12. Volume        12. Change\n\n")

    def user_Menu(self):
        print("\n\nWhat would you like to do:")
        print("1. View the next stock")
        print("2. View the last stock")
        print("3. Search a different stock")

    def preferred_column_list(self):
        while True:
            try:
                str_arr_col_1 = input("Please select the elements from column 1: ").split(" ")
                col_1 = [int(num) for num in str_arr_col_1]
            except ValueError:
                print("Invalid Entry!\n")
                continue
            else:
                break
        while True:
            try:
                str_arr_col_2 = input("Please select the elements from column 2: ").split(" ")
                col_2 = [int(num) for num in str_arr_col_2]
            except ValueError:
                print("Invalid Entry!\n")
                continue
            else:
                break
        while True:
            try:
                str_arr_col_3 = input("Please select the elements from column 3: ").split(" ")
                col_3 = [int(num) for num in str_arr_col_3]
            except ValueError:
                print("Invalid Entry!\n")
                continue
            else:
                break
        while True:
            try:
                str_arr_col_4 = input("Please select the elements from column 4: ").split(" ")
                col_4 = [int(num) for num in str_arr_col_4]
            except ValueError:
                print("Invalid Entry!\n")
                continue
            else:
                break
        while True:
            try:
                str_arr_col_5 = input("Please select the elements from column 5: ").split(" ")
                col_5 = [int(num) for num in str_arr_col_5]
            except ValueError:
                print("Invalid Entry!\n")
                continue
            else:
                break
        while True:
            try:
                str_arr_col_6 = input("Please select the elements from column 6: ").split(" ")
                col_6 = [int(num) for num in str_arr_col_6]
            except ValueError:
                print("Invalid Entry!\n")
                continue
            else:
                break
        return col_1, col_2, col_3, col_4, col_5, col_6

class My_Chrome(Stock_Table_Menu):

    # Fucntion to hold website 
    def return_Website(self):
        return "https://finviz.com"


    #Function to open browser to webpage
    def setUp(self):
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
        self.options = webdriver.ChromeOptions()
        self.options.headless = True
        self.options.add_argument(f'user-agent={user_agent}')
        self.options.add_argument("--window-size=1920,1080")
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--allow-running-insecure-content')
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--proxy-server='direct://'")
        self.options.add_argument("--proxy-bypass-list=*")
        self.options.add_argument("--start-maximized")
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(options=self.options)
        # self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        website = self.return_Website()
        self.driver.get(website)
        print(self.driver.title)
        return self.driver

    #Function to search stocks
    def searchStocks(self, stock_name):
        delay = 10
        try:
            search = WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/table[1]/tbody/tr[1]/td/table/tbody/tr/td[1]/table/tbody/tr[2]/td/div/form/input")))
        except TimeoutException:
            print("Loading took too much time! Please check your network connectivity")
            self.driver.quit()
            exit()
        search.send_keys(stock_name)
        search.send_keys(Keys.RETURN)
        print("\n")
        while True:
            try:
                print(self.driver.title)
                print("What would you like to see about " + stock_name + "?")
                print("1. The whole table")
                print("2. Your preferred list")
                self.response = int(input("Please select one of the two options: ")) 
            except ValueError:
                print("Invalid Entry!\n")
                continue
            else:
                self.response = str(self.response)
                break
        if self.response == "1":
            delay = 10
            try:
                table = WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, "snapshot-table2")))
            except TimeoutException:
                print("Loading took too much time! Please check your network connectivity")
                self.driver.quit()
                exit()
            print()        
            print(table.text)
            return self.response
        if self.response == "2":
            return self.response

    #Function to get list of stocks
    def inquiryList(self):
        #Creates an empty list
        self.list = []
        #Number of elements as input
        while True:
            try:
                self.n = int(input("Enter the numbe of stocks you would like to review: "))
            except ValueError:
                print("Invalid Entry!\n")
                continue
            else:
                break
        #Iterating till the range
        for self.stock in range(0, self.n):
            while True:
                try:
                    self.stock = input("Enter the ticker symbol or company name: ")
                    self.stock = str(self.stock)
                except ValueError:
                    print("Invalid Entry!\n")
                    continue
                else:
                    self.list.append(self.stock)                     
                    break
        print(self.list)
        return self.n, self.list

class Saved_Files(My_Chrome):
    
    # Still needs to be fixed. 
    def table_iterator_for_saving(self, i):
        self.colu_1, self.colu_2, self.colu_3, self.colu_4, self.colu_5, self.colu_6 = self.preferred_column_list()
        File = open(list[i]+".csv", 'w+')
        Data = csv.writer(File)
        if(len(self.colu_1) != 0):
            print("\n")
            self.store_column_1_values = self.column_1_val() 
            self.store_column_1_strings = self.column_1_str()
            Data.writerows([self.store_column_1_strings])
            Data.writerows([self.store_column_1_values])
            for i in range(len(self.colu_1)):
                value = self.colu_1[i]
                value = int(value)
                value = value -1
                print(self.store_column_1_strings[value] + self.store_column_1_values[value] + " ", end='')
        if(len(self.colu_2) != 0):
            print()
            self.store_column_2_values = self.column_2_val()
            self.store_column_2_strings = self.column_2_str()
            Data.writerows([self.store_column_2_strings])
            Data.writerows([self.store_column_2_values])
            for i in range(len(self.colu_2)):
                value = self.colu_2[i]
                value = int(value)
                value = value -1
                print(self.store_column_2_strings[value] + self.store_column_2_values[value]+ " ", end='')
        if(len(self.colu_3) != 0):
            print()
            self.store_column_3_values = self.column_3_val()
            self.store_column_3_strings = self.column_3_str()
            Data.writerows([self.store_column_3_strings])
            Data.writerows([self.store_column_3_values])
            for i in range(len(self.colu_3)):
                value = self.colu_3[i]
                value = int(value)
                value = value -1
                print(self.store_column_3_strings[value] + self.store_column_3_values[value]+ " ", end='')
        if(len(self.colu_4) != 0):
            print()
            self.store_column_4_values = self.column_4_val()
            self.store_column_4_strings = self.column_4_str()
            Data.writerows([self.store_column_4_strings])
            Data.writerows([self.store_column_4_values])
            for i in range(len(self.colu_4)):
                value = self.colu_4[i]
                value = int(value)
                value = value -1
                print(self.store_column_4_strings[value] + self.store_column_4_values[value]+ " ", end='')
        if(len(self.colu_5) != 0):
            print()
            self.store_column_5_values = self.column_5_val()
            self.store_column_5_strings = self.column_5_str()
            Data.writerows([self.store_column_5_strings])
            Data.writerows([self.store_column_5_values])
            for i in range(len(self.colu_5)):
                value = self.colu_5[i]
                value = int(value)
                value = value -1
                print(self.store_column_5_strings[value] + self.store_column_5_values[value]+ " ", end='')
        if(len(self.colu_6) != 0):
            print()
            self.store_column_6_values = self.column_6_val()
            self.store_column_6_strings = self.column_6_str()
            Data.writerows([self.store_column_6_strings])
            Data.writerows([self.store_column_6_values])
            for i in range(len(self.colu_6)):
                value = self.colu_6[i]
                value = int(value)
                value = value -1
                print(self.store_column_6_strings[value] + self.store_column_6_values[value])
        File.close()

class Window_Messages(Saved_Files):

    def table_iterator(self, *args):
        self.colu_1, self.colu_2, self.colu_3, self.colu_4, self.colu_5, self.colu_6 = self.preferred_column_list()
        if(len(self.colu_1) != 0):
            self.store_column_1_values = self.column_1_val()
            self.store_column_1_strings = self.column_1_str()
            for i in range(len(self.colu_1)):
                value = self.colu_1[i]
                value = int(value)
                value = value -1
                print(self.store_column_1_strings[value] + self.store_column_1_values[value] + " ", end='')
        if(len(self.colu_2) != 0):
            print()
            self.store_column_2_values = self.column_2_val()
            self.store_column_2_strings = self.column_2_str()
            for i in range(len(self.colu_2)):
                value = self.colu_2[i]
                value = int(value)
                value = value -1
                print(self.store_column_2_strings[value] + self.store_column_2_values[value] + " ", end='')
        if(len(self.colu_3) != 0):
            print()
            self.store_column_3_values = self.column_3_val()
            self.store_column_3_strings = self.column_3_str()
            for i in range(len(self.colu_3)):
                value = self.colu_3[i]
                value = int(value)
                value = value -1
                print(self.store_column_3_strings[value] + self.store_column_3_values[value] + " ", end='')
        if(len(self.colu_4) != 0):
            print()
            self.store_column_4_values = self.column_4_val() 
            self.store_column_4_strings = self.column_4_str()
            for i in range(len(self.colu_4)):
                value = self.colu_4[i]
                value = int(value)
                value = value -1
                print(self.store_column_4_strings[value] + self.store_column_4_values[value] + " ", end='')
        if(len(self.colu_5) != 0):
            print()
            self.store_column_5_values = self.column_5_val() 
            self.store_column_5_strings = self.column_5_str()
            for i in range(len(self.colu_5)):
                value = self.colu_5[i]
                value = int(value)
                value = value -1
                print(self.store_column_5_strings[value] + self.store_column_5_values[value] + " ", end='')
        if(len(self.colu_6) != 0):
            print()
            self.store_column_6_values = self.column_6_val() 
            self.store_column_6_strings = self.column_6_str()
            for i in range(len(self.colu_6)):
                value = self.colu_6[i]
                value = int(value)
                value = value -1
                print(self.store_column_6_strings[value] + self.store_column_6_values[value])

class Investment_Playground(Window_Messages):
    
    def seeder_program(self,n):
        #While Loop for multiple stock searches
        resume = "Y"
        i = 0
        while resume == "Y" and i <= n-1:
            stock_name = self.list[i]
            response = browser.searchStocks(stock_name)
            if response == "2":
                browser.table_Menu()
                while True:
                    try:
                        save_keys = input("\nWould you like to save this data (Y/N): ")
                    except ValueError:
                        print("Invalid Entry!\n")
                        continue
                    else:
                        break
                if(save_keys == "Y" or save_keys == "y"):
                    browser.table_iterator_for_saving(i)
                else:
                    browser.table_iterator()
            self.position = i+2
            self.counter = n
            if(self.position > self.counter):
                while True:
                    try:
                        print("\n\nThank you for using Investment Playground!")
                        print("What would you like to do?")
                        print("1. Quit?")
                        print("2. Search More Stocks!")
                        self.dialogue = int(input("Please select one of the two choices: "))
                    except ValueError:
                        print("Invalid Entry!")
                        continue
                    else:
                        self.dialogue = str(self.dialogue)
                        break
                if(self.dialogue == "1" or self.dialogue == "Q" or self.dialogue == "q" or self.dialogue == "quit" or self.dialogue == "Quit"):
                    print("Goodbye and Good Luck!")
                    self.driver.quit()
                    exit()
                if(self.dialogue == "2" or self.dialogue == "Yes" or self.dialogue == "Y" or self.dialogue == "y" or self.dialogue == "yes"):
                    self.list.clear()
                    n, self.list = browser.inquiryList()
                    i = 0
                    continue
            while True:
                try:
                    self.user_Menu()
                    self.question = int(input("\n\nPlease select one of the 3 choices: "))
                except ValueError:
                    print("Invalid Entry!")
                    continue
                else:
                    self.question = str(self.question)
                    break
            if(self.question == "1"):
                i+=1
                continue
            if(self.question == "2"):
                resume = "Y"
                i = len(self.list)-1
                continue
            if(self.question == "3"):
                print("The remaining stocks are: "+ " ", end='')
                self.z = i+1
                for self.z in range(len(list)):
                    print(list[self.z]+" ", end='')
                self.the_user_wants = input("\n\nEnter the ticker symbool or company name: ")
                self.list[i] = self.the_user_wants
                continue

browser = Investment_Playground()
browser.setUp()
n, list = browser.inquiryList()

browser.seeder_program(n)