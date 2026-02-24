class HashChaining:
    def __init__(self,size):
        self.size = size
        self.table = [[] for _i in range(self.size)]

    def Hashfunction(self,key):
        return key%self.size
    
    def insert(self,key):
        index = self.Hashfunction(key)
        self.table[index].append(key)

    def search(self,key):
        index = self.Hashfunction(key)
        return key in self.table[index]
    
    def delete(self,key):
        index = self.Hashfunction(key)
        self.table[index].remove(key)

h1 = HashChaining(10)

h1.insert(45)
h1.insert(34)
h1.insert(465)
h1.insert(334)

print(h1.table)

h1.delete(34)
print(h1.table)

print(h1.search(334))