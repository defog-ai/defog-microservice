from chalice import Chalice
app = Chalice(app_name='defog-demo')

from defog import Defog

defog = Defog(
    api_key = "DEFOG_API_KEY",
    db_type = "YOUR_DB_TYPE",
    db_creds = YOUR_DB_CREDS
)

@app.route('/', methods=['POST'])
def answer():
    # This is the JSON body the user sent in their POST request.
    query = app.current_request.json_body
    answer = defog.run_query(query['question'])
    # We'll echo the json body back to the user in a 'user' key.
    return answer
