# with open("weather_data.csv") as file:
#      data = file.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as file:
#     data=csv.reader(file)
#     # print(data)
#     temperatures=[]
#     for item in data:
#         temperatures.append(item[1])
#     temperatures.remove("temp")
#     for n in range(len(temperatures)):
#         temperatures[n]=int(temperatures[n])
# print(temperatures)
import pandas
# data=pandas.read_csv("weather_data.csv")
# new_data=data.to_dict()
# print(new_data)
# print(type(data))
# temp=data["temp"].to_list()
# print(temp)

# print(data["temp"].mean())
# print(data[data.temp==data.temp.max()])


data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels=len(data[data["Primary Fur Color"]=="Gray"])
cinnamon_squirrels=len(data[data["Primary Fur Color"]=="Cinnamon"])
black_squirrels=len(data[data["Primary Fur Color"]=="Black"])
print(grey_squirrels)
print(cinnamon_squirrels)
print(black_squirrels)

data_dict={
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels, cinnamon_squirrels, black_squirrels]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")