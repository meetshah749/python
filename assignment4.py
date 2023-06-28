numbers = [1, 2, 3, 4, 5]      #Break Statement Loop
for num in numbers:       
    if num == 3:
        break
    print(num)

for num in numbers:       #pass statement loop
    if num == 3:
        pass
    print(num)

for num in numbers:  #Continue Statement loop
    if num == 3:
        continue
    print(num)

for num in numbers:  # For loop with Else Statement
    if num == 3:
        break
    print(num)
else:
    print("Loop completed successfully.")

i = 0        # While loop With Else
while i < 5:
    if i == 3:
        break
    print(i)
    i += 1
else:
    print("Loop completed successfully.")