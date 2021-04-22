import time
from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def hello_world(self):
        # self.client.get("https://staging.propcert.co.uk/admin/business-client-list")
        # self.client.get("https://staging.propcert.co.uk/admin/business-client-edit-detail/396171")
        self.client.get("example.com")

    def on_start(self):
        # self.client.post("https://staging.propcert.co.uk/my-admin", json={"username": "faisal", "password": "Dlogic123!"})
        self.client.get("")
