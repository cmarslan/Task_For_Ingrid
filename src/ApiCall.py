import requests
import json

response = requests.get(
    'http://your-service/routes?src=13.388860,52.517037&dst=13.397634,52.529407&dst=13.428555,52.523219').json()

handle_json = json.dumps(response)

load_json = json.loads(handle_json)

r = load_json

source_location = (r["source"])

first_destination_location = (r["routes"][0]["destination"])

second_destination_location = (r["routes"][1]["destination"])

# command


# mk kadir