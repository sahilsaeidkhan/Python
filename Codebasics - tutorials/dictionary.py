countries =  {"China": 143 , "India": 120 , "USA": 43, "Pakistan": 14}

for i in range(4):
  ask = input("Enter your input").lower()
  if ask == "print":
    for country, population in countries.items():
       print(f"{country}==>{population}")

  elif( ask == "add"):
    ask2 = input("Enter Country name to add")
    if ask2 in countries:
      print("Country Already exist")
    else:
      ask3 = int(input("Enter Population for the country"))
      countries[ask2] = ask3

  elif ( ask == "remove"):
    ask4 = input("Enter Country name to remove")
    if ask4 in countries:
      del countries[ask4]
      print(countries)
    else:
      print("Countries doesn't exist")

  elif ask == "query":
    query = input("query for which country")
    if query in countries:
     print(countries["query"])
    else:
      print("Country doesn't exist")
