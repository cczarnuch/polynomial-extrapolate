## @file SeqADT.py
#  @author Connor Czarnuch
#  @date 01/21/2018


from time import sleep

## @brief SeqT is a class composed of a list with operations for a given object.
#  @details SeqT includes a constructor, several mutators, and several accessors.
class SeqT:
    ## @brief The init class constructs a list within the class.
    def __init__(self):
        ## @brief A variable of type list to store elements of a given type
        self.lst = []

    ## @brief add is a mutator that can add objects to a list
    #  @details add can insert a data value at any point within, or just after the list. The number of elements will always increase by one.
    #  @param i is the index that you wish to insert an element v at.
    #  @param v is the value of the element that you wish to add.
    #  @return The returned value is the updated list.
    def add(self, i, v):
        if i < len(self.lst):
            return self.lst.insert(i, v)
        else:
            return self.lst.append(v)

    ## @brief rm is a mutator that removes elements from the list. The number of elements decreases by one.
    #  @param i is the index of the element you wish to remove.
    #  @return The returned value is the updated list.
    def rm(self, i):
        return self.lst.pop(i)

    ## @brief set is a mutator that changes the value of an element in the list. The number of elements is unchanged.
    #  @param i is the index of the element you wish to change
    #  @param v is the new value of the element.
    #  @return The returned value is the value of the returned list.
    def set(self, i, v):
        self.lst[i] = v
        return self.lst

    ## @brief get is an accessor that gets the value of the list at a certain index.
    #  @param i is the index of the element that you wish to get.
    #  @return The returned value is the value at the given index of the list.
    def get(self, i):
        return self.lst[i]
    
    ## @brief size is an accessor that gets the size of the list.
    #  @return The returned value is the number of elements of the list as an integer.
    def size(self):
        return len(self.lst)

    ## @brief indexInSeq is an accessor that takes a value as input and determines the indices of two consecutive elements that have lower and higher values than the input, respectively.
    #  @param v is a numerical value for use in this function.
    #  @return The returned value is an index of the list where the value at the index is less than the inputted value and the next value in the list is greater than the inputted value.
    def indexInSeq(self, v):
        try:
            for i in range(self.size()):
                if self.get(i) <= v and v <= self.get(i + 1):
                    return i
        except IndexError:
            print("The value is out of range of the file, please amend the file or choose a new value.\nExiting...")
            sleep(2)
            exit()
