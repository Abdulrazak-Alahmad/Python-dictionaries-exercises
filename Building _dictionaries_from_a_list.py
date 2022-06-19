wordlist = ["apple","durian","banana","durian","apple","cherry",
"cherry","mango","apple","apple","cherry","durian","banana",
"apple","apple","apple","apple","banana","apple"]

fruits={}
for fruit in wordlist:
    fruits[fruit]= wordlist.count(fruit)
    
print( fruits)
