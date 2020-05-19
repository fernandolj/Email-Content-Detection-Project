#! usr/bin/env bash

conda init bash

conda activate email-anomaly

spark-submit test_pyspark.py

