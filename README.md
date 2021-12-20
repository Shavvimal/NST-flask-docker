In a terminal, run the following command to build the Docker image:
`docker build -f Dockerfile -t recog_container:api .`

Run container in background and print container ID using:
`docker run -p 5000:5000 -d recog_container:api`

Once this is running, you should be able to view your app running in your browser at http://localhost:5000/upload


`pip install -r ./requirements.txt`

`python upload.py`

