""" 
Both iterator and generator are used to iterate over a sequence of data,
but they differ in how they are implemenated

"""
#Iterator

"""
Iterator are an object which contains countable value to be iterate over,
In python iterator are build over a two protocol
1. __iter__ it returns the iterator object itself
2. __next__  it returns the next element from the iterator, if no more element left
 it raise Stopiteration
"""

class Myiterator:
    def __init__(self,data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            item = self.data[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration
        
data = [1,3,4,5]
output=Myiterator(data)
for i in output:
    print(i)

# Generator 

"""
A generator is a function that yields values one at a time and returns an iterator. 
Unlike a normal function, which returns a value and terminates, 
a generator uses yield to return a value and suspends its state, 
so it can continue from where it left off when next() is called again.
"""

def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4

# Using the generator
gen = my_generator()

for value in gen:
    print(value)
