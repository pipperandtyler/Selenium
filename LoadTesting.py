"""
# This code contains the test locust example using Locust and Json.
from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(0, 1.5)

    @task
    def hello_world(self):
        self.client.get("/admin/business-client-list/")
        self.client.get("/admin/field-worker-edit-personal/396186/")
        # self.client.get("example.com")

    def on_start(self):
        # self.client.post("https://staging.propcert.co.uk/my-admin", json={"username": "faisal", "password": "Dlogic123!"})
        response = self.client.post("/my-admin/", data={"username": "faisal", "password": "Dlogic123!"})
        print("Response status code:", response.status_code)
        print("Response text:", response.text)
        response = self.client.get("/admin/business-client-list/")
"""

from locust import User, task, constant, events
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


class WebdriverExample(User):
    wait_time = constant(0.25)
    host = "https://staging.propcert.co.uk/my-admin"

    def __init__(self, environment):
        #chrome_options = Options()
        #chrome_options.add_argument("--disable-extensions")
        #chrome_options.add_argument("--disable-gpu")
        #chrome_options.add_argument("--headless")
        #super().__init__(environment)
        #self.driver = webdriver.Chrome("C:\chromedriver", options=chrome_options)
        self.driver = webdriver.Chrome("C:\chromedriver")

    def on_stop(self):
        self.driver.close()

    @task
    def home(self):
        start_at = time.time()
        self.driver.get(self.host)
        elem = self.driver.find_element_by_name("username")
        elem.clear()
        elem.send_keys("faisal")
        elem = self.driver.find_element_by_name("password")
        elem.clear()
        elem.send_keys("Dlogic123!")
        elem.send_keys(Keys.RETURN)

