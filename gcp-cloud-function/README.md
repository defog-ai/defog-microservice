# Deploying as a serverless function on Google Cloud Run

## Adding your API key and database credentials
Add your API key and DB credentials in the `main.py` file

## Deploying as a serverless function
Just run the following line in your command prompt and you will be ready to go!

```
gcloud functions deploy test-defog \
--gen2 \
--runtime=python310 \
--region=us-central1 \
--source=. \
--entry-point=hello_http \
--trigger-http \
--allow-unauthenticated
```