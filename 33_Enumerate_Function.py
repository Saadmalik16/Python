l1 = ["A", "B", "C", "D"]
# i = 1
# for item in l1:
#     if i%2 is not 0:
#         print(f"Please Buy {item}")
#     i += 1
for index, item in enumerate(l1):
    if index%3 ==0:
        print(f"Please Buy {item}")
