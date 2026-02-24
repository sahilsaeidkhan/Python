

detail = {}

with open("nyc_weather.csv","r") as weather:
     next(weather)

     for line in weather:
          parts = line.strip().split(',')
          date = parts[0]
          temperature = parts[1]
          detail[date] = temperature


print(detail["Jan 9"])
print(detail["Jan 4"])     




          




