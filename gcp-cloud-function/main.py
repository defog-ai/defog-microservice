import functions_framework
from defog import Defog
import json

defog = Defog(
    api_key = "YOUR_API_KEY",
    db_type = "YOUR_DB_TYPE",
    db_creds = "YOUR_DB_CREDS"
)

@functions_framework.http
def hello_http(request):
    # Set CORS headers for the preflight request
    if request.method == 'OPTIONS':
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }
        return ('', 204, headers)

    # Set CORS headers for the main request
    headers = {
        'Access-Control-Allow-Origin': '*'
    }
    request_json = request.get_json(force=True)
    question = request_json.get('question')
    hard_filters = request_json.get('hard_filters')
    previous_context = request_json.get('previous_context')
    
    if not previous_context:
        previous_context = []

    answer = defog.run_query(question, previous_context=previous_context, hard_filters=hard_filters)
    answer = json.dumps(answer, default=str)
    # this is a dictionary with the keys `columns`, `data`, `previous_context`, `generate_query`, `is_successful`, `reason_for_query`, `suggestion_for_further_questions`
    return (answer, 200, headers)
