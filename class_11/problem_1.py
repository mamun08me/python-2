'''Create a nested loop to simulate:
Daily schedule like:

Morning session → 3 tasks
Evening session → 3 tasks'''

for order in range(1,3):
    if order==1:
        for i in range(3):
            print(f"morning_task{i+1}")
    else:
        for i in range(3):
            print(f"evening_task{i+1}")
            