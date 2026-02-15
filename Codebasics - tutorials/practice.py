# write a recursive function to print all elements in a list

books = ["Do Epic Shit,","The Metamorphosis,","The Almanack Of Naval Ravikant"]

def relist(index , books):
    if(index==2):
        return print(books[index])
    print(books[index] ,  end = " ")
    relist(index+1,books)

print(relist(0,books))
