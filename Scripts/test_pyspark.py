import pyspark
sc = pyspark.SparkContext(appName="test_pyspark")
import random
NUM_SAMPLES = 1000
def inside(p):
 x, y = random.random(), random.random()
 return x*x + y*y < 1
count = sc.parallelize(range(0, NUM_SAMPLES)).filter(inside).count()
pi = 4 * count / NUM_SAMPLES
print()
print(pi)
print()
print("Pyspark is working")
print()
