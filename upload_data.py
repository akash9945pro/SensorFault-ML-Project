import pandas as pd
import json
from pymongo import MongoClient

# URL
uri = "mongodb+srv://acashTech:acashTech746@cluster0.apjn3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to server
client = MongoClient(uri)

# Create database name and collection name
DATABASE_NAME = "SensorData"
COLLECTION_NAME = 'waferfault'

# Read CSV file
df = pd.read_csv(r"C:\Users\akash\SensorProject\notebooks\wafer_23012020_041211.csv")

# Drop unnecessary column
df = df.drop("Unnamed: 0", axis=1)

# Convert dataframe to JSON records
json_records = df.to_dict(orient='records')

# Insert data in batches
batch_size = 100
for i in range(0, len(json_records), batch_size):
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_records[i:i+batch_size])