# Start up

## Without Docker compose
docker build -t fastapi-image .

docker run --name fastapi-container -p 80:80 -d -v $(pwd):/code fastapi-image

## Docker Compose
docker compose up -d

###
turn off with docker compose down

### Update
docker compose --build -d

# IDLE setup
install Docker and Dev Containers extensions
Attach to running container
Select /code folder
Install dependencies

