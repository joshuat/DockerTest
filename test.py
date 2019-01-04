import sys
import random
import numpy
from pyspark.sql import SparkSession
from pyspark import SparkContext


print("Hello from python!")
print("Python version is:", sys.version)
print()
print("Numpy version:", numpy.__version__)


def inside(p):
    x, y = random.random(), random.random()
    return x*x + y*y < 1


sc = SparkContext()

spark = SparkSession.builder.appName('test app').getOrCreate()

spark.sql('show tables').show()

NUM_SAMPLES = 1000
count = sc.parallelize(range(0, NUM_SAMPLES)) \
             .filter(inside).count()
print("Pi is roughly %f" % (4.0 * count / NUM_SAMPLES))