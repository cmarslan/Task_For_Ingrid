import requests
import json

from src.Enums import Alterable


class HandleFirstData(object):
    source_to_first_destination = requests.get(
        'http://router.project-osrm.org/route/v1/driving/' + Alterable.SOURCE_LOCATION.value + ';' + Alterable.FIRST_DESTINATION.value + '?overview=false').json()

    handle_json = json.dumps(source_to_first_destination)

    first_destination_data = json.loads(handle_json)

    first_destination_duration = (first_destination_data["routes"][0]["duration"])

    first_destination_distance = (first_destination_data["routes"][0]["distance"])

    first_destination_code = (first_destination_data["code"])
