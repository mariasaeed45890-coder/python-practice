print("===== simple calculator =====")

num1 =float(input("Enter first number:"))
operator =input("Emter operator(=.-,*,/):")
num2 =float(input("Enter second number:"))

if operator =="+":
    print("Answer:",num1+num2)
elif operator =="-":
    print("Answer:",num1-num2)
elif operator =="*":
    print("Answer:",num1*num2)
elif operator =="/":
    if num2 !=0:
        print("Amswer:",num1/num2)
    else:
        print("Error :cannot divide by zero!")
else:
    print("Invalid operator ")
    
    
