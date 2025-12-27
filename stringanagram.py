s="tae"
r="ate"
def anagram(s,r):
for char in s:
      if char not in r:
return "anagram"
print(anagram(s,r))
