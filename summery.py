print ("---------------------------------------------")
print ("# Summation program")
print ("# Type 'exit'to end the Program")
print ("---------------------------------------------")


sumdata=0
count=0

while True:
    sum=input(f" Enter Number {count}:")
    if sum=="exit":
        break
    sumdata +=int(sum)
    count=count+11
print (f"Total :{sumdata}")

