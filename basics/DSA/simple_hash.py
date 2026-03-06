class Hashtable:
    def __init__(self):
       self.size = 10
       self.table = [[]for _i in range(self.size)]

    def hashfunction(self,key):
        return key%self.size
    
    def insert(self,key):
        index = self.hashfunction(key)
        self.table[index].append(key)
    
    def search(self,key):
        index = self.hashfunction(key)
        return key in self.table[index]


h1 = Hashtable()

h1.insert(50)
h1.insert(30)
h1.insert(67)
h1.insert(15)
h1.insert(25)
h1.insert(45)

print(h1.search(50))
print(h1.search(45))