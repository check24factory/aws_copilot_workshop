# aws_copilot_workshop
Mastering ML Deployment: Utilizing AWS ECS Copilot for Scalable Inference Solutions

## Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Setup Instructions API](#setup-instructions-api)
- [Training the Model](#training-the-model)
- [Deploying with FastAPI](#deploying-with-fastapi)
- [ RUN and test the API](#run-and-test-the-api)
- [Project Structure](#project-structure)

### Introduction
--draft-- \
In this workshop, you will learn how to deploy a machine learning
model using FastAPI, containerize the application with Docker,
and deploy it to AWS ECS. AWS ECS allows you to easily run and
manage Docker containers on a cluster of EC2 instances or 
using AWS Fargate, a serverless compute engine for containers.

### Requirements
--draft-- \
- Python 3.12+

### Setup Instructions API
--draft-- \
1. Clone the repository
```bash
git clone ###
cd aws_copilot_workshop
```

### Training the Model
--draft-- \
```python
# training.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# ---  Load Data ---
iris_df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',
                 header=None,
                 names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# --- Prepare DATA ---
label_encoder = LabelEncoder()
iris_df['class'] = label_encoder.fit_transform(iris_df['class'])

# Split features and labels
X = iris_df.drop('class', axis=1)
y = iris_df['class']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- Train Model ---
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Initialize and train the model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# -- Save Model --
import joblib

SAVE_PATH = 'model_dir'

# Save the model to a file
model_filename = 'iris_model.pkl'
joblib.dump(model, f'{SAVE_PATH}/{model_filename}')
print(f"💾 Model saved to {model_filename}")

# Save the label encoder to a file
label_encoder_filename = 'label_encoder.pkl'
joblib.dump(label_encoder, f'{SAVE_PATH}/{label_encoder_filename}')
print(f"💾 Label encoder saved to {label_encoder_filename}")
```

### Deploying with FastAPI
--draft-- \
MAYBE MORE TO THE TOP

### RUN and test the API
--draft-- \
1. using container locally

```bash
#❕ Should be executed from the root of the project ❕

# build and run docker, and start the FastAPI server
make api_serve

# YOU MAY NEED TO CHANGE THE URL
curl -X 'POST' 'http://0.0.0.0:8000/classify_iris' \
  -H 'accept: application/json' \
  -H 'X-Access-Token: 1234' \
  -H 'Content-Type: application/json' \
  -d '{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}'
```

2. Using server locally 
```bash
# 1. switch inside the api directory
cd api
# 2. Create and activate a virtual environment
python3.12 -m venv .venv
source $(pwd)/.venv/bin/activate
# 3. Install dependencies
pip install -r requirements.api.txt
# 4. Start the FastAPI server Locally
cd .. # main project root
uvicorn api.application:APP --port 8000 --reload
# 5. Test the API
curl -X 'POST' 'http://127.0.0.1:8000/classify_iris' \
  -H 'accept: application/json' \
  -H 'X-Access-Token: 1234' \
  -H 'Content-Type: application/json' \
  -d '{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}'
```

### Locust
--draft-- \
test api_locally
```bash
# create a network
docker network create iris-network

# start api locally
docker build -t iris-api .
docker run --name iris-api --network iris-network -p 8000:8000 iris-api

# start locust locally
docker run -p 8089:8089 \                                                                                                                                   ok | aws_copilot_workshop py | 18:31:51
           -v $PWD/test/load_testing:/mnt/locust \
           --name iris-locust \
           --network iris-network \
           locustio/locust -f /mnt/locust/locustfile.py

```

test hosted api
```bash
docker ps -q --filter "name=iris-locust" | grep -q . && docker stop iris-locust
docker build -t custom-locust -f Dockerfile.locust . && \
docker run -p 8089:8089 \
           -v $PWD/test/load_testing:/mnt/locust \
           --name iris-locust-new \
           --network iris-network \
           custom-locust -f /mnt/locust/locustfile.py
```