from validator import validate
email=input("Enter Email Address :-\n")
data={"email":email}
res={"email":"required|mail"}
result=validate(data,res)
if result == True:
    print(f"You email is Vaild {email}")
else:
    print(f"You email is not Vaild {email}")
