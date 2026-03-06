# 1. nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
# i. What was the average temperature in first week of Jan
# ii. What was the maximum temperature in first 10 days of Jan

# Figure out data structure that is best for this problem

temperatures = []

with open("nyc_weather.csv","r") as file:
     next(file)

     for line in file:
          parts = line.strip().split(',')
          temp = int(parts[1])
          temperatures.append(temp)

# average temp 
sum = 0
for i in range(7):
     sum+=temperatures[i]

print(sum/7)


# max temp
first_ten = temperatures[:10]
max_temp = max(first_ten)
print(max_temp)


