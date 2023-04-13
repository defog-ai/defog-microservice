from chalice import Chalice
app = Chalice(app_name='defog-demo')

from defog import Defog
import json

defog = Defog(
    api_key = "83d670e8f8702c988ed961ae0a17e3f79c02f886158b757d14f08e71296fc638",
    db_type = "postgres",
    db_creds = { "host": 'redshift-cluster-1.cbhvnw9silab.us-west-2.redshift.amazonaws.com', "port": 5439, "database": 'dev', "user": 'defoguser', "password": 'defog0xPass' }
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
