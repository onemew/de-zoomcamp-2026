# Homework 3: Data Warehouse


#### Prerequisies

1. Setup a local analytics engineering environment using DuckDB and dbt.

2. Load the Green and Yellow taxi data for 2019-2020 into a local warehouse: run `python data-ingestion.py` in the `taxi_rides_ny` directory.

3. Run `dbt build --target prod` to create all models and run tests.

4. Load the FHV data for 2019 into a local warehouse:
- modify `data-ingestion.py`
- run `python data-ingestion.py` in the taxi_rides_ny directory
- add source for FHV-data into `models/staging/sources.yaml`
- run `dbt build --target prod --select stg_fhv_tripdata` to create a model


#### Question 1. dbt run --select int_trips_unioned builds which models?

Run `dbt run --select int_trips_unioned` in the `taxi_rides_ny` directory.

#### Question 2. New value 6 appears in payment_type. What happens on dbt test?

Add test in `models/marts/schema.yml` and run `dbt test --select fct_trips`.

#### Question 3. Count of records in fct_monthly_zone_revenue?

```sql
select count(1) from prod.fct_monthly_zone_revenue;
```

#### Question 4. Zone with highest revenue for Green taxis in 2020?

```sql
select
    pickup_zone
from prod.fct_monthly_zone_revenue
where service_type = 'Green'
    and year(revenue_month) = 2020
order by revenue_monthly_total_amount desc
limit 1;
```

#### Question 5. Total trips for Green taxis in October 2019?

```sql
select
    sum(total_monthly_trips) as total_monthly_trips
from prod.fct_monthly_zone_revenue
where service_type = 'Green'
    and DATE_TRUNC('month', revenue_month) = '2019-10-01 00:00:00.000'
;
```

#### Question 6. Count of records in stg_fhv_tripdata (filter dispatching_base_num IS NULL)?

```sql
select count(1) from prod.stg_fhv_tripdata;
```
