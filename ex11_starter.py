#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

print( '-'*len(Belgium))
Belgium_list= Belgium.split(',') #searches for every comma in string and splits it(takes the commas out) and makes string into list
print (Belgium_list)
Belgium_new= ':'.join(Belgium_list)#takes strings in the list and separates them with colon. Undoes the list, it's a string
print(Belgium_new)
print(int(Belgium_list[1])+ int(Belgium_list[3]))#we take indeces from our list and add