import requests

r = requests.get('https://api.github.com/users/DeepUthale')

with open("DeepUthale.txt", "w") as file:
    file.write(r.text)
