word = "apple,durian,banana,durian,apple,cherry,cherry,mango," + \
"apple,apple,cherry,durian,banana,apple,apple,apple," + \
"apple,banana,apple"

list=word.split(',')
fruits={}
for fruit in list:
    fruits[fruit]= list.count(fruit)
    
print( fruits)
