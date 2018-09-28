
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
        input_str = "//input[@class='selector ' and @data-value='4']"
        try:        #for onsome bizare reason, this does work but still throws an excepti
            elem = driver.find_elements_by_xpath(input_str)[0]
            print (elem)
            elem.click()
        except:
                print ("Error with changing quality 5")
        
        try:        #for onsome bizare reason, this does work but still throws an excepti
            driver.find_elements_by_xpath(input_str)[1].click ()
        except:
                print ("Error with changing quality 6")
        
    
    
    
    #input_str = "//*[contains(text(), '" + quality_str + "')]"
    #print (driver.find_elements_by_xpath(input_str))
    
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
 


#def total_setup (model,week,num_workers,quality,outsourcing,one_c,d_stand,stat_rev,over_time,num_proto):
    
    
    

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
select_model (3)
select_week (20)
team_characteristics(6,4,2)

