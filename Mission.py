def sumofsq(array, N):  # Function that calculates the sum of squares of numbers recursively
    
    if len(array) == 1: # Base Case
        return array[0] * array[0]
    else:
        return array[0] * array[0] + sumofsq(array[1:], N) # Recursive Case
    
def remove_neg(array): # Function that removes negative integers from a list of integers
    
    array = filter(lambda x: x >= 0, array)
    array1 = list(array)
    return array1

def input_in_list(list, length): # Function that takes input inside a Python List recursively
    if(length == 0): # Base Case
        return list
    else:
        ele = int(input()) 
        list.append(ele)
        return input_in_list(list, length - 1) #Recursive Case

def not_main(list_of_sums, start): # Function that recursively repeats all the processes for the given number of test cases
    
    if(start == 0): # Base Case
        return 0
    else:
        
        length = int(input()) # Number of Elements entered by the user
        
        ll = [] # Empty List
        
        array = input_in_list(ll, length) # Taking elements from user's input into a list
        
        array = remove_neg(array) # Removing all the negative elements from the user's input
        
        length = len(array) # Number of elements after removing negative elements
            
        ans = sumofsq(array, length) # Sum of Squares of the above elements
            
        list_of_sums.append(ans) # Storing all the sums in a separate list
        
        return not_main(list_of_sums, start - 1) # Recursive Case
    
    
def print_sums(list_of_sums, length1, i): # Function that recursively prints the elements of a list
    if(length1 == 0): # Base Case
        return 0
    else:
        print(list_of_sums[i])
        return print_sums(list_of_sums, length1 - 1, i + 1) # Recursive Case

def main(): # Main  Function
    
    N = int(input()) # Taking Number of Test Cases as input from the user
    
    list_of_sums = [] # Empty List
    
    not_main(list_of_sums, N) # Starting the whole process
    
    i = 0
    
    print_sums(list_of_sums, len(list_of_sums), i) # Prints the Sums of Squares of Positive Integers
     
if __name__ == "__main__": # Checking if the method is main or not
    main() # Running the main() method
