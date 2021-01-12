# from locust import HttpUser, TaskSet, task
#
#
# # 定义用户行为
# class UserBehavior(TaskSet):
#
#     @task(1)
#     def test_login(self):
#         data={"account":"15811411759",
#               "password":"123456"}
#         res=self.client.post('http://dev.usercenter.imagicdatatech.com/user/login/accountLogin',data=data)
#         print(res.text)
#
#
# class WebsiteUser(HttpUser):
#     task_create = [UserBehavior]
#     host = 'http://dev.usercenter.imagicdatatech.com'
#     min_wait = 3000
#     max_wait = 6000
from locust import HttpUser, TaskSet, task


class ScriptTasks(TaskSet):
    def on_start(self):
        self.client.post("/login", {
            "username": "liuguiju",
            "password": "123456"
        })

    @task(2)
    def index(self):
        self.client.get("/")

    @task(1)
    def about(self):
        self.client.get("/about")

    @task(1)
    def demo(self):
        payload = {}
        headers = {}
        self.client.post("/demo", data=payload, headers=headers)


class WebsiteUser(HttpUser):
    tasks = [ScriptTasks]
    host = "http://127.0.0.1:8888"
    min_wait = 1000
    max_wait = 5000