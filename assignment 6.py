 def ds():
#     name={"Saanvi singh"}
#     rollno={31}
#     print("Name:",name,"\n","Rollno:",rollno)
#     print("Name:",type(name),"\n","Rollno:",type(rollno))


# name1=["Tiara kabara"]
# rollno1=[14]
# print("Name:",name1,"\n","Rollno:",rollno1)
# print("Name:",type(name1),"\n","Rollno:",type(rollno1))

# dict={
#     "Name":"Kanak Rai",
#     "Rollno":"39"
#     }
# print(dict["Name"])
# print(dict)
# print(type(dict),type(dict))

# ds()

def ds():
    name=input("Enter Your Name:")
    rollno=int(input("Enter Your Rollno:"))
#list
    ls=[name,rollno]
    print(ls)
    print(type(ls))
    print(ls)
#dicitonary
    dict={
    "Name":name,
    "Rollno":rollno
}
    print(dict["Name"])
    print(dict["Rollno"])
    print(type(dict))
#set
    s={name,rollno}
    print(s)
    print(type(s))
#tuple
    t=(name,rollno)
    print(t)
    print(type(t))

    del ls
    del dict
    del s
    del t
ds()