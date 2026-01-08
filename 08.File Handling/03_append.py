# Append to an existing file called John Doe.txt
# It should contain data about John Doe's Home town

f = open("John Doe.txt", "a")

string = '''
John Initially lived in Phoenix, Arizona. He is a very nice guy. 
'''

f.write(string)

f.close()
