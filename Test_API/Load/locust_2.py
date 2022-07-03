from locust import HttpUser, task, between
import os

class QuickUserTest(HttpUser):
    wiat_time = between(1,5) # between 1 to 5 s
    host = "https://www.baidu.com"

    @task
    def hello_test(self):
        self.client.get("/hello")

if __name__=="__main__":
    os.system("locust -f locust_2.py -u 100 -r 10 ")