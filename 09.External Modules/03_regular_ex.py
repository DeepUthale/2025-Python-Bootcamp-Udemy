import re
text = "The quick brown fox jumps over the lazy dog."

# Search for a pattern
match = re.search("brown", text)
print(match)
if match:
    print("Match Found!")
    print("Start Index:", match.start())
    print("End Index:", match.end())

# Find all occurrences of a pattern
matches = re.findall("the", text, re.IGNORECASE) # Case-insensitive Search
print("Matches:", matches)

new_text = re.sub("fox", "cat", text)
print("New text:", new_text)
