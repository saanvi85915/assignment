#Arithimetic operator

a=10
b=5
print("Adding A + B:",a+b)
print("Subtracting A - B:",a-b)
print("Multiplying A * B:",a*b)
print("Divide A / B:",a/b)
print("Modulus A % B:",a%b)
print("Floor Division A // B:",a//b)
print("Exponential A ** B:",a**b)

#Comparison Operator

a=int(input("Enter A:"))
b=int(input("Enter B:"))

if a<b:
    print("B is largest Number than A")
if a>b:
    print("A is largest Number than B")
if a==b:
    print("Both Number are same")

#Assignment Operator

a+=1
print("+=",a)
a=10
a-=1
print("-=",a)
a=10
a*=1
print("*=",a)
a=10
a/=1
print("/=",a)
a=10
a**=1
print("**=",a)
a=10
a//=1
print("//=",a)
a=10
a%=1
print("%=",a)

#Logical Operator
a=True
b=False
print("and",a and b)
print("or",a or b)
print("not",not b)
# bitwise operators
print("bitwise &",a&b)
print("bitwise |",a|b)
print("bitwise ^",a^b)
print("bitwise >>",a>>b)
print("bitwise <<",a<<b)

# identity operator
print("is",a is b)
print("is not",a is not b)

#Membership operator

Name="Saanvi"
print("a" in Name)
print("s" not in Name)