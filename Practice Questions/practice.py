
# # 2. Find index of all the occurances of a number from sorted list

# # numbers = [1,4,6,9,11,15, 15, 15, 17, 21, 34, 34, 56]
# # number_to_find = 15

# # This should return 5,6,7 as indices containing number 15 in the array

# numbers = [1,4,6,9,11,15, 15, 15, 17, 21, 34, 34, 56]

# target = 15
# start = 0
# end = len(numbers) - 1
          
# while start<=end:
#     mid = start + ((end-start)//2)

#     if target > numbers[mid]:
#         start = mid + 1
#     elif target< numbers[mid]:
#         end = mid-1
#     else:
#         print("Found")
    


# print("Not found")
        















# def sum ( a = 3 , b=2):
#     return a+b

# print(sum())














# import time

# print("task started")
# time.sleep(2)

# print("Task 1 done")

# time.sleep(2)

# print("Task 2 done")




















# import multiprocessing
# import os

# def processid():
#     print("process id is " , os.getpid() )
      

# if __name__ == "__main__" :
#    p1 = multiprocessing.Process(target=processid)
#    p2 = multiprocessing.Process(target=processid)

#    p1.start()
#    p2.start()

#    p1.join()
#    p2.join()

# print("program ends")