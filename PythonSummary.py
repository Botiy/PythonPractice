'''
Password checker
'''
def password_checker():
    username = input('what is your username?')
    password = input('what is your password?')
    passlen = len(password)
    hidden_pass = '*'*passlen
    print(f'{username} your password: {hidden_pass}, is {passlen} letters long')

#password_checker()

'''
String indexer [start:stop:stepover]
'''

def string_indexer():
    numbers = '01234567'
    start = numbers[:3]
    stop = numbers[3:]
    stepover= numbers[0:8:2]
    print(start)
    print(stop)
    print(stepover)

#string_indexer()

'''
Data structures: List, tuple, set, dictionary
'''

def data_structures():
    '''
    Contains information about data structures
    '''
    # List: type is not fixed
    '''
    List methods
    append()	Adds an element at the end of the list
    clear()	    Removes all the elements from the list
    copy()	    Returns a copy of the list
    count()	    Returns the number of elements with the specified value
    extend()	Add the elements of a list (or any iterable), to the end of the current list
    index()	    Returns the index of the first element with the specified value
    insert()	Adds an element at the specified position
    pop()	    Removes the element at the specified position
    remove()	Removes the first item with the specified value
    reverse()	Reverses the order of the list
    sort()	    Sorts the list
    '''
    list= ['lista', 33, 'listc']
    print(f"List elements:{list}\n"
          f"Length: {len(list)}\n"
          f"Append: {list.append('listnew')} {list}\n"
          f"Insert: {list.insert(2, 'listd')}{list}\n"
          f"Count:'a'  {list.count('a')}\n"
          f"Remove:'c' {list.remove('listc')} {list}\n"
          f"Clear:  {list.clear()} {list}\n")
    # Tuple: contains elements with the same type
    '''
    Tuple methods:
    count()	Returns the number of times a specified value occurs in a tuple
    index()	Searches the tuple for a specified value and returns the position of where it was found
    '''
    tuple= ('tuple1', 'tuple2', 'tuple3')
    new = tuple[0:2]
    print(f"Tuple elements:{tuple}\n"
          f"New: {new}\n")

    # Dictionary: contains key-value pairs
    '''
    Dictionary methods:
    clear()	Removes all the elements from the dictionary
    copy()	Returns a copy of the dictionary
    fromkeys()	Returns a dictionary with the specified keys and value
    get()	Returns the value of the specified key
    items()	Returns a list containing a tuple for each key value pair
    keys()	Returns a list containing the dictionary's keys
    pop()	Removes the element with the specified key
    popitem()	Removes the last inserted key-value pair
    setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
    update()	Updates the dictionary with the specified key-value pairs
    values()	Returns a list of all the values in the dictionary
    '''
    dictionary = {'a': 1,
                  'b': 2,
                  'c': 3}
    updict = dictionary.copy()
    updict.update({'d': 4})

    print(f"Dictionary elements:{dictionary}\n"
          f"Keys: {dictionary.keys()}\n"
          f"Values: {dictionary.values()}\n"
          f"Update: {updict}\n")

    # Set: used to return unique elements
    '''
    Set functions: 
    add()	 	Adds an element to the set
    clear()	 	Removes all the elements from the set
    copy()	 	Returns a copy of the set
    difference()	-	Returns a set containing the difference between two or more sets
    difference_update()	-=	Removes the items in this set that are also included in another, specified set
    discard()	 	Remove the specified item
    intersection()	&	Returns a set, that is the intersection of two other sets
    intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
    isdisjoint()	 	Returns whether two sets have a intersection or not
    issubset()	<=	Returns whether another set contains this set or not
 	<	Returns whether all items in this set is present in other, specified set(s)
    issuperset()	>=	Returns whether this set contains another set or not
 	>	Returns whether all items in other, specified set(s) is present in this set
    pop()	 	Removes an element from the set
    remove()	 	Removes the specified element
    symmetric_difference()	^	Returns a set with the symmetric differences of two sets
    symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
    union()	|	Return a set containing the union of sets
    update()	|=	Update the set with the union of this set and others
    '''
    my_set = {-1,1,2,3,4,5,5}
    convert_list = [1, 2, 3, 3]
    print(f"Set elements(unique): {my_set}\n"
          f"Convert list into set: {set(convert_list)}")


data_structures()