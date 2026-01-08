# def is_greater_than_9(x):
#     if x > 9:
#         return True
#     else:
#         return False
    
a = [1, 3, 5, 23, 45, 86, 77, 124, 236, 6, 8, 10]

new = list(filter(lambda x: x>9, a))
print(new)
