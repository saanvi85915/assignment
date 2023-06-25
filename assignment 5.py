var = []
for i in range(0,5,1):
    n = int(input("Enter number = "))
    var.append(n)
print("List: \n",var)
print("Sum of all Numbers = ",sum(var))
print("Smallest number = ",min(var))
print("Biggest number = ",max(var))
var.sort()
print("Ascending = ",var)
var.reverse()
print("Descending = ",var)
var.sort()
print(tuple(var))
del var