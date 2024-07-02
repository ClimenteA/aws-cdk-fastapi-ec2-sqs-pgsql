from locust import HttpUser, task, between


# Run with locust -f locust.py
# Make sure to change IP
# In UI on HOST add: http://3.76.216.129/
class LogsAPI(HttpUser):
    wait_time = between(5, 9)

    @task
    def perform_post_request(self):
        payload = {"level": "DEBUG", "message": "string"}
        url = "http://localhost:3000/v1/save-log-sync"
        self.client.post(url, json=payload)
