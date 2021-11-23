In a terminal, run the following command to build the Docker image:
`docker build -f Dockerfile -t recog_container:api .`

Run container in background and print container ID using:
`docker run -p 5000:5000 -d recog_container:api`

