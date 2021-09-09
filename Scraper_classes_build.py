import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image
import pandas as pd
import sys
import csv
import json
import os
import selenium
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from ttkwidgets.autocomplete import AutocompleteCombobox, autocompletecombobox
import yfinance as yf
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from selenium.common.exceptions import TimeoutException
from googleapiclient.http import MediaIoBaseDownload
from io import BytesIO



root = tk.Tk()
root.title("Project Playground - Investment Playground")
root.iconbitmap('/Users/buddyugwumba1/WebScrapper/Caesar_Planet_of_the_Apes.icns')
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# pylint: disable=no-member

class Stock():

        # recom = self.driver.find_element_by_xpath("/html/body/div[4]/div/table[2]/tbody/tr[12]/td[2]/b")
        # colum_1_info = [index.text, market_cap.text, income.text, sales.text, book_sh.text, cash_sh.text, dividend.text,
        # dividend_percent.text, employees.text, optionable.text, shortfall.text, recom.text]
        # return colum_1_info

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


class My_Chrome():

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
        print(self.driver.title)

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


browser = Window_Messages()
browser.setUp()

def activate_screener():
    delay = 10
    if(selected_method1.get() == "Ticker Symbol"):
        stock = selected_method2.get()
        browser.searchStocks(stock)
        try:
            print("Looking for element")
            graph = WebDriverWait(browser.driver,delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[1]/div/div[2]")))
            graph_location = graph.location
            size = graph.size
            png = browser.driver.get_screenshot_as_png()

            stock_graph = Image.open(BytesIO(png))
            left = graph_location['x']
            top = graph_location['y']
            right = graph_location['x'] + size['width']+1800
            bottom = graph_location['y'] + size['height']+800

            stock_graph = stock_graph.crop((left, top, right, bottom))
            stock_graph.thumbnail((1400,680))

            stock_graph.save('screenshot.png')
            img=ImageTk.PhotoImage(file="/Users/buddyugwumba1/Documents/Buddy Ugwumba/A - Z Capital Investment Group/Python/Python_3/screenshot.png", master=graphical_display_window)
            my_image = graphical_display_window.create_image(-150,-100, anchor=tk.NW, image=img)
            graphical_display_window.itemconfigure(tagOrId=my_image, Image=my_image)
            
        except TimeoutError:
            print('Process took too long')
    if(selected_method1.get() == "Company Name"):
        company_name = selected_method3.get()
        browser.searchStocks(company_name)
        try:
            graph = WebDriverWait(browser.driver,delay).until(EC.presence_of_element_located((By.CLASS_NAME, "interactive-chart small")))
            graph_location = graph.location
            size = graph.size()
            png = browser.get_screenshot_as_png()

            stock_graph = Image.open(BytesIO(png))
            left = graph_location['x']
            top = graph_location['y']
            right = graph_location['x'] + size['2560']
            bottom = graph_location['y'] + size['800']

            # stock_graph = stock_graph.crop((left, top, right, bottom))
            # stock_graph.save('screenshot.png')
            # img=ImageTk.PhotoImage(file="/Users/buddyugwumba1/Documents/Buddy Ugwumba/A - Z Capital Investment Group/Python/Python_3/screenshot.png")
        except TimeoutException:
            print('Process took too long')



def column_1_val1():
    delay = 10
    if(var1.get() == "1"):
        entry_1.delete(0, tk.END)
        try:
            index = WebDriverWait(browser.driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/table[2]/tbody/tr[1]/td[2]")))
            index = index.text
            entry_1.insert(0, index)
        except TimeoutException:
            entry_1.delete(0, tk.END)
            entry_1.insert(0, "----")
    if(var1.get() == "0"):
        entry_1.delete(0, tk.END)
        entry_1.insert(0, "----")

def column_1_val2():
    delay = 10
    if(var2.get() == "1"):
        entry_2.delete(0, tk.END)
        try:
            market_cap = WebDriverWait(browser.driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/table[2]/tbody/tr[2]/td[2]/b")))
            market_cap = market_cap.text
            entry_2.insert(0, market_cap)
        except TimeoutException:
            entry_2.delete(0, tk.END)
            entry_2.insert(0, "----")
    if(var2.get() == "0"):
        entry_2.delete(0, tk.END)
        entry_2.insert(0, "----")

def column_1_val3():
    delay = 10
    if(var3.get() == "1"):
        entry_3.delete(0, tk.END)
        try:
            income = WebDriverWait(browser.driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/table[2]/tbody/tr[3]/td[2]/b")))
            income = income.text
            entry_3.insert(0, income)
        except TimeoutException:
            entry_3.delete(0, tk.END)
            entry_3.insert(0, "----")
    if(var3.get() == "0"):
        entry_3.delete(0, tk.END)
        entry_3.insert(0, "----")

def column_1_val4():
    delay = 10
    if(var4.get() == "1"):
        entry_4.delete(0, tk.END)
        try:
            sales = WebDriverWait(browser.driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/table[2]/tbody/tr[4]/td[2]/b")))
            sales = sales.text
            entry_4.insert(0, sales)
        except TimeoutException:
            entry_4.delete(0, tk.END)
            entry_4.insert(0, "----")
    if(var4.get() == "0"):
        entry_d.delete(0, tk.END)
        entry_4.insert(0, "----")

def column_1_val5():
    delay = 10
    if(var5.get() == "1"):
        entry_5.delete(0, tk.END)
        try:
            book_sh = WebDriverWait(browser.driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/table[2]/tbody/tr[5]/td[2]/b")))
            book_sh = book_sh.text
            entry_5.insert(0, book_sh)
        except TimeoutException:
            entry_5.delete(0, tk.END)
            entry_5.insert(0, "----")
    if(var5.get() == "0"):
        entry_5.delete(0, tk.END)
        entry_5.insert(0, "----")

def column_1_val6():
    delay = 10
    if(var6.get() == "1"):
        entry_6.delete(0, tk.END)
        try:
            cash_sh = WebDriverWait(browser.driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/table[2]/tbody/tr[6]/td[2]/b")))
            cash_sh = cash_sh.text
            entry_6.insert(0, cash_sh)
        except TimeoutException:
            entry_6.delete(0, tk.END)
            entry_6.insert(0, "----")
    if(var6.get() == "0"):
        entry_6.delete(0, tk.END)
        entry_6.insert(0, "----")

def column_1_val7():
    delay = 10
    if(var7.get() == "1"):
        entry_7.delete(0, tk.END)
        try:
            dividend = WebDriverWait(browser.driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/table[2]/tbody/tr[7]/td[2]/b")))
            dividend = dividend.text
            entry_7.insert(0, dividend)
        except TimeoutException:
            entry_7.delete(0, tk.END)
            entry_7.insert(0, "----")
    if(var7.get() == "0"):
        entry_7.delete(0, tk.END)
        entry_7.insert(0, "----")

def column_1_val8():
    delay = 10
    if(var8.get() == "1"):
        entry_8.delete(0, tk.END)
        try:
            dividend_percent = WebDriverWait(browser.driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/table[2]/tbody/tr[8]/td[2]/b")))
            dividend_percent = dividend_percent.text
            entry_8.insert(0, dividend_percent)
        except TimeoutException:
            entry_8.delete(0, tk.END)
            entry_8.insert(0, "----")
    if(var8.get() == "0"):
        entry_8.delete(0, tk.END)
        entry_8.insert(0, "----")

def column_1_val9():
    delay = 10
    if(var9.get() == "1"):
        entry_9.delete(0, tk.END)
        try:
            employees = WebDriverWait(browser.driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/table[2]/tbody/tr[9]/td[2]/b")))
            employees = employees.text
            entry_9.insert(0, employees)
        except TimeoutException:
            entry_9.delete(0, tk.END)
            entry_9.insert(0, "----")
    if(var9.get() == "0"):
        entry_9.delete(0, tk.END)
        entry_9.insert(0, "----")

def column_1_val10():
    delay = 10
    if(var10.get() == "1"):
        entry_10.delete(0, tk.END)
        try:
            optionable = WebDriverWait(browser.driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/table[2]/tbody/tr[10]/td[2]/b")))
            optionable = optionable.text
            entry_10.insert(0, optionable)
        except TimeoutException:
            entry_10.delete(0, tk.END)
            entry_10.insert(0, "----")
    if(var10.get() == "0"):
        entry_10.delete(0, tk.END)
        entry_10.insert(0, "----")

def column_1_val11():
    delay = 10
    if(var11.get() == "1"):
        entry_11.delete(0, tk.END)
        try:
            shortfall = WebDriverWait(browser.driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/table[2]/tbody/tr[11]/td[2]/b")))
            shortfall = shortfall.text
            entry_11.insert(0, shortfall)
        except TimeoutException:
            entry_11.delete(0, tk.END)
            entry_11.insert(0, "----")
    if(var11.get() == "0"):
        entry_11.delete(0, tk.END)
        entry_11.insert(0, "----")

def column_1_val12():
    delay = 10
    if(var12.get() == "1"):
        entry_12.delete(0, tk.END)
        try:
            recom = WebDriverWait(browser.driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/table[2]/tbody/tr[12]/td[2]/b")))
            recom = recom.text
            entry_12.insert(0, recom)
        except TimeoutException:
            entry_12.delete(0, tk.END)
            entry_12.insert(0, "----")
    if(var12.get() == "0"):
        entry_12.delete(0, tk.END)
        entry_12.insert(0, "----")


graphical_display = tk.LabelFrame(root, text="Graphical Display")
graphical_display.grid(row=0, column=0, sticky=tk.NW)
graphical_display.grid_rowconfigure(0, weight = 0)
graphical_display.grid_columnconfigure(0, weight=0)

graphical_display_window = tk.Canvas(graphical_display, width=1150, height=380, bg='white')
graphical_display_window.pack()
graphical_display_window.grid_rowconfigure(0, weight = 0)
graphical_display_window.grid_columnconfigure(0, weight=1)

analysis_display = tk.LabelFrame(root, text ="Quantitative Analysis")
analysis_display.grid(row=0, column =1, sticky=tk.NW)
analysis_display.grid_rowconfigure(0, weight=1)
analysis_display.grid_columnconfigure(0, weight=1)
Label_2 = tk.Label(analysis_display, text="Here is your analysis")
Label_2.grid(row=0, column=0)

quantitative_display = tk.LabelFrame(root, text="Quantitative Data")
quantitative_display.grid(row=1, column=0, sticky=tk.NW)
quantitative_display.grid_rowconfigure(0, weight =1)
quantitative_display.grid_columnconfigure(0, weight=1)

#--------------------------------------------------------------------------------

#Column_1 ------------------------------------------------------------------------------------------
var1 = tk.StringVar()
Label_3 = tk.Checkbutton(quantitative_display, text="Index:", variable=var1, onvalue="1", offvalue="0", width=10, anchor=tk.W, command=column_1_val1)
Label_3.grid(row=0, column=0)
entry_1 = tk.Entry(quantitative_display, width=9)
entry_1.grid(row=0,column=1)

var2 = tk.StringVar()
Label_4 = tk.Checkbutton(quantitative_display, text="Market Cap:", variable=var2, onvalue="1", offvalue="0", width=13, anchor=tk.W, command=column_1_val2)
Label_4.grid(row=1, column=0)
entry_2 = tk.Entry(quantitative_display, width=9)
entry_2.grid(row=1, column=1)

var3 = tk.StringVar()
Label_5 = tk.Checkbutton(quantitative_display, text="Income:", variable=var3, onvalue="1", offvalue="0", width=10, anchor=tk.W, command=column_1_val3)
Label_5.grid(row=2, column=0)
entry_3 = tk.Entry(quantitative_display, width=9)
entry_3.grid(row=2,column=1)

var4 = tk.StringVar()
Label_6 = tk.Checkbutton(quantitative_display, text="Sales:", variable=var4, onvalue="1", offvalue="0", width=10, anchor=tk.W, command=column_1_val4)
Label_6.grid(row=3, column=0)
entry_4 = tk.Entry(quantitative_display, width=9)
entry_4.grid(row=3,column=1)

var5 = tk.StringVar()
Label_7 = tk.Checkbutton(quantitative_display, text="Book/sh:", variable=var5, onvalue="1", offvalue="0", width=10, anchor=tk.W, command=column_1_val5)
Label_7.grid(row=4, column=0)
entry_5 = tk.Entry(quantitative_display, width=9)
entry_5.grid(row=4,column=1)

var6 = tk.StringVar()
Label_8 = tk.Checkbutton(quantitative_display, text="Cash/sh:", variable=var6, onvalue="1", offvalue="0", width=10, anchor=tk.W, command=column_1_val6)
Label_8.grid(row=5, column=0)
entry_6 = tk.Entry(quantitative_display, width=9)
entry_6.grid(row=5,column=1)

var7 = tk.StringVar()
Label_9 = tk.Checkbutton(quantitative_display, text="Dividend:", variable=var7, onvalue="1", offvalue="0", width=10, anchor=tk.W, command=column_1_val7)
Label_9.grid(row=6, column=0)
entry_7 = tk.Entry(quantitative_display, width=9)
entry_7.grid(row=6,column=1)

var8 = tk.StringVar()
Label_10 = tk.Checkbutton(quantitative_display, text="Dividend %:", variable=var8, onvalue="1", offvalue="0", width=13, anchor=tk.W, command=column_1_val8)
Label_10.grid(row=7, column=0)
entry_8 = tk.Entry(quantitative_display, width=9)
entry_8.grid(row=7,column=1)

var9 = tk.StringVar()
Label_11 = tk.Checkbutton(quantitative_display, text="Employees:", variable=var9, onvalue="1", offvalue="0", width=10, anchor=tk.W, command=column_1_val9)
Label_11.grid(row=8, column=0)
entry_9 = tk.Entry(quantitative_display, width=9)
entry_9.grid(row=8,column=1)

var10 = tk.StringVar()
Label_12 = tk.Checkbutton(quantitative_display, text="Optionable:", variable=var10, onvalue="1", offvalue="0", width=10, anchor=tk.W, command=column_1_val10)
Label_12.grid(row=9, column=0)
entry_10 = tk.Entry(quantitative_display, width=9)
entry_10.grid(row=9,column=1)

var11 = tk.StringVar()
Label_13 = tk.Checkbutton(quantitative_display, text="Shortable:", variable=var11, onvalue="1", offvalue="0", width=10, anchor=tk.W, command=column_1_val11)
Label_13.grid(row=10, column=0)
entry_11 = tk.Entry(quantitative_display, width=9)
entry_11.grid(row=10,column=1)

var12 = tk.StringVar()
Label_14 = tk.Checkbutton(quantitative_display, text="Recom:", variable=var12, onvalue="1", offvalue="0", width=10, anchor=tk.W, command=column_1_val12)
Label_14.grid(row=11, column=0)
entry_12 = tk.Entry(quantitative_display, width=9)
entry_12.grid(row=11,column=1)

#Column 2---------------------------------------------------------------------------------------
Label_15 = tk.Checkbutton(quantitative_display, text="P/E:", width=11, anchor=tk.W)
Label_15.grid(row=0, column=2)
entry_13 = tk.Entry(quantitative_display, width=8)
entry_13.grid(row=0,column=3)

Label_16 = tk.Checkbutton(quantitative_display, text="Forward P/E:", width=11, anchor=tk.W)
Label_16.grid(row=1, column=2)
entry_14 = tk.Entry(quantitative_display, width=8)
entry_14.grid(row=1,column=3)

Label_17 = tk.Checkbutton(quantitative_display, text="REG:", width=11, anchor=tk.W)
Label_17.grid(row=2, column=2)
entry_15 = tk.Entry(quantitative_display, width=8)
entry_15.grid(row=2,column=3)

Label_18 = tk.Checkbutton(quantitative_display, text="P/S:", width=11, anchor=tk.W)
Label_18.grid(row=3, column=2)
entry_16 = tk.Entry(quantitative_display, width=8)
entry_16.grid(row=3,column=3)

Label_19 = tk.Checkbutton(quantitative_display, text="P/B:", width=11, anchor=tk.W)
Label_19.grid(row=4, column=2)
entry_17 = tk.Entry(quantitative_display, width=8)
entry_17.grid(row=4,column=3)

Label_20 = tk.Checkbutton(quantitative_display, text="P/C:", width=11, anchor=tk.W)
Label_20.grid(row=5, column=2)
entry_18 = tk.Entry(quantitative_display, width=8)
entry_18.grid(row=5,column=3)

Label_21 = tk.Checkbutton(quantitative_display, text="P/FCF:", width=11, anchor=tk.W)
Label_21.grid(row=6, column=2)
entry_19 = tk.Entry(quantitative_display, width=8)
entry_19.grid(row=6,column=3)

Label_22 = tk.Checkbutton(quantitative_display, text="Quick Ratio:", width=11, anchor=tk.W)
Label_22.grid(row=7, column=2)
entry_20 = tk.Entry(quantitative_display, width=8)
entry_20.grid(row=7,column=3)

Label_23 = tk.Checkbutton(quantitative_display, text="Current Ratio:", width=11, anchor=tk.W)
Label_23.grid(row=8, column=2)
entry_21 = tk.Entry(quantitative_display, width=8)
entry_21.grid(row=8,column=3)

Label_24 = tk.Checkbutton(quantitative_display, text="Debt/Eq:", width=11, anchor=tk.W)
Label_24.grid(row=9, column=2)
entry_22 = tk.Entry(quantitative_display, width=8)
entry_22.grid(row=9,column=3)

Label_25 = tk.Checkbutton(quantitative_display, text="Lt Debt/Eq:", width=11, anchor=tk.W)
Label_25.grid(row=10, column=2)
entry_23 = tk.Entry(quantitative_display, width=8)
entry_23.grid(row=10,column=3)

Label_26 = tk.Checkbutton(quantitative_display, text="SMA20:", width=11, anchor=tk.W)
Label_26.grid(row=11, column=2)
entry_24 = tk.Entry(quantitative_display, width=8)
entry_24.grid(row=11,column=3)


#Column 3------------------------------------------------------------------------------------------
Label_27 = tk.Checkbutton(quantitative_display, text="EPS (ttm):", width=12, anchor=tk.W)
Label_27.grid(row=0, column=4)
entry_25 = tk.Entry(quantitative_display, width=8)
entry_25.grid(row=0,column=5)

Label_28 = tk.Checkbutton(quantitative_display, text="EPS next Y:", width=12, anchor=tk.W)
Label_28.grid(row=1, column=4)
entry_26 = tk.Entry(quantitative_display, width=8)
entry_26.grid(row=1,column=5)

Label_29 = tk.Checkbutton(quantitative_display, text="EPS next Q:", width=12, anchor=tk.W)
Label_29.grid(row=2, column=4)
entry_27 = tk.Entry(quantitative_display, width=8)
entry_27.grid(row=2,column=5)

Label_30 = tk.Checkbutton(quantitative_display, text="EPS this Y:", width=12, anchor=tk.W)
Label_30.grid(row=3, column=4)
entry_28 = tk.Entry(quantitative_display, width=8)
entry_28.grid(row=3,column=5)

Label_31 = tk.Checkbutton(quantitative_display, text="EPS next Y %:", width=12, anchor=tk.W)
Label_31.grid(row=4, column=4)
entry_29 = tk.Entry(quantitative_display, width=8)
entry_29.grid(row=4,column=5)

Label_32= tk.Checkbutton(quantitative_display, text="EPS next 5Y:", width=12, anchor=tk.W)
Label_32.grid(row=5, column=4)
entry_30 = tk.Entry(quantitative_display, width=8)
entry_30.grid(row=5,column=5)

Label_33 = tk.Checkbutton(quantitative_display, text="EPS past 5Y:", width=12, anchor=tk.W)
Label_33.grid(row=6, column=4)
entry_31 = tk.Entry(quantitative_display, width=8)
entry_31.grid(row=6,column=5)

Label_34 = tk.Checkbutton(quantitative_display, text="Sales past 5Y:", width=12, anchor=tk.W)
Label_34.grid(row=7, column=4)
entry_32 = tk.Entry(quantitative_display, width=8)
entry_32.grid(row=7,column=5)

Label_35 = tk.Checkbutton(quantitative_display, text="Sales Q/Q:", width=12, anchor=tk.W)
Label_35.grid(row=8, column=4)
entry_33 = tk.Entry(quantitative_display, width=8)
entry_33.grid(row=8,column=5)

Label_36 = tk.Checkbutton(quantitative_display, text="EPS Q/Q:", width=12, anchor=tk.W)
Label_36.grid(row=9, column=4)
entry_34 = tk.Entry(quantitative_display, width=8)
entry_34.grid(row=9,column=5)

Label_37 = tk.Checkbutton(quantitative_display, text="Earnings:", width=12, anchor=tk.W)
Label_37.grid(row=10, column=4)
entry_35 = tk.Entry(quantitative_display, width=8)
entry_35.grid(row=10,column=5)

Label_38 = tk.Checkbutton(quantitative_display, text="SMA50:", width=12, anchor=tk.W)
Label_38.grid(row=11, column=4)
entry_36 = tk.Entry(quantitative_display, width=8)
entry_36.grid(row=11,column=5)

#Column 4 -----------------------------------------------------------------------------------------------------
Label_39 = tk.Checkbutton(quantitative_display, text="Insider Own:", width=12, anchor=tk.W)
Label_39.grid(row=0, column=6)
entry_37 = tk.Entry(quantitative_display, width=8)
entry_37.grid(row=0,column=7)

Label_40 = tk.Checkbutton(quantitative_display, text="Insider Trans:", width=12, anchor=tk.W)
Label_40.grid(row=1, column=6)
entry_38 = tk.Entry(quantitative_display, width=8)
entry_38.grid(row=1,column=7)

Label_41 = tk.Checkbutton(quantitative_display, text="Inst Own:", width=12, anchor=tk.W)
Label_41.grid(row=2, column=6)
entry_39 = tk.Entry(quantitative_display, width=8)
entry_39.grid(row=2,column=7)

Label_42 = tk.Checkbutton(quantitative_display, text="Inst Trans:", width=12, anchor=tk.W)
Label_42.grid(row=3, column=6)
entry_40 = tk.Entry(quantitative_display, width=8)
entry_40.grid(row=3,column=7)

Label_43 = tk.Checkbutton(quantitative_display, text="ROA:", width=12, anchor=tk.W)
Label_43.grid(row=4, column=6)
entry_41 = tk.Entry(quantitative_display, width=8)
entry_41.grid(row=4,column=7)

Label_44 = tk.Checkbutton(quantitative_display, text="ROE:", width=12, anchor=tk.W)
Label_44.grid(row=5, column=6)
entry_42 = tk.Entry(quantitative_display, width=8)
entry_42.grid(row=5,column=7)

Label_45 = tk.Checkbutton(quantitative_display, text="ROI:", width=12, anchor=tk.W)
Label_45.grid(row=6, column=6)
entry_43 = tk.Entry(quantitative_display, width=8)
entry_43.grid(row=6,column=7)

Label_46 = tk.Checkbutton(quantitative_display, text="Gross Margin:", width=12, anchor=tk.W)
Label_46.grid(row=7, column=6)
entry_44 = tk.Entry(quantitative_display, width=8)
entry_44.grid(row=7,column=7)

Label_47 = tk.Checkbutton(quantitative_display, text="Open Margin:", width=12, anchor=tk.W)
Label_47.grid(row=8, column=6)
entry_45 = tk.Entry(quantitative_display, width=8)
entry_45.grid(row=8,column=7)

Label_48 = tk.Checkbutton(quantitative_display, text="Profit Margin:", width=12, anchor=tk.W)
Label_48.grid(row=9, column=6)
entry_46 = tk.Entry(quantitative_display, width=8)
entry_46.grid(row=9,column=7)

Label_49 = tk.Checkbutton(quantitative_display, text="Payout:", width=12, anchor=tk.W)
Label_49.grid(row=10, column=6)
entry_47 = tk.Entry(quantitative_display, width=8)
entry_47.grid(row=10,column=7)

Label_50 = tk.Checkbutton(quantitative_display, text="SMA200:", width=12, anchor=tk.W)
Label_50.grid(row=11, column=6)
entry_48 = tk.Entry(quantitative_display, width=8)
entry_48.grid(row=11,column=7)

#Column 5--------------------------------------------------------------------------------------------------------------------
Label_51 = tk.Checkbutton(quantitative_display, text="Shs Outstand:", width=11, anchor=tk.W)
Label_51.grid(row=0, column=8)
entry_49 = tk.Entry(quantitative_display, width=8)
entry_49.grid(row=0,column=9)

Label_52 = tk.Checkbutton(quantitative_display, text="Shs Float:", width=11, anchor=tk.W)
Label_52.grid(row=1, column=8)
entry_50 = tk.Entry(quantitative_display, width=8)
entry_50.grid(row=1,column=9)

Label_53 = tk.Checkbutton(quantitative_display, text="Short Float:", width=11, anchor=tk.W)
Label_53.grid(row=2, column=8)
entry_51 = tk.Entry(quantitative_display, width=8)
entry_51.grid(row=2,column=9)

Label_54 = tk.Checkbutton(quantitative_display, text="Short Radio:", width=11, anchor=tk.W)
Label_54.grid(row=3, column=8)
entry_52 = tk.Entry(quantitative_display, width=8)
entry_52.grid(row=3,column=9)

Label_55 = tk.Checkbutton(quantitative_display, text="Target Price:", width=11, anchor=tk.W)
Label_55.grid(row=4, column=8)
entry_53 = tk.Entry(quantitative_display, width=8)
entry_53.grid(row=4,column=9)

Label_56 = tk.Checkbutton(quantitative_display, text="52W Range:", width=11, anchor=tk.W)
Label_56.grid(row=5, column=8)
entry_54 = tk.Entry(quantitative_display, width=8)
entry_54.grid(row=5,column=9)

Label_57 = tk.Checkbutton(quantitative_display, text="52W High:", width=11, anchor=tk.W)
Label_57.grid(row=6, column=8)
entry_55 = tk.Entry(quantitative_display, width=8)
entry_55.grid(row=6,column=9)

Label_58 = tk.Checkbutton(quantitative_display, text="52W Low:", width=11, anchor=tk.W)
Label_58.grid(row=7, column=8)
entry_56 = tk.Entry(quantitative_display, width=8)
entry_56.grid(row=7,column=9)

Label_59 = tk.Checkbutton(quantitative_display, text="RSI (14):", width=11, anchor=tk.W)
Label_59.grid(row=8, column=8)
entry_57 = tk.Entry(quantitative_display, width=8)
entry_57.grid(row=8,column=9)

Label_60 = tk.Checkbutton(quantitative_display, text="Rel Volume:", width=11, anchor=tk.W)
Label_60.grid(row=9, column=8)
entry_58 = tk.Entry(quantitative_display, width=8)
entry_58.grid(row=9,column=9)

Label_61 = tk.Checkbutton(quantitative_display, text="Avg Volume:", width=11, anchor=tk.W)
Label_61.grid(row=10, column=8)
entry_59 = tk.Entry(quantitative_display, width=8)
entry_59.grid(row=10,column=9)

Label_62 = tk.Checkbutton(quantitative_display, text="Volume:", width=11, anchor=tk.W)
Label_62.grid(row=11, column=8)
entry_60 = tk.Entry(quantitative_display, width=8)
entry_60.grid(row=11,column=9)

#Column 6-------------------------------------------------------------------------------------------
Label_63 = tk.Checkbutton(quantitative_display, text="Perf Week:", width=11, anchor=tk.W)
Label_63.grid(row=0, column=10)
entry_61 = tk.Entry(quantitative_display, width=8)
entry_61.grid(row=0,column=11)

Label_64 = tk.Checkbutton(quantitative_display, text="Perf Month:", width=11, anchor=tk.W)
Label_64.grid(row=1, column=10)
entry_62 = tk.Entry(quantitative_display, width=8)
entry_62.grid(row=1,column=11)

Label_65 = tk.Checkbutton(quantitative_display, text="Perf Quarter:", width=11, anchor=tk.W)
Label_65.grid(row=2, column=10)
entry_63 = tk.Entry(quantitative_display, width=8)
entry_63.grid(row=2,column=11)

Label_66 = tk.Checkbutton(quantitative_display, text="Perf Half Y:", width=11, anchor=tk.W)
Label_66.grid(row=3, column=10)
entry_64 = tk.Entry(quantitative_display, width=8)
entry_64.grid(row=3,column=11)

Label_67 = tk.Checkbutton(quantitative_display, text="Perf Year:", width=11, anchor=tk.W)
Label_67.grid(row=4, column=10)
entry_65 = tk.Entry(quantitative_display, width=8)
entry_65.grid(row=4,column=11)

Label_68 = tk.Checkbutton(quantitative_display, text="Perf YTD:", width=11, anchor=tk.W)
Label_68.grid(row=5, column=10)
entry_66 = tk.Entry(quantitative_display, width=8)
entry_66.grid(row=5,column=11)

Label_69 = tk.Checkbutton(quantitative_display, text="Beta:", width=11, anchor=tk.W)
Label_69.grid(row=6, column=10)
entry_67 = tk.Entry(quantitative_display, width=8)
entry_67.grid(row=6,column=11)

Label_70 = tk.Checkbutton(quantitative_display, text="ATR:", width=11, anchor=tk.W)
Label_70.grid(row=7, column=10)
entry_68 = tk.Entry(quantitative_display, width=8)
entry_68.grid(row=7,column=11)

Label_71 = tk.Checkbutton(quantitative_display, text="Volatility:", width=11, anchor=tk.W)
Label_71.grid(row=8, column=10)
entry_69 = tk.Entry(quantitative_display, width=8)
entry_69.grid(row=8,column=11)

Label_72 = tk.Checkbutton(quantitative_display, text="Prev Close:", width=11, anchor=tk.W)
Label_72.grid(row=9, column=10)
entry_70 = tk.Entry(quantitative_display, width=8)
entry_70.grid(row=9,column=11)

Label_73 = tk.Checkbutton(quantitative_display, text="Price:", width=11, anchor=tk.W)
Label_73.grid(row=10, column=10)
entry_71 = tk.Entry(quantitative_display, width=8)
entry_71.grid(row=10,column=11)

Label_74 = tk.Checkbutton(quantitative_display, text="Change:", width=11, anchor=tk.W)
Label_74.grid(row=11, column=10)
entry_72 = tk.Entry(quantitative_display, width=8)
entry_72.grid(row=11,column=11)

#------------------------------------------------------------------------------------------------------------------------------------

#Screener function
def screener_decision(self):
    if selected_method1.get() == "-":
        user_choice2['state'] = tk.DISABLED
        user_choice2.set(user_choices_2[0])
        user_choice3['state'] = tk.DISABLED
        user_choice3.set(user_choices_3[0])
        user_choice4['state'] = tk.DISABLED
        user_choice4.set(user_choices_4[0])
        b1['state'] = tk.DISABLED
    if selected_method1.get() == "Ticker Symbol":
        user_choice2['state'] = tk.ACTIVE
        user_choice3['state'] = tk.DISABLED
        user_choice3.set(user_choices_3[0])
        user_choice4['state'] = tk.DISABLED
        b1['state'] = tk.DISABLED
        if selected_method2.get() != "-":
            user_choice4['state'] = 'readonly'
            if selected_method4.get() != "-":
                b1['state'] = tk.ACTIVE
    if selected_method1.get() == "Company Name":
        user_choice2['state'] = tk.DISABLED
        user_choice2.set(user_choices_2[0])
        user_choice3['state'] = tk.ACTIVE
        user_choice4['state'] = tk.DISABLED
        b1['state'] = tk.DISABLED
        if selected_method3.get() != "-":
            user_choice4['state'] = 'readonly'
            if selected_method4.get() != "-":
                b1['state'] = tk.ACTIVE

#Frame to hold screener in root windo
screener = tk.LabelFrame(root, text="Screener")
screener.grid(row=1, column=1)
#Grid configuration for screener by column
screener.grid_columnconfigure(0, weight=1)
screener.grid_columnconfigure(1, weight=1)

#Screener question 1
Label_75 = tk.Label(screener,text="Select By:", width=14, anchor=tk.NW)
Label_75.grid(row=0, column=0)
#Combobox for screener questioon one
user_choices_1 = ["-", "Ticker Symbol", "Company Name", "Country", "Sector", "Industry"]
selected_method1 = tk.StringVar(screener)
user_choice1 = ttk.Combobox(screener, textvariable=selected_method1, value=user_choices_1, width =13)
user_choice1.set(user_choices_1[0])
user_choice1.bind('<<ComboboxSelected>>', screener_decision)
user_choice1['state'] = 'readonly'
user_choice1.grid(row=0, column=1)


#Screener question 2
Label_76 = tk.Label(screener,text="Ticker Symbol:", width =14, anchor=tk.NW)
Label_76.grid(row=1, column=0)
#Combobox for screener question two
user_choices_2 = ["-"]

with open("nasdaq_screener_1630814001874.csv") as f:
    records = csv.DictReader(f)
    for row in records:
        user_choices_2.append(row['Symbol'])

selected_method2 = tk.StringVar(screener)
user_choice2 = AutocompleteCombobox(screener, textvariable=selected_method2, completevalues=user_choices_2, width =13)
user_choice2.set(user_choices_2[0])
user_choice2.bind('<<ComboboxSelected>>', screener_decision)
user_choice2.grid(row=1, column=1)
user_choice2['state'] = tk.DISABLED

#Screener question 3
Label_77 = tk.Label(screener,text="Company Name:", width = 14, anchor=tk.NW)
Label_77.grid(row=2, column=0)
#Combobox for screener question 3
user_choices_3 = ["-"]

with open("nasdaq_screener_1630814001874.csv") as f:
    records = csv.DictReader(f)
    for row in records:
        user_choices_3.append(row['Name'])

selected_method3 = tk.StringVar(screener)
user_choice3 = AutocompleteCombobox(screener, textvariable=selected_method3, completevalues=user_choices_3, width=13)
user_choice3.set(user_choices_3[0])
user_choice3.bind('<<ComboboxSelected>>', screener_decision)
user_choice3.grid(row=2, column=1)
user_choice3['state'] = tk.DISABLED

#Screener question 4
Label_78 = tk.Label(screener,text="Save:", width = 14, anchor=tk.NW)
Label_78.grid(row=3, column=0)
#Combobox for screener question 3
user_choices_4 = ["-", "Yes", "No"]
selected_method4 = tk.StringVar(screener)
selected_method4.set(user_choices_4[0])
user_choice4 = ttk.Combobox(screener, textvariable=selected_method4, value=user_choices_4, width=13)
user_choice4.set(user_choices_4[0])
user_choice4.bind('<<ComboboxSelected>>', screener_decision)
user_choice4.grid(row=3, column=1)
user_choice4['state'] = tk.DISABLED

#Screener question 5
b1 = tk.Button(screener,text="Find", width=2, command=activate_screener)
b1.grid(row=4, column=0)
b1['state'] = tk.DISABLED

#----------------------------------------------------------------------------------------------------------------------

root.mainloop()