### Homework 1: Docker, SQL and Terraform

#### Question 1. What's the version of pip in the python:3.13 image?

Run a container in interactive mode with the desired version of Python.

```sh
docker run -it --entrypoint=bash python:3.13
```

In the container shell run `pip --version`.

#### Question 2. Given the docker-compose.yaml, what is the hostname and port that pgadmin should use to connect to the postgres database?

Run `docker compose up` in the directory with `docker-compose.yaml`.

Containers with PostgreSQL and pgAdmin are running in the same network. Сonnect to the database via pgAdmin and find out that service name (`db`) and `container_name` both work as `hostname` for the db connection in pgAdmin.

---


#### Upload taxi trips data to the database

1. Build docker image with ingesting python script, requirements, and wget using `Dockerfile` is in current directory.

```sh
docker build -t taxi_trips_data_upload:v001 .
```

2. Create docker network for the correct operation of the PostgreSQL container and the data ingesting container.

```sh
docker network create pg-network
```

3. Create an environment variable with data URL for convenience.

```sh
URL="https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet"
```

4. Run PostgreSQL container.

```sh
docker run -it \
    -e POSTGRES_USER="postgres" \
    -e POSTGRES_PASSWORD="postgres" \
    -e POSTGRES_DB="postgres" \
    -v $(pwd)/postgres_data:/var/lib/postgresql/data \
    -p 5432:5432 \
    --network=pg-network \
    --name pg-database \
    postgres:17-alpine
```

5. Run data ingesting container.

```sh
docker run -it \
    --network=pg-network \
    taxi_trips_data_upload:v001 \
    --user=postgres \
    --password=postgres \
    --host=pg-database \
    --port=5432 \
    --db=postgres \
    --table_name=trips \
    --url=${URL}
```

6. Save file with zones.

```sh
wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv
```

And upload zones dictionary using script `upload_zones.py`.

---

#### Question 3. For the trips in November 2025, how many trips had a trip_distance of less than or equal to 1 mile?

```sql
select
    count(1)
from trips
where 1=1
    and lpep_pickup_datetime::date >= '2025-11-01'
    and lpep_pickup_datetime::date < '2025-12-01'
    and trip_distance <= 1
```

#### Question 4. Which was the pick up day with the longest trip distance? Only consider trips with trip_distance less than 100 miles.

```sql
select
    lpep_pickup_datetime::date as pick_up_date,
    trip_distance
from trips
where 1=1
    and lpep_pickup_datetime::date >= '2025-11-01'
    and lpep_pickup_datetime::date < '2025-12-01'
    and trip_distance <= 100
order by trip_distance desc
;
```

#### Question 5. Which was the pickup zone with the largest total_amount (sum of all trips) on November 18th, 2025?

```sql
select
    zones."Zone",
    sum(total_amount) as total_amount
from trips
    left join zones
        on trips."PULocationID" = zones."LocationID"
where 1=1
    and lpep_pickup_datetime::date = '2025-11-18'
group by zones."Zone"
order by total_amount desc
;
```

#### Question 6. For the passengers picked up in the zone named "East Harlem North" in November 2025, which was the drop off zone that had the largest tip?

```sql
select
    doz."Zone",
    tip_amount
from trips
    left join zones as puz
        on trips."PULocationID" = puz."LocationID"
    left join zones as doz
        on trips."DOLocationID" = doz."LocationID"
where 1=1
    and trips.lpep_pickup_datetime::date >= '2025-11-01'
    and trips.lpep_pickup_datetime::date < '2025-12-01'
    and puz."Zone" = 'East Harlem North'
order by tip_amount desc
;
```

#### Question 7. Which of the following sequences describes the Terraform workflow for: 1) Downloading plugins and setting up backend, 2) Generating and executing changes, 3) Removing all resources?**

terraform init, terraform apply -auto-approve, terraform destroy
