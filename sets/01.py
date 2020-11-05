import time
sets ={"cow","dog","cat","donkey"} 

#used to pirint it out
#for x in sets:
#    print(x)

#used to add items in a set
sets.add("hen")
print(sets)

time.sleep(2)

#finding the lengh
print(len(sets))

#used to remuve
sets.remove("dog")
print(sets)
time.sleep(2)
#used to discard
sets.discard("cat")
print(sets)

time.sleep(2)
#used to pop
x = sets.pop()
print(x) 
print(sets) 

time.sleep(2)
#used to clear
#sets.clear()
#print(sets)


sets2 ={"lion","tiger","cheater"}
sets3 = sets.union(sets2)
print(sets3)