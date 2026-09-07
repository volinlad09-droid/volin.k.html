n=int(input("Number: ")); prime=n>1
for i in range(2,n):
    if n%i==0: prime=False; break
print("Prime" if prime else "Not prime")
