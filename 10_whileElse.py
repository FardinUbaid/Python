iteration = 100

while iteration < 100:
    if(iteration % 2 ==0):
        print(str(iteration)+" is an even number.")
    else:
        print(str(iteration) + " is an odd number.")
    iteration+=1        #iteration = iteration + 1
else:
    print("I'm out of the loop now!")