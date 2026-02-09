# Homework 3: Data Warehouse 

#### Prerequisies

Load date via `data loader`.

Create external table referring to GCS path:
```sql
CREATE OR REPLACE EXTERNAL TABLE `project.dezc_m3.external_yellow_tripdata`
OPTIONS (
  format = 'parquet',
  uris = ['gs://dezc_m3/yellow_tripdata_2024-*.parquet']
);
```

Create materialized table:
```sql
CREATE OR REPLACE TABLE `project.dezc_m3.yellow_tripdata`
```

#### Question 1. What is count of records for the 2024 Yellow Taxi Data?

```sql
SELECT COUNT(1)
FROM `project.dezc_m3.external_yellow_tripdata`
```

#### Question 2. What is the estimated amount of data that will be read when this query is executed on the External Table and the Table?

```sql
SELECT COUNT(DISTINCT PULocationID) 
FROM `project.dezc_m3.external_yellow_tripdata`

SELECT COUNT(DISTINCT PULocationID) 
FROM `project.dezc_m3.yellow_tripdata`
```

#### Question 3. Why are the estimated number of Bytes different?

```sql
SELECT PULocationID 
FROM `project.dezc_m3.yellow_tripdata`

SELECT PULocationID, DOLocationID 
FROM `project.dezc_m3.yellow_tripdata`
```

#### Question 4. How many records have a fare_amount of 0?

```sql
SELECT COUNT(1)
FROM `project.dezc_m3.yellow_tripdata`
WHERE fare_amount = 0;
```

#### Question 5. What is the best strategy to make an optimized table in Big Query if your query will always filter based on tpep_dropoff_datetime and order the results by VendorID?

```sql
CREATE OR REPLACE TABLE `project.dezc_m3.opimized_yellow_tripdata`
PARTITION BY DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID AS
SELECT * FROM `project.dezc_m3.yellow_tripdata`;

```

#### Question 6. Write a query to retrieve the distinct VendorIDs between tpep_dropoff_datetime 2024-03-01 and 2024-03-15 (inclusive). Use the materialized table you created earlier in your from clause and note the estimated bytes. Now change the table in the from clause to the partitioned table you created for question 5 and note the estimated bytes processed. What are these values?

```sql
SELECT DISTINCT VendorID
FROM `project.dezc_m3.opimized_yellow_tripdata`
WHERE TIMESTAMP_TRUNC(tpep_dropoff_datetime, DAY) BETWEEN '2024-03-01' AND '2024-03-15'
;
```
