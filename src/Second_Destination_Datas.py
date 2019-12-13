import requests
import json

from src.Enums import Alterable


class HandleSecondData(object):
    source_to_second_destination = requests.get(
        'http://router.project-osrm.org/route/v1/driving/' + Alterable.SOURCE_LOCATION.value + ';' + Alterable.SECOND_DESTINATION.value + '?overview=false').json()

    handle_json = json.dumps(source_to_second_destination)

    second_destination_data = json.loads(handle_json)

    second_destination_duration = (second_destination_data["routes"][0]["duration"])

    second_destination_distance = (second_destination_data["routes"][0]["distance"])

    second_destination_code = (second_destination_data["code"])
