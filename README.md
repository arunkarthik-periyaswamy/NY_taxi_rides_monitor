# NY Taxi Rides Monitor
A robust, end-to-end machine learning project for monitoring and predicting New York City taxi ride demand. This repository covers data ingestion, feature engineering, model training, inference pipelines, and interactive frontends-enabling real-time insights and analytics for NYC taxi rides.

# About
NY Taxi Rides Monitor is designed to help analyze, visualize, and predict NYC taxi ride patterns using advanced data science and MLOps workflows. The project includes data pipelines, Jupyter notebooks for experimentation, model training scripts, and frontend dashboards for monitoring predictions.

# Features
Automated Data Pipelines: Fetch, process, and transform raw taxi data.

Model Training & Inference: Baseline and advanced models (XGBoost, LightGBM) with retraining support.

Feature Engineering: Modular feature pipelines for robust model input.

Interactive Frontend: Dashboards for real-time monitoring and visualization.

MLOps Ready: CI/CD workflows, Docker, and environment management.

# Directory Structure

arunkarthik-periyaswamy-ny_taxi_rides_monitor/
├── anaconda-ubuntu/         # Docker setup for reproducible environments
├── data/                    # Raw data files
├── frontend/                # Frontend dashboard scripts
├── notebooks/               # Jupyter notebooks for data exploration & modeling
├── pipelines/               # Model training and inference pipelines
├── src/                     # Source code and utilities
├── test/, tests/            # Sample and unit tests
├── .github/workflows/       # CI/CD pipeline definitions
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
Quickstart
Clone the repo:


git clone https://github.com/arunkarthik-periyaswamy/ny_taxi_rides_monitor.git
cd ny_taxi_rides_monitor
Install dependencies:


pip install -r requirements.txt
Explore notebooks or run pipelines:

Open Jupyter notebooks in the notebooks/ folder for step-by-step analysis.

Use scripts in pipelines/ and src/ for automated workflows.
