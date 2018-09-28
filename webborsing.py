
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import numpy as np
import matplotlib

global_delay_time = 0.12
# =============================================================================
# utility functions -- ignore
# =============================================================================
def print_timer (count_secs):
    for i in range (count_secs):
        print(count_secs - i)
        time.sleep (1)
        
def select_proj_scen ():
    time.sleep(global_delay_time)
    elem = driver.find_element_by_id("about-scenario")
    elem.click()
    
def add_week ():
    time.sleep(global_delay_time)
    elem = driver.find_element_by_class_name('btn.plus')
    elem.click()
    
def minus_week ():
    time.sleep(global_delay_time)
    elem = driver.find_element_by_class_name('btn.minus')
    elem.click()
    
def add_worker ():
    time.sleep(global_delay_time)
    elem = driver.find_element_by_class_name('btn.plus')
    elem.click()
    
def minus_worker ():
    time.sleep(global_delay_time)
    elem = driver.find_element_by_class_name('btn.plus')
    elem.click()
    
def minus_one2one ():
    time.sleep(global_delay_time)
    elem = driver.find_element_by_class_name("btn.minus")
    elem.click()
    
def plus_one2one ():
    time.sleep(global_delay_time)
    elem = driver.find_element_by_class_name ("btn.plus")
    elem.click()
    
def minus_daily ():
    time.sleep(global_delay_time)
    elems = [e for e in driver.find_elements_by_class_name("btn.minus")]
    elems[1].click()
    
def plus_daily ():
    time.sleep(global_delay_time)
    elems = [e for e in driver.find_elements_by_class_name("btn.plus")]
    elems[1].click()
    
def minus_stat ():
    time.sleep(global_delay_time)
    elems = [e for e in driver.find_elements_by_class_name("btn.minus")]
    elems[2].click()
    
def plus_stat ():
    time.sleep(global_delay_time)
    elems = [e for e in driver.find_elements_by_class_name("btn.plus")]
    elems[2].click()
    
def plus_proto ():
    time.sleep(global_delay_time)
    elem = driver.find_element_by_class_name('btn.plus')
    elem.click()
    
def minus_proto ():
    time.sleep(global_delay_time)
    elem = driver.find_element_by_class_name('btn.plus')
    elem.click()
    
# =============================================================================
# Useful functions -- dont ignore    
# =============================================================================

def play_now ():
    time.sleep(global_delay_time)
    elem = driver.find_element_by_id("play-now")
    elem.click()
    
def select_model (model):
    time.sleep(global_delay_time)
    elem = driver.find_element_by_id("scope-widget")
    elem.click()
    
    time.sleep(global_delay_time)
    model = "scope-level-" + str(model)
    elem = driver.find_element_by_id(model)
    elem.click()
    
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
            add_week()
        if (curr_week > week):
            minus_week ()
        if (curr_week == week):
            time.sleep(global_delay_time)
            driver.find_element_by_class_name ("tab-button.close.green").click()
            return
            
    
# quality and outsourcing : 1 <-> 4
def team_characteristics (num_workers, quality, outsourcing):
    
    
    time.sleep(global_delay_time)
    elem = driver.find_element_by_id("resources-widget")
    elem.click()
    
    # configure workers
    while True:
        time.sleep(global_delay_time)
        curr_num_workers = int(driver.find_element_by_class_name("value").text)
        
        if (curr_num_workers < num_workers):
            add_worker ()
        if (curr_num_workers > num_workers):
            minus_week()
        if (curr_num_workers == num_workers):
            break
        
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
    except:
        print ("Error with changing outsourcing")
    
    # exit menu screen
    time.sleep(global_delay_time)
    driver.find_element_by_class_name ("tab-button.close.orange").click()
 

def meetings_overtime (one2one, daily, stat, over):
        
    time.sleep(global_delay_time)
    elem = driver.find_element_by_class_name("tab-button.open.purple")
    elem.click()
    
    one21_str = "/html/body/div/div/div/div/div/div/div/div/div/table/tbody/tr/td/span/span[1]"
    time.sleep(global_delay_time)
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
    

def set_prototypes (num):
    time.sleep(global_delay_time)
    elem = driver.find_element_by_class_name("tab-button.open.red")
    elem.click()
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

driver = webdriver.Firefox()
driver.get('https://hbsp.harvard.edu/coursepacks/561410')

#assert 'facebook' in browser.title

elem = driver.find_element_by_name("email")
elem.clear()
elem.send_keys('barberal@tcd.ie' + Keys.TAB + 'pass!' + Keys.RETURN)

print_timer (20)

#open tab
#driver.execute_script("window.open('https://forio.com/simulate/harvard/project-management/simulation/#prepare');")


# =============================================================================
# PREPARE SCREEN
# =============================================================================

driver.get('https://forio.com/simulate/harvard/project-management/simulation/#prepare')
time.sleep(2.5)
play_now ()
select_model (4)
select_week (13)
team_characteristics(8,3,3)
meetings_overtime (3,2,1,3)
set_prototypes (5)
