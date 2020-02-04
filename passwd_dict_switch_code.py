#!/usr/bin/python3
import string

#############
# FUNCTIONS #
#############
## print unique occurences from user input
#tokenized user input is independent variable of function
def unique(usr_in):
    #create a new empty list
    single_char = []
    #iterate thru tokenized user input 
    for val in usr_in: 
        #if tokenized char not in empty list...
        if val not in single_char:
            #...append to list 
            single_char.append(val) 
            #else skip char

    return single_char 
    print(unique(usr_in))

## mirror opposite case into list
def case(usr_in):
    #tokenize user input
    usrin = list(usr_in)
    #uppercase copy of user input
    usrup = list(usr_in.upper())
    #lowercase copy of user input
    usrdn = list(usr_in.lower())
    #concatenate user input
    case = usrin + usrup + usrdn
    #create a new empty list
    single_char = []
    #iterate thru tokenized user input 
    for val in case: 
       #if tokenized char not in empty list...
        if val not in single_char:
            #...append to list 
            single_char.append(val) 
            #else skip char
            
    return single_char 
################
# INSTRUCTIONS #
################

usr_in = input("elements to combine: ")

if "-lit" in usr_in:
    print(unique(usr_in))
else:
    print(case(usr_in))