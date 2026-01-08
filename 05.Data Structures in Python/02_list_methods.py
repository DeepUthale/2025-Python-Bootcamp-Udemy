marks = [5, 2, 21, 5, 7]
print(marks)

marks.append(63) # This will change the original list
print(marks)

marks.pop()
print(marks)

extra_marks = [53, 23, 32]
marks.extend(extra_marks)
print(marks)

marks.sort()
print(marks)

marks.reverse()
print(marks)

# Table of 5
# a = 5
# table = []

# for i in range(1,11):
#     table.append(a*i)

table = [5*i for i in range(1, 11)]

print(table)
