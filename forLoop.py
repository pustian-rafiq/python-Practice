
print("Ptint Out for continue statement")
for j in range(1,10):
    if j%2 == 0:
        print("hey, now i am in if block for value", j)
        continue

    print(j)

print("Print out for break statement")
for i in range(1,10):
    if i == 5:
        print("hey, now i am in if block for value", j)
        break

    print(i)