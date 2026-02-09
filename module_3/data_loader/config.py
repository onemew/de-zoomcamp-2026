BUCKET_NAME = "dezc_m3"

CREDENTIALS_FILE = "gcs.json"

BASE_URL = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-"

DOWNLOAD_DIR = "."

CHUNK_SIZE = 8 * 1024 * 1024

MONTHS = [f"{i:02d}" for i in range(1, 7)]
