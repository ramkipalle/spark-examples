
from pyspark.sql import SparkSession



if __name__ == "__main__":

    # build spark session
    spark = SparkSession.builder.appName('Example1').getOrCreate()

    columns = ["name","languagesAtSchool","currentState"]
    data = [("James,Smith",["Java","Scala","C++"],"CA"), \
        ("Michael,Rose,",["Spark","Java","C++"],"NJ"), \
        ("Robert,Williams",["CSharp","VB", "Java"],"NV")]

    df = spark.createDataFrame(data=data,schema=columns)
    df.printSchema()
    df.show(truncate=False)

    spark.stop()


