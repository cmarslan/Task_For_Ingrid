from src.ComparingDatas import CompareData

from src.First_Destination_Datas import HandleFirstData
from src.Second_Destination_Datas import HandleSecondData


def result():
    if not CompareData.first_destination_best_option:
        print("The Best Route ==> \nDuration Time (Minute) : {}\nDistance : {}".format(
            int(CompareData.second_destination_best_option[0] / 60), CompareData.second_destination_best_option[1]))
        CompareData.first_destination_best_option.append(HandleFirstData.first_destination_duration)
        CompareData.first_destination_best_option.append(HandleFirstData.first_destination_distance)
        print("Alternative Route ==> \nDuration Time (Minute) : {}\nDistance : {}".format(
            int(CompareData.first_destination_best_option[0] / 60), CompareData.first_destination_best_option[1]))
        CompareData.second_destination_best_option.append(HandleSecondData.second_destination_duration)
        CompareData.second_destination_best_option.append(HandleSecondData.second_destination_distance)
    elif not CompareData.second_destination_best_option:
        print("The Best Route ==> \nDuration Time (Minute) : {}\nDistance : {}".format(
            int(CompareData.first_destination_best_option[0] / 60), CompareData.first_destination_best_option[1]))
        CompareData.second_destination_best_option.append(HandleSecondData.second_destination_duration)
        CompareData.second_destination_best_option.append(HandleSecondData.second_destination_distance)
        print("Alternative Route ==> \nDuration Time (Minute) : {}\nDistance : {}".format(
            int(CompareData.second_destination_best_option[0] / 60), CompareData.second_destination_best_option[1]))
        CompareData.first_destination_best_option.append(HandleFirstData.first_destination_duration)
        CompareData.first_destination_best_option.append(HandleFirstData.first_destination_distance)


result()
