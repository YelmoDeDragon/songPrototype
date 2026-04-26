# Build the Docker image
docker build -t song-search-app .
# Run the container
docker run -d -p 8000:8000 song-search-app