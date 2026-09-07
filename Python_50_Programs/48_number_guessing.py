import random
secret=random.randint(1,10)
while True:
 g=int(input("Guess 1-10: "))
 if g==secret: print("Correct!"); break
 print("Try again")
