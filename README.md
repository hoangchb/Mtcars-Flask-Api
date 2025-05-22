# Mtcars-Flask-Api

This repo uses the **mtcars.csv** dataset predict mpg with a simple linear regression model. The model includes the following columns as predictors: `'cyl'`, `'disp'`, `'hp'`, `'drat'`, `'wt'`, `'qsec'`, `'vs'`, `'am'`, and `'gear'`.

We create a Flask API that runs locally inside a Docker container, push the image to DockerHub, and deploy the service on Google Cloud Run. 

## File Descriptions
- Dockerfile -- Defines the Docker image setup and environment for running the Flask API
- docker-compose.yml -- Builds and runs the app inside the Docker Container, port 5001 
- mtcars.csv -- mtcars dataset
- prediction.py -- Contains the simple lienar regression model to predict mpg
- requirements.txt -- Lists Python packages/libraries needed to run the API and model
- server.py -- Flask API server 

## Steps 
### Locally
1. Sync/clone this repo to pull the files. Open a new terminal in the same directory as the folder and run:\
`docker compose up -d`

2. Check to see if the localhost server was created successfully.\
`curl http://localhost:5001/`

    - This should print **"server  is up - nice job!"**

3. Run the following curl command to see the results.\
`curl -X POST http://localhost:5001/predict_price -H "Content-Type: application/json" -d '{"cyl": 8, "disp": 360, "hp": 175, "drat": 3.15, "wt": 3.44, "qsec": 17.02, "vs": 0, "am": 0, "gear": 3}`

    - This should print **"predicted mpg": 17.722366494548137**

### Google Cloud
1. Visit the url https://mtcars-flask-api-378985735322.us-central1.run.app/

    - You should see **"server  is up - nice job!"**

2. Run the following curl command to see the results.\
   `curl -X POST https://mtcars-flask-api-378985735322.us-central1.run.app/predict_price -H "Content-Type: application/json" -d '{"cyl": 8, "disp": 360, "hp": 175, "drat": 3.15, "wt": 3.44, "qsec": 17.02, "vs": 0, "am": 0, "gear": 3}'`

    - This should print **"predicted mpg": 17.722366494548137**

