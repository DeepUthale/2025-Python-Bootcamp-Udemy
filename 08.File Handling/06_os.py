import os

li = os.listdir("dir")
print(li)

print(os.getcwd())
print(os.path.exists("dir"))
print(os.path.exists("deep"))

# os.remove("sample.txt")
os.rmdir("dir/sub")
