from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import string
import random

count = 1
while count:
    print("Test case number: " + str(count))
    # producing a random string for test data creation
    N = random.randint(20, 40)
    Name = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=N))

    O = random.randint(11, 40)
    name = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=O))

    Email = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=O))
    Email = Email + '@gmail.com'

    Number = ''.join(random.choices(string.digits, k=O))
    driver = webdriver.Chrome('C:\chromedriver')
    driver.maximize_window()
    driver.get("http://52.211.207.33/")
    driver.find_element_by_xpath('/html/body/header/div/nav/div/ul/li[5]/button').click()
    opt = random.randint(2, 40)
    opt = str(opt)
    driver.find_element_by_xpath("//option[" + opt + "]").click()
    wait = WebDriverWait(driver, 50)
    elm = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/section/div/div/div/div[1]/div["
                                                               "2]/select/option[2]")))
    elm.click()
    driver.find_element_by_xpath("html/body/div[3]/section/div/div/div/div[1]/div[3]/button").click()
    if count % 2 == 0:
        elm = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/section/div[1]/div/div[1]/div["
                                                                   "1]/div/div[1]/div/div/h5")))
        elm.click()
        elm = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/section/div[1]/div/div["
                                                                   "3]/div/div/div[1]/h5")))
        elm.click()
    else:
        elm = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/section/div[1]/div/div[1]/div["
                                                                   "2]/div/div[1]/div/div/h5")))
        elm.click()
        elm = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/section/div[1]/div/div[3]/div["
                                                                   "1]/div/div[1]/h5")))
        elm.click()
        elm = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/section/div[1]/div/div[3]/div["
                                                                   "2]/div/div[1]/h5")))
        elm.click()

    driver.find_element_by_xpath("//button[text()=' Next Step ']").click()
    #elm = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()=' Next Step ']")))
    #elm.click()
    opt = random.randint(2, 5)
    opt = str(opt)
    elm = wait.until(
        EC.presence_of_element_located((By.XPATH, ("/html/body/div[3]/section/div/div/div[1]/div[1]/div/div["
                                                   "1]/div/div/div/select/option[" + opt + "]"))))
    elm.click()
    driver.find_element_by_xpath("/html/body/div[3]/section/div/div/div[1]/div[1]/div/div[2]/div/input").send_keys(Name)
    driver.find_element_by_xpath("/html/body/div[3]/section/div/div/div[1]/div[1]/div/div[3]/div/input").send_keys(name)
    driver.find_element_by_xpath("/html/body/div[3]/section/div/div/div[1]/div[1]/div/div[4]/div/input").send_keys(Email
                                                                                                                   )
    driver.find_element_by_xpath("/html/body/div[3]/section/div/div/div[1]/div[1]/div/div[5]/div/input").send_keys(
        Number)
    driver.find_element_by_xpath("/html/body/div[3]/section/div/div/div[1]/div[1]/div/div[7]/div/div/input").send_keys(
        "212E")
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[3]/section/div/div/div[1]/div[1]/div/div[7]/div/div/input").click()
    act = ActionChains(driver)
    act.send_keys(Keys.ARROW_DOWN * 3)
    act.perform()
    act.send_keys()
    act = ActionChains(driver)
    act.send_keys(Keys.RETURN)
    act.perform()
    act.send_keys()
    time.sleep(2)
    driver.find_element_by_xpath("//button[text()='Next Step ']").click()
    if count % 2 == 0:
        elm = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/section/div/div/ul/li[1]/p/i")))
        elm.click()
        driver.find_element_by_xpath("/html/body/div[3]/section/div/div/ul/li[1]").click()
        driver.find_element_by_xpath("//button[text()=' Continue ']").click()
        elm = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/section/div[1]/div/ul/li[1]")))
        elm.click()
    else:
        elm = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/section/div/div/ul/li[2]/p/i")))
        elm.click()
        driver.find_element_by_xpath("//button[text()=' Continue ']").click()
        elm = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/section/div/div/ul/li[1]/p/i")))
        elm.click()
        elm = wait.until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/section/div[1]/div/ul/li[2]/p/i")))
        elm.click()
        F = random.randint(500, 1000)
        s = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=F))
        elm = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/section/div/div/textarea")))
        elm.send_keys(s)
        elm = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()=' Continue ']")))
        elm.click()
    driver.find_element_by_xpath("//button[text()=' Payment ']").click()
    elm = wait.until(EC.presence_of_element_located(
        (By.XPATH, "/html/body/section/div[2]/form/div[1]/div/div[2]/div/div/div[2]/input")))
    elm.send_keys("4976000000003436")
    driver.find_element_by_xpath(
        "/html/body/section/div[2]/form/div[1]/div/div[2]/div/div/div[3]/div/div[1]/select/option[13]").click()
    driver.find_element_by_xpath(
        "/html/body/section/div[2]/form/div[1]/div/div[2]/div/div/div[3]/div/div[2]/select/option[2]").click()
    driver.find_element_by_xpath(
        "/html/body/section/div[2]/form/div[1]/div/div[2]/div/div/div[4]/div/div[1]/input").send_keys("452")
    driver.find_element_by_xpath("//button[text()[normalize-space()='Make Payment']]").click()
    time.sleep(0.20)
    count = count + 1
    driver.quit()
