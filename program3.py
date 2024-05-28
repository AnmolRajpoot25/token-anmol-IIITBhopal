List1 = [12 ,3,4,5,6,7,8]
list2 =[12 , 123,44,56,667,]
#catenation
print( List1 + list2)
print(list2 + List1)
#reptiton */
list3= [ 'party' ]
print (list3*5) 
#membership 
# membership 
list4= ['Anmol','Saurabh','Prince','Anuj','Nishu']
print('Anmol' in list4)
#print(True)
print('Agrim' in list4)
#print(False) 
print('Saurabh' in list4)
#print(True)
print('Divyank' not in list4)
#print(False)
# #Slicing 
list5= ['Anmol','divyanshu','Shivanshu','Saraubh','Prince','Anuj','Nishu']
print(list5[2:4])
print(list5[2:7:2])
#if the start is not inisitialised than start with 0 and the end is stop -1
#[a:b:c]} a is start which is included, bis the the stop which is excuted till stop-1 , cis the the jump amount how much should we jump during slicing of the list 
#is the negative index is given then start with the end of the list such as -1 is Nishu from list 5 

print(list5[-1])
print(list5[-1:-6:2])
print(list5[::1])
print(list5[::-1])
#append ,add ,extend , update 
X = [1,2,3,4,5,6]
print(X)
X.append(44)
print(X)
# add is for Set to adding only 1 element while update is adding more than 1 element in set duplication is not allowed in set 
#set is unordered data while list is a a orddered data , duplication is possible in the set while in list it is possible 
line = 'this is the time ti booming up to the sky with your golden wings'
line = line.rstrip()
#if not line.startswith('From') :
words = line.split()
print(words[1])
print(words[2])
print(words[6])
print(words[3])
print(words[4])
print(words[5])
# the double split pattern 
line6= 'from rajpootanmol779@gmail.com' 
words = line6.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])

