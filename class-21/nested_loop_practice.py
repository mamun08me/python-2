r = int(input("Row: "))
c = int(input("Column: "))

for i in range(r):
    for j in range(c):
        # বর্ডার এবং দুটি ডায়াগোনাল লাইনের শর্তসমূহ
        if i == 0 or i == r - 1 or j == 0 or j == c - 1 or i == j or i + j == r - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
