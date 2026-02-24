detail = {}

with open("poem.txt","r") as file:

    for line in file:
         words = line.split()
        
         for word in words:
           word = word.lower()
           word.strip(".,!?;:\"'")
           if word in detail:
            detail[word] += 1
           else:
            detail[word] = 1

print(detail)
