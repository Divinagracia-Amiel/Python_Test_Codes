#Lists
x = [1,2,3,4,5] #[0,1,2,3,4,...,n] or [-5, -4, -3, -2, -1] will be the order 
print(x) #all the numbers in the list will be printed
print(x[0]) #the first number is printed
print(x[-2]) #fouth number will be printed
print(x[0:3]) #the first to 3rd number will be printed (*note: the 4th is the limit hence is not printed
print(x[2:]) #from the 3rd onwards is printed (*note: no limit)
y = x[3] * x[4] #4th number * 5th number
print(y)
z = 3
z += x[2] # adding itself to the 3rd number of the list
print (z)
names = ['amiel','osias','divinagracia'] #string list
print(names)
diff = ['amiel', 4.5, 5, 'osias', 1E-3] #lists can work out differen data types
print(diff)
var = [names, diff, x] #lists within a list
print(var)
var.append(45) #append is adding the data to the selected list at the end
print(var)
x.insert(2, 'tanga')  #in between at index 2 which is the third in the list
print(x)

subject = ['chemistry', 'calculus', 'programming']
subject.remove('chemistry') #will remove selected thing in the selected list
print(subject)
subject.pop(0) #pop is used for removing the data in an index
print(subject)

num = [1,2,3,4,5]
num.pop()
print(num) #when pop has no value, it will remove the last element in the list
num = [1,2,3,4,5]
del num[2:] #deleting multiple data based on index number, in this case, deleting the 3rd data until last
print(num)

num = [1,2,3,4,5]
num.extend(['amiel','divinagracia','osias']) #adding multiple items in the list (note* dont forget the extra bracket inside)
print(num)

num = [1,2,3,4,5]
print(min(num)) #finding the smallest value in the list
print(max(num)) #finding the largest value in the list
print(sum(num)) #sum of all the values in the list

num = [3,4,7,8,1,22,100,64,23,23,23,22]
brain = ['games','feelings','you']
num.sort() #sorting the values in the list
print(num)
num.reverse() #reverses the order of the list
print(num)
x = num.count(22) #counting the frequency of the selected element
y = num.count(23) #counting the frequence of the selected element
brain.remove('feelings') 
brain.remove('you')
print(x,y)
print(brain)

brain = ['games','feelings','you']
garb = brain.copy() #copying lists
print(garb)
clr = garb.clear() #deleting all elements
print(garb)
#Finally, lists are mutable so they are changeable as were doing right now           
           
           
           
           
           
           
           