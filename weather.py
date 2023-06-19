import csv
import shutil
# with open("weather.csv","r") as file:
#     data = list(csv.reader(file))
#
# city = input("Enter a city : ")
#
# for i in data[1:]:
#     if i[0] == city:
#         print(i[1])

shutil.make_archive("output","zip","files")