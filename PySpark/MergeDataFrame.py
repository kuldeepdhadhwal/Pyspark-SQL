from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

#Create DataFrame df1 with columns name,dept & age
data = [("James","Sales",34), ("Michael","Sales",56), \
    ("Robert","Sales",30), ("Maria","Finance",24) ]
columns= ["name","dept","age"]
df1 = spark.createDataFrame(data = data, schema = columns)
df1.printSchema()

#Create DataFrame df1 with columns name,dep,state & salary
data2=[("James","Sales","NY",9000),("Maria","Finance","CA",9000), \
    ("Jen","Finance","NY",7900),("Jeff","Marketing","CA",8000)]
columns2= ["name","dept","state","salary"]
df2 = spark.createDataFrame(data = data2, schema = columns2)
df2.printSchema()

def merge_df(df1,df2):
    from pyspark.sql.function import lit
    for column in [column for column in df2.columns if column not in df1.columns]:
        df1 = df1.withColumn(column, lit(None))
    return df1

first_df = merge_df(df1,df2)
second_df = merge_df(df2,df1)

merged_df=first_df.unionByName(second_df)
merged_df.show()
