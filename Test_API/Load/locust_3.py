from locust import HttpUser, task, between, tag
import os

class QuickUserTest(HttpUser):
    wiat_time = between(1,5) # between 1 to 5 s
    host = "https://www.baidu.com"

    @task
    @tag("task1")
    def hello_world1(self):
        self.client.get("/hello")

    @task(3)
    @tag("task2")
    def hello_world2(self):
        self.client.get("/world")

    @task(3)
    @tag("task3")
    def hello_world3(self):
        self.client.get("/world1")



if __name__=="__main__":
    os.system("locust -f locust_2.py --headless -u 100 -r 10 -7 1m --html report.html --tags task1 task2")