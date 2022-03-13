from pyspark.sql import SparkSession
spark = SparkSession.builder.master('local').getOrCreate()

# word count program to count the occurence of each word in a text file
sc = spark.SparkContext
readFile = sc.textFile(r'path').flatMap(lambda x:x.split(' ')).map(lambda x:(x,1)).reduceByKey(lambda x,y:x+y)
readFile.collect()
