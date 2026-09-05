n=input()
vowels=0
consonats=0
for i in n:
    if i in"aeiouAEIOU":
        vowels=vowels+1
    else:
        consonats=consonats+1
print(f"Vowels = {vowels}")
print(f"Consonats = {consonats}")