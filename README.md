# Basic Docker ML Exercise

## Overview
Learn to containerize a simple ML application that:
1. Trains a model on iris dataset, and saves it in model directory
2. Uses a Gradio Interface for developing user friendly UI
3. Dockerizes the application

## Project Structure
```
basic-ml-docker/
├── Dockerfile
├── requirements.txt
├── app/
│   ├── train.py
│   ├── main.py
│   └── model/
│       └── .gitkeep
└── README.md
```

## Tasks
1. Install requirements using pip
2. Run the training script to train the model and save it inside model directory
3. Write code in main.py file to develop a UI using Gradio
4. Create a Docker image for this application
5. Start a Docker container and make predictions


## Step-by-Step Instructions

### Task 1: Install requirements using pip
1. Required libraries are mentioned in requirements.txt
2. Install this libraries

### Task 2: Run the training script to train the model and save it inside model directory
1. Run training script
2. Verify model creation
3. Check training logs
4. Model should be saved after the script execution

### Task 3: Write code in main.py file to develop a UI using Gradio
1. Load the trained model
2. Create input, output components
3. View predictions

### Task 4: Create a Docker image for this application
1. Dockerize the application
2. Create a Docker image

### Task 5: Start a Docker container and make predictions
1. Start a Docker container
2. Access the running application and make predictions
