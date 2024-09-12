# return function tells code to stop function and sends the 
# function's result back to the caller!!

from statistics import mean
def temps(temp1, temp2, temp3):
    the_list = {temp1, temp2, temp3}
    avg = mean(the_list)
    return avg

avg1 = temps(10, 95, 1010)
avg2 = temps(20, 69, 4140)
avg3 = temps(30, 20, 505)
avg4 = temps(40, 249, 8)

print(avg1)
print(avg2)
print(avg3)
print(avg4)