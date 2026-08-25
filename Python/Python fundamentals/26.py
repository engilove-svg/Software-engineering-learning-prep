temp=int(input("Enter the temperature: "))
if(temp<0):
    print("Freezing")
elif(temp<=15):
    print("Cold")
elif(temp<=25):
    print("Comfortable")
else:
    print("Hot")