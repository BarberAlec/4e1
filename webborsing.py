#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 siybul <siybul@siybul-Aspire-E5-553G>
#
# Distributed under terms of the MIT license.


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import numpy as np
import matplotlib
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

global_delay_time = 0.12
driver = webdriver.Firefox()
# =============================================================================
# utility functions -- ignore
# =============================================================================

#Generic count-down timer
def print_timer (count_secs):
    for i in range (count_secs):
        print(count_secs - i)
        time.sleep (1)
        
        
#These are super cheecky functions whose purpose is to retry any function if
#there was an error on the first attempt
def find_elem_id (strg):
    try:
        elem = driver.find_element_by_id(strg)
        return elem
    except:
        print ("failed elem_id, giving it another go: " + strg)
        driver.implicitly_wait(1.8)
        try:
            elem = driver.find_element_by_id(strg)
        except:
            print ("failed elem_id, giving it another go (round 2): " + strg)
            driver.implicitly_wait(1.8)
            elem = driver.find_element_by_id(strg)
        return elem

def find_elem_class (strg):
    try:
        elem = driver.find_element_by_class_name(strg)
        return elem
    except:
        print ("failed class, giving it another go: " + strg)
        driver.implicitly_wait(1.8)
        try:    
            elem = driver.find_element_by_class_name(strg)
        except:
            print ("failed class, giving it another go (round 2): " + strg)
            driver.implicitly_wait(1.8)
            elem = driver.find_element_by_class_name(strg)
        return elem

def find_elem_xpath (strg):
    try:
        elem = driver.find_element_by_xpath (strg)
        return elem
    except:
        print ("failed xpath, giving it another go: " + strg)
        driver.implicitly_wait(1.8)
        elem = driver.find_element_by_xpath (strg)
        return elem


        
# clicks an element for you...more reliably
def clicker (elem):
    try:
        clicker (elem)
    except:
        print ("click failed with elem: " + str(elem))
        driver.implicitly_wait(1.8)
        try:    
            clicker (elem)
        except:
            print ("click failed with elem (round 2): " + str(elem))
            driver.implicitly_wait(1.8)
            clicker (elem)

        
def select_proj_scen ():
    time.sleep(global_delay_time)
    elem = driver.find_element_by_id("about-scenario")
    elem.click()
    driver.implicitly_wait(1)
     
def plus_week ():
    time.sleep(global_delay_time)
    elem = driver.find_element_by_class_name('btn.plus')
    elem.click()
    driver.implicitly_wait(1)
     
def minus_week ():
    time.sleep(global_delay_time)
    elem = driver.find_element_by_class_name('btn.minus')
    elem.click()
    driver.implicitly_wait(1)
     
def plus_worker ():
    time.sleep(global_delay_time)
    elem = driver.find_element_by_class_name('btn.plus')
    elem.click()
    driver.implicitly_wait(1)
     
def minus_worker ():
    time.sleep(global_delay_time)
    elem = driver.find_element_by_class_name('btn.plus')
    elem.click()
    driver.implicitly_wait(1)
     
def minus_one2one ():
    time.sleep(global_delay_time)
    elem = driver.find_element_by_class_name("btn.minus")
    elem.click()
    driver.implicitly_wait(1)
     
def plus_one2one ():
    time.sleep(global_delay_time)
    elem = driver.find_element_by_class_name ("btn.plus")
    elem.click()
    driver.implicitly_wait(1)
     
def minus_daily ():
    time.sleep(global_delay_time)
    elems = [e for e in driver.find_elements_by_class_name("btn.minus")]
    elems[1].click()
    driver.implicitly_wait(1)
     
def plus_daily ():
    time.sleep(global_delay_time)
    elems = [e for e in driver.find_elements_by_class_name("btn.plus")]
    elems[1].click()
    driver.implicitly_wait(1)
     
def minus_stat ():
    time.sleep(global_delay_time)
    elems = [e for e in driver.find_elements_by_class_name("btn.minus")]
    elems[2].click()
    driver.implicitly_wait(1)
       
def plus_stat ():
    time.sleep(global_delay_time)
    elems = [e for e in driver.find_elements_by_class_name("btn.plus")]
    elems[2].click()
    driver.implicitly_wait(1)
       
def plus_proto ():
    time.sleep(global_delay_time)
    elem = driver.find_element_by_class_name('btn.plus')
    elem.click()
    driver.implicitly_wait(1)
       
def minus_proto ():
    time.sleep(global_delay_time)
    elem = driver.find_element_by_class_name('btn.plus')
    elem.click()
    driver.implicitly_wait(1)
    
    
    
# =============================================================================
# Useful functions -- dont ignore    
# =============================================================================

#Clicks Play Now button on home screen
def play_now ():
    time.sleep(global_delay_time)
    elem = driver.find_element_by_id("play-now")
    elem.click()

#Selects which model you want (model : 1,2,3,4)  
def select_model (model):
    time.sleep(global_delay_time)
    elem = driver.find_element_by_id("scope-widget")
    elem.click()
    
    time.sleep(global_delay_time)
    model = "scope-level-" + str(model)
    elem = driver.find_element_by_id(model)
    elem.click()

#Selects which week you want to target as your finish week (week : 1 -> 25)
def select_week (week):
    curr_week = int(driver.find_element_by_class_name("text-xxbig").text)
    
    time.sleep(global_delay_time)
    elem = driver.find_element_by_id("schedule-widget")
    elem.click()
    
    if (curr_week == week):
        return
    
    while True:
        time.sleep(global_delay_time)
        curr_week = int(driver.find_element_by_class_name("value").text)
        
        if (curr_week < week):
            plus_week()
        if (curr_week > week):
            minus_week ()
        if (curr_week == week):
            time.sleep(global_delay_time)
            driver.find_element_by_class_name ("tab-button.close.green").click()
            return
            
    
# Slect Characteristics of your team (num_workers : 1 -> 10, quality/outsourcing : 1 -> 4)
def team_characteristics (num_workers, quality, outsourcing):
    
    
    time.sleep(global_delay_time*2)
    elem = driver.find_element_by_id("resources-widget")
    elem.click()
    driver.implicitly_wait(1) 
    # configure workers
    while True:
        time.sleep(global_delay_time)
        curr_num_workers = int(driver.find_element_by_class_name("value").text)
        
        if (curr_num_workers < num_workers):
            plus_worker ()
        if (curr_num_workers > num_workers):
            minus_worker()
        if (curr_num_workers == num_workers):
            break
        
    #configure quality
    time.sleep(global_delay_time*2)
    if quality == 1:
        quality_str = "Basic"
        input_str = "//*[contains(text(), '" + quality_str + "')]"
        try:
            driver.find_elements_by_xpath(input_str)[0].click ()
            for i in range(4):
                try:
                    run_test = WebDriverWait(driver, 120).until( \
                    EC.presence_of_element_located((By.XPATH, "xpath")))
                    run_test.click()
                    break
                except StaleElementReferenceException as e:
                    raise e
        except:
             print ("Error with changing quality")
    
    
    if quality == 2:
        quality_str = "Medium"
        input_str = "//*[contains(text(), '" + quality_str + "')]"
        try:
            driver.find_elements_by_xpath(input_str)[0].click ()
            for i in range(4):
                try:
                    run_test = WebDriverWait(driver, 120).until( \
                    EC.presence_of_element_located((By.XPATH, "xpath")))
                    run_test.click()
                    break
                except StaleElementReferenceException as e:
                    raise e
        except:
                print ("Error with changing quality")
    
    
    if quality == 3:
        quality_str = "Medium-High"
        input_str = "//*[contains(text(), '" + quality_str + "')]"
        try:
            driver.find_elements_by_xpath(input_str)[0].click ()
            for i in range(4):
                try:
                    run_test = WebDriverWait(driver, 120).until( \
                    EC.presence_of_element_located((By.XPATH, "xpath")))
                    run_test.click()
                    break
                except StaleElementReferenceException as e:
                    raise e
        except:
                print ("Error with changing quality")
    
    
    if quality == 4:
        quality_str = "High"             
        input_str = "//*[contains(text(), '" + "High" + "')]"        
        try:
            driver.find_elements_by_xpath(input_str)[3].click ()
        except:
                print ("Error with changing quality")
                
        #Useful code to debug HIGH quality button when it stops working...
# =============================================================================
#         count = 0
#         for i in elem:
#             try:
#                 count += 1
#                 i.click()
#             except:
#                 print ("elem: " + str(count) + "did not work")
# =============================================================================
    
    
    #configure outsoucing
    if outsourcing == 1:
        outsourcing_str = "None"
    if outsourcing == 2:
        outsourcing_str = "Support Tasks"
    if outsourcing == 3:
        outsourcing_str = "Some Primary Tasks"
    if outsourcing == 4:
        outsourcing_str = "Extensive"
    
    time.sleep(global_delay_time*2)
    input_str = "//*[contains(text(), '" + outsourcing_str + "')]"
    try:
        driver.find_elements_by_xpath(input_str)[0].click ()
        driver.implicitly_wait(1)
    except:
        print ("Error with changing outsourcing")
    
    # exit menu screen
    time.sleep(global_delay_time)
    driver.find_element_by_class_name ("tab-button.close.orange").click()

#Honestly Not sure why this is here... will ignore for now...
def team_characteristics_startup (quality, outsourcing):
    
    time.sleep(global_delay_time)
    elem = driver.find_element_by_id("resources-widget")
    elem.click()
    
    # configure workers
       
    #configure quality
    time.sleep(global_delay_time)
    if quality == 1:
        quality_str = "Basic"
        input_str = "//*[contains(text(), '" + quality_str + "')]"
        try:        #for onsome bizare reason, this does work but still throws an excepti
            driver.find_elements_by_xpath(input_str)[0].click ()
        except:
                print ("Error with changing quality")
    if quality == 2:
        quality_str = "Medium"
        input_str = "//*[contains(text(), '" + quality_str + "')]"
        try:        #for onsome bizare reason, this does work but still throws an excepti
            driver.find_elements_by_xpath(input_str)[0].click ()
        except:
                print ("Error with changing quality")
    if quality == 3:
        quality_str = "Medium-High"
        input_str = "//*[contains(text(), '" + quality_str + "')]"
        try:        #for onsome bizare reason, this does work but still throws an excepti
            driver.find_elements_by_xpath(input_str)[0].click ()
        except:
                print ("Error with changing quality")
    if quality == 4:
        quality_str = "High"
        #input_str = "//span/"
        elem = driver.find_elements_by_xpath ("//*[contains(text(), '" + quality_str + "')]")
        try:        #for onsome bizare reason, this does work but still throws an excepti
            elem[4].click()
        except:
                print ("Error with changing quality")
    
    
    
    #configure outsoucing
    if outsourcing == 1:
        outsourcing_str = "None"
    if outsourcing == 2:
        outsourcing_str = "Support Tasks"
    if outsourcing == 3:
        outsourcing_str = "Some Primary Tasks"
    if outsourcing == 4:
        outsourcing_str = "Extensive"
    
    time.sleep(global_delay_time)
    input_str = "//*[contains(text(), '" + outsourcing_str + "')]"
    try:
        driver.find_elements_by_xpath(input_str)[0].click ()
        driver.implicitly_wait(1)
    except:
        print ("Error with changing outsourcing")
    
    # exit menu screen
    time.sleep(global_delay_time)
    driver.find_element_by_class_name ("tab-button.close.orange").click()
    driver.implicitly_wait(1)

#Select Parametres for meetings overtime section (one2one/daily/stat : 0 -> 10, over : 0,1,2)
def meetings_overtime (one2one, daily, stat, over):
        
    time.sleep(global_delay_time*3)
    elem = driver.find_element_by_class_name("tab-button.open.purple")
    elem.click()
    driver.implicitly_wait(1)
    
    one21_str = "/html/body/div/div/div/div/div/div/div/div/div/table/tbody/tr/td/span/span[1]"
    time.sleep(global_delay_time*4)
    text_list = [e.text for e in driver.find_elements_by_xpath(one21_str)]

    #one2one
    while True:
        time.sleep(global_delay_time)
        curr_one2one = int(driver.find_element_by_xpath(one21_str).text)
        if (curr_one2one == one2one):
            break
        if (curr_one2one < one2one):
            plus_one2one ()
        if (curr_one2one > one2one):
            minus_one2one ()
    
    #daily standup
    while True:
        time.sleep (global_delay_time)
        text_list = [e.text for e in driver.find_elements_by_xpath(one21_str)]
        curr_daily = int(text_list[1])
        curr_daily = curr_daily//5
        if (curr_daily == daily):
            break
        if (curr_daily < daily):
            plus_daily ()
        if (curr_daily > daily):
            minus_daily ()
    
    #stat review
    while True:
        time.sleep (global_delay_time)
        text_list = [e.text for e in driver.find_elements_by_xpath(one21_str)]
        curr_stat = int(text_list[2])
        if (curr_stat == stat):
            break
        if (curr_stat < stat):
            plus_stat ()
        if (curr_stat > stat):
            minus_stat ()
    
    #overtime
    time.sleep (global_delay_time)
    if (over == 1):
        driver.find_element_by_class_name ("overtime-none").click ()
    if (over == 2):
        driver.find_element_by_class_name ("overtime-allowed.selected").click ()
    if (over == 3):
        driver.find_element_by_class_name ("overtime-encorage").click ()
    
    # exit menu screen
    time.sleep(global_delay_time)
    driver.find_element_by_class_name ("tab-button.close.purple").click()
    driver.implicitly_wait(1) 

#Set number of prototypes (limit is dependant on target week finish, but genaerally < 5)
def set_prototypes (num):
    time.sleep(global_delay_time)
    elem = driver.find_element_by_class_name("tab-button.open.red")
    elem.click()
    driver.implicitly_wait(1)
    while True:
        curr_proto = int(driver.find_element_by_class_name ("value").text)
        if (curr_proto != num):
            if (curr_proto < num):
                plus_proto ()
            if (curr_proto > num):
                minus_proto ()
        else:
            break
            
    time.sleep(global_delay_time)
    driver.find_element_by_class_name ("tab-button.close.red").click()

#Pass time by specified number of weeks (num_weeks : 0 -> inf)
def end_week (num_weeks):
    while True:
        time.sleep(global_delay_time)
        curr_week = int(driver.find_element_by_class_name ("value").text)
        if (curr_week == num_weeks):
            break
        if (curr_week < num_weeks):
            plus_week ()
        if (curr_week > num_weeks):
            minus_week ()
    
    #end week        
    time.sleep(global_delay_time)
    driver.find_element_by_id ("simulate").click ()
    
    time.sleep(global_delay_time)
    driver.find_element_by_class_name ("modal-action.affirmative.btn").click ()
    time.sleep(global_delay_time+2.5)

#Get rid of pop ups
def startup_affirm ():
    time.sleep(global_delay_time+2.5)
    driver.find_element_by_class_name ("modal-action.affirmative.btn").click ()
    time.sleep(global_delay_time+2.5)
      
    
def main (passw):
    driver.get('https://hbsp.harvard.edu/coursepacks/561410')
    
    
    elem = driver.find_element_by_name("email")
    elem.clear()
    elem.send_keys('barberal@tcd.ie' + Keys.TAB + passw + Keys.RETURN)
    
    print_timer (25)
    
    driver.get('https://forio.com/simulate/harvard/project-management/simulation/#prepare')
    time.sleep(2.5)
    play_now ()
    select_model (4)
    select_week (13)
    team_characteristics(6,4,4)
    meetings_overtime (3,2,1,3)
    set_prototypes (1)
    end_week (1)        #pass 5 weeks as thats when event happens
    
  



if __name__ == "__main__":
    passw = "enterpasshere"
    main (passw)
