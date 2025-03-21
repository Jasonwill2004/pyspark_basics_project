from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, count

# Initialize a Spark session
spark = SparkSession.builder.appName("PySpark_CSV_Demo").getOrCreate()

# Load data from CSV file
df = spark.read.option("header", "true").csv("data.csv", inferSchema=True)

# Show the original data
print("Original Data:")
df.show()

# 1. Filter Data: Transactions where amount > 150
filtered_df = df.filter(col("amount") > 150)
print("Filtered Data (Amount > 150):")
filtered_df.show()

# 2. Group By & Aggregate: Total spending per customer
customer_spending = df.groupBy("customer").sum("amount")
print("Total Spending Per Customer:")
customer_spending.show()

# 3. Count Transactions Per Category
category_count = df.groupBy("category").agg(count("*").alias("transaction_count"))
print("Transaction Count Per Category:")
category_count.show()

# Stop Spark session
spark.stop()
