while True:
 print("1 Add 2 Subtract 3 Multiply 4 Divide 5 Exit")
 c=input("Choice: ")
 if c=="5": break
 a=float(input("A: ")); b=float(input("B: "))
 if c=="1": print(a+b)
 elif c=="2": print(a-b)
 elif c=="3": print(a*b)
 elif c=="4": print(a/b if b else "Cannot divide by zero")
