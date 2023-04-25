from chalice import Chalice
app = Chalice(app_name='defog-demo')

from defog import Defog
import json

defog = Defog(
    api_key = "YOUR_API_KEY",
    db_type = "YOUR_DB_TYPE",
    db_creds = "YOUR_DB_CREDS"
)

@app.route('/', methods=['POST'])
def answer():
    # This is the JSON body the user sent in their POST request.
    query = app.current_request.json_body
    question = query['question']
    hard_filters = query.get('hard_filters')
    answer = defog.run_query(question, hard_filters=hard_filters)
    answer = json.dumps(answer, default=str)
    return answer
