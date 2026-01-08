# Write to a file called John Doe.txt
# It should contain data about John Doe

f = open("John Doe.txt", "w")

string = '''
John Doe lives in NYC and he works with Python. His Favourite Package is Pandas. 
'''

f.write(string)

f.close()
