# 2019-CS316-CapitalOne-Email-Content-Anomaly-Detection

## Requirements
- Install Anaconda version 4.7.12
- Install Python version 3.7.4
- Install Spark specifically PySpark inside Anaconda version 2.4.3
- Install Scala version 2.11.12

## Environment Setup
- Install above
- Use environment.yml file to create env:`conda env create -f environment.yml`

## Enter the Environment
- cd into the Scripts folder
- run the command `source run.sh` or `. run.sh` which will then enter you into the conda environment

## Features and Modeling
- source code located in featuresudf branch in the SRC folder
- to prepare environment run source ./start.sh

## Dataset Evaluation/Generation
- source code located in dataset_evaluation branch Dataset Evaluation folder

## Dataset
- script to get dataset in current directory is located in the dataset_evaluation branch in the Data folder

## Steps
- Do environment setup
- Enter the environment
- Download dataset
- Move dataset into same directory as code for modeling (SRC/spark) or update path to dataset
- run start.sh script in SRC/spark folder
- Run model
