# Variables
IMAGE_NAME= iris-fastapi-app
CONTAINER_NAME= iris-fastapi-container
PORT=8000
DOCKERFILE_PATH=./Dockerfile

# Build the Docker image from scratch
.PHONY: build
build:
	docker build -t $(IMAGE_NAME) -f $(DOCKERFILE_PATH) .

# Run the Docker container
.PHONY: run
run:
	docker run -p $(PORT):$(PORT) --name $(CONTAINER_NAME) $(IMAGE_NAME)

# Clean up by stopping and removing the container if it exists
.PHONY: clean
clean:
	@if [ $$(docker ps -a -q -f name=$(CONTAINER_NAME)) ]; then \
		docker stop $(CONTAINER_NAME); \
		docker rm $(CONTAINER_NAME); \
	fi

# View logs from the Docker container
.PHONY: logs
logs:
	docker logs -f $(CONTAINER_NAME)

# Serve the API (build, run, and follow logs)
.PHONY: api_serve
api_serve: clean build run