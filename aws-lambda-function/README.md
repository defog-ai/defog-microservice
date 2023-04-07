# Deploying as a serverless function on AWS Lambda

## Adding your API key and database credentials
Add your API key and DB credentials in the `app.py` file

## Deploying as a serverless function
1. Install `chalice` with `pip install chalice`
2. Create a `chalice` project using `chalice new-project defog-lambda`
3. Inside the `defog-lambda` directory, replace `app.py` with the `app.py` file in this directory.
4. Copy and paste the `requirements.txt` file from this directory to the `defog-lambda` directory
5. Run `chalice deploy`. Your microservice is now live!
6. Optionally, enable CORS by going to your API gateway
