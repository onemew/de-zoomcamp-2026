### Homework 2: Workflow Orchestration

#### Prerequisies

Run `docker compose up -d` in the directory with `docker-compose.yaml`.

In Kestra UI:
- create flow `04_postgres_taxi.yaml` from file `04_postgres_taxi.yaml`
- execute the flow for particular taxi type, year and month


#### Question 1. Within the execution for Yellow Taxi data for the year 2020 and month 12: what is the uncompressed file size (i.e. the output file yellow_tripdata_2020-12.csv of the extract task)?

Note, that 1 MiB = 1024 bytes to the power of 2.


#### Question 2. What is the rendered value of the variable file when the inputs taxi is set to green, year is set to 2020, and month is set to 04 during execution?

Substitute specific values into a string template `{{inputs.taxi}}_tripdata_{{inputs.year}}-{{inputs.month}}.csv`.


#### Question 3. How many rows are there for the Yellow Taxi data for all CSV files in the year 2020?

Run query:

```sql
select count(1)
from public.yellow_tripdata
where filename in (
	'yellow_tripdata_2020-01.csv',
	'yellow_tripdata_2020-02.csv',
	'yellow_tripdata_2020-03.csv',
	'yellow_tripdata_2020-04.csv',
	'yellow_tripdata_2020-05.csv',
	'yellow_tripdata_2020-06.csv',
	'yellow_tripdata_2020-07.csv',
	'yellow_tripdata_2020-08.csv',
	'yellow_tripdata_2020-09.csv',
	'yellow_tripdata_2020-10.csv',
	'yellow_tripdata_2020-11.csv',
	'yellow_tripdata_2020-12.csv'
)
;
```

#### Question 4. How many rows are there for the Green Taxi data for all CSV files in the year 2020?

Run query:

```sql
select count(1)
from public.yellow_tripdata
where filename in (
	'green_tripdata_2020-01.csv',
	'green_tripdata_2020-02.csv',
	'green_tripdata_2020-03.csv',
	'green_tripdata_2020-04.csv',
	'green_tripdata_2020-05.csv',
	'green_tripdata_2020-06.csv',
	'green_tripdata_2020-07.csv',
	'green_tripdata_2020-08.csv',
	'green_tripdata_2020-09.csv',
	'green_tripdata_2020-10.csv',
	'green_tripdata_2020-11.csv',
	'green_tripdata_2020-12.csv'
)
;
```

#### Question 5. How many rows are there for the Yellow Taxi data for the March 2021 CSV file?

Run query:

```sql
select count(1)
from public.yellow_tripdata
where filename = 'yellow_tripdata_2021-03.csv'
```


#### Question 6. How would you configure the timezone to New York in a Schedule trigger? 

Use the TZ identifier (also known as the IANA Time Zone database name). The benefit of using this specific string rather than a manual offset (like -5) is that Kestra will automatically handle Daylight Saving Time (DST) changes.
