#we import sleep class from time module
from time import sleep,strftime
#we import webdriver class from selenium
from selenium import webdriver
#we import keys from selenium.webdriver.common.keys
from selenium.webdriver.common.keys import Keys
#we import the randint from random
from random import randint
#we import pandas as pd its used to explore data sets
#import pandas as pd
#from the webdriver class we call the firefox function and whatever is 
# is returned is stored in a 
# variable called browser
from selenium.webdriver.common.action_chains import ActionChains
browser = webdriver.Firefox()
#the browser waits for 5 seconds
browser.implicitly_wait(5)


#to open the url stated 
browser.get('http://0.0.0.0:8000/')

sleep(randint(10,15))

#Click leadership
login_link = browser.find_element_by_xpath("/html/body/div[2]/a[2]/p")
#and then click it
login_link.click()

sleep(randint(10,12))

#Go back Home
go_back_home = browser.find_element_by_xpath("/html/body/div[2]/a[1]")
go_back_home.click()
sleep(randint(12,16))

#Go to parents
go_to_parents = browser.find_element_by_xpath("/html/body/div[2]/a[3]/p")
go_to_parents.click()
sleep(randint(11,15))

#Go back home
parents_go_back_home = browser.find_element_by_xpath("/html/body/div/a[1]")
parents_go_back_home.click()
sleep(randint(14,16))

#Go to children
go_to_children = browser.find_element_by_xpath("/html/body/div[2]/a[4]/p")
go_to_children.click()
sleep(randint(13,15))

#Go back home
children_go_back_home = browser.find_element_by_xpath("/html/body/div/a[1]")
children_go_back_home.click()
sleep(randint(10,14))

#go_to_register
go_to_register = browser.find_element_by_xpath("/html/body/div[2]/a[5]/p")
go_to_register.click()
sleep(randint(15,17))

#register_go_home
register_go_home = browser.find_element_by_xpath("/html/body/div[2]/a[1]/p")
register_go_home.click()
sleep(randint(13,15))

#go_to_payments
go_to_payments = browser.find_element_by_xpath("/html/body/div[2]/a[6]/p")
go_to_payments.click()
sleep(randint(14,15))

#go_back_home_payments
go_back_home_payments = browser.find_element_by_xpath("/html/body/div/a[1]")
go_back_home_payments.click()

