sum_of_numbers = sum(numbers)   #sum of all elements
print("Sum of all elements:", sum_of_numbers)

smallest_number = min(numbers)  #smallest num
print("Smallest number:", smallest_number)

largest_number = max(numbers)   #largest number
print("Largest number:", largest_number)

ascending_order = sorted(numbers)    #ascending
print("List in ascending order:", ascending_order)

descending_order = sorted(numbers, reverse=True)    #descending order
print("List in descending order:", descending_order)

numbers_tuple = tuple(numbers)   #list into Tuple
print("List converted to tuple:", numbers_tuple)

del numbers   #delete list
print("List deleted.")