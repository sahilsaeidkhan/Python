def area(b,h):
    triangle = 1/2 * b * h
    return triangle

base = int(input("Enter base : "))
height = int(input("Enter height : "))

print(area(base,height))





















def pattern(n):
  for i in range(n+1):
    for j in range(i):
        print("*", end="")
    
    print()

i = int(input("Enter number to print pattern :"))
pattern(i)


















