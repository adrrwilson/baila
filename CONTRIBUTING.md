# Contributing

## How to build the Dockerfile

```
docker build -t IMAGE_NAME .
```

## How to run the Dockerfile Locally 

```
docker run -dp 5000:5000 -w /app -v "$(pwd):/app" IMAGE_NAME sh -c
```

## Run using Docker Compose

```
docker compose up
```


## How to run the App Locally 

```
flask run --host 0.0.0.0
```