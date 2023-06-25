var=input("Enter the Varaiale:")
value=ord(var)
print("ASCII value of your variable is :",ord(var))
print("Variable value of ASCII Number is :",chr(value))


value=int(input("Enter the value of Alcohol drunked by the Driver:"))
if (value<=40):
     pass
     print("The driver has less rate of Alcohol consumption")
else:
     print("The driver has high rate of Alcohol consumption",value)


for num in range(1,2,1):
    age = int(input("enter age="))
    if age<18:
        print("Under 18")
        break
    if age>18 and age <60:
        print("Above 18")
        continue
while age>18 and age<60:
    print("Eligible to vote")
    break
else:
    print("Not eligible to vote")