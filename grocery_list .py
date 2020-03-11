#Hunter Holcombe
#Grocery List Script That Accepts User Input

#Code to create an empty dictionay named grocery_item
grocery_item = {}

#Code to create an empty list named grocery_history
grocery_history = []

#Variable definitions
grand_total = 0.00 
stop = 'go'


#While loop that stops on the condition that the variable stop is set to 'stop'
#This loop accepts user input to add to the list and dictionary defined above
while stop == 'go' :
    item_name = input("Item name:\n")
    quantity = input("Quantity purchased:\n")
    cost = input("Price per item:\n")
    condition_input = input("Would you like to enter another item?\nType 'c' for continue or 'q' to quit:\n")
    
    #Adding key-value pairs to the dictionary
    grocery_item = {'name':item_name, 'number': int(quantity), 'price': float(cost)}
    
    #Adding the grocery_item above to the list using the append function
    grocery_history.append(grocery_item)
    
    #If the user enters into the promt 'q' the while loop condition is met to break
    if condition_input == 'q':
      stop = 'stop'

      
#For loop that goes through the amount of elements in the grocery_history list
for i in range(len(grocery_history)):
  
  #Using values from the list to calculate each item total and adding that to the grand total
  item_total = grocery_history[i]['number'] * grocery_history[i]['price']
  grand_total = grand_total + item_total
  
  #Print using the defined format by converting values to string utilizing elements from the list
  print(str(grocery_history[i]['number']) + " " + str(grocery_history[i]['name']) + " @ $" + str(grocery_history[i]['price']) + " ea $" + str(item_total))
  item_total = 0
  i = i + 1
  
  
#Print the grand total at the end of the output  
print("Grand total: $" + str(grand_total))
