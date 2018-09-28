
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import numpy as np
import matplotlib

global_delay_time = 0.1
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
    
    while True:
        time.sleep(global_delay_time)
        curr_num_workers = int(driver.find_element_by_class_name("value").text)
        
        if (curr_num_workers < num_workers):
            add_worker ()
        if (curr_num_workers > num_workers):
            minus_week()
        if (curr_num_workers == num_workers):
            time.sleep(global_delay_time)
            driver.find_element_by_class_name ("tab-button.close.orange").click()
            return
    
def total_setup (model,week,num_workers,quality,outsourcing,one_c,d_stand,stat_rev,over_time,num_proto):
    
    
    

driver = webdriver.Firefox()
driver.get('https://hbsp.harvard.edu/coursepacks/561410')

#assert 'facebook' in browser.title

elem = driver.find_element_by_name("email")
elem.clear()
elem.send_keys('barberal@tcd.ie' + Keys.TAB + 'mypassword' + Keys.RETURN)

print_timer (22)

#open tab
#driver.execute_script("window.open('https://forio.com/simulate/harvard/project-management/simulation/#prepare');")


# =============================================================================
# PREPARE SCREEN
# =============================================================================

driver.get('https://forio.com/simulate/harvard/project-management/simulation/#prepare')
time.sleep(2.5)
play_now ()
select_model (3)
select_week (20)
team_characteristics(6,1,1)

