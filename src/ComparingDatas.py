from src.First_Destination_Datas import HandleFirstData
from src.Second_Destination_Datas import HandleSecondData


class CompareData(object):
    first_distance = HandleFirstData.first_destination_distance
    second_distance = HandleSecondData.second_destination_distance
    first_duration = HandleFirstData.first_destination_duration
    second_duration = HandleSecondData.second_destination_duration
    first_destination_best_option = []
    second_destination_best_option = []
    if first_duration < second_duration:
        first_destination_best_option.append(first_duration)
        first_destination_best_option.append(first_distance)
    elif second_duration < first_duration:
        second_destination_best_option.append(second_duration)
        second_destination_best_option.append(second_distance)
    elif first_distance < second_distance:
        first_destination_best_option.append(first_duration)
        first_destination_best_option.append(first_distance)
    else:
        second_destination_best_option.append(second_duration)
        second_destination_best_option.append(second_distance)
