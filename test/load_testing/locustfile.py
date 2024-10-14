from locust import HttpUser, TaskSet, task, between
from dotenv import load_dotenv
import os
import random
from pathlib import Path

load_dotenv(Path(os.getcwd()) / "api/.env")


class UserBehavior(TaskSet):

    @task
    def classify_iris(self):
        # Define the headers to match your curl request
        headers = {
            "accept": "application/json",
            "X-Access-Token": os.getenv("API_KEY"),
            "Content-Type": "application/json"
        }

        # Define the JSON body to match your curl request
        json_data = {
            "sepal_length": random.randint(1, 25),
            "sepal_width": random.randint(1, 25),
            "petal_length": random.randint(1, 25),
            "petal_width": random.randint(1, 25)
        }

        # Perform POST request to the /classify_iris endpoint
        self.client.post("/classify_iris", json=json_data, headers=headers)


class IrisAPIUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 3)  # wait time between requests
