
from functools import wraps
from time import time

#######################################
# Timing Tools
#######################################

# Returns and prints the elapsed runtime of a function
def timeIt(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        startTime = time()
        for i in range(0, 10000):
            func(*args)
        endTime = time()

        elapsedTime = (endTime - startTime) * 1000
        print(func.__name__.ljust(20, ' ') + ':' + str('%.3f' % elapsedTime).rjust(10, ' ') + ' ms')

        return elapsedTime
    return wrapper

# Compares the runtimes of any number of functions and prints the best one
def timeCompare(funcs, data):
    executionTimes = {}
    for item in funcs:
        executionTimes[item.__name__] = item(data)
    
    fastestFunction = sorted(executionTimes, key=executionTimes.get)[0]
    print(f'{fastestFunction} is the best')

#######################################
# Test String Concatenation versus Join
#######################################

# Concatenates a list of strings into one string, with spaces in between
# each item in the list
@timeIt
def stringConcatenator(words):
    resultString = ''
    for item in words:
        if item == words[-1]:
            resultString = resultString + str(item)
        else:
            resultString = resultString + str(item) + ' '
    return resultString

# Concatenates a list of strings with the join() function
@timeIt
def stringJoiner(words):
    return ' '.join(words)
 
# A collection of words that will be used
# to test Concatenation and Joining
words = []
for i in range(100,300):
    words.append(str(i))

# Compare stringConcatenator and stringJoiner
timeCompare([stringConcatenator, stringJoiner], words)

# Extra print to space out output
print()

#######################################
# Test String Formatting
#######################################

# Formatting a string with the percent style
@timeIt
def stringPercent(words):
    return '%s%s%s%s%s%s%s%s%s%s%s%s%s' % (words[0],  words[1], words[2], words[3], words[4], \
         words[5], words[6], words[7], words[8], words[9], words[10], words[11], words[12])

# Formatting a string with the format method
@timeIt
def stringFormat(words):
    return '{}{}{}{}{}{}{}{}{}{}{}{}{}'.format(words[0],  words[1], words[2], words[3], words[4], \
         words[5], words[6], words[7], words[8], words[9], words[10], words[11], words[12])

# Formatting a string with the f specifier
@timeIt
def stringF(words):
    return f'{words[0]}{words[1]}{words[2]}{words[3]}{words[4]}{words[5]}{words[6]}{words[7]}{words[8]}{words[9]}{words[10]}{words[11]}{words[12]}'

# A collection of 13 long strings that will be used to test
# the 3 formatting styles
words = ["Fourscore and seven years ago our fathers brought forth,", 
         "on this continent, a new nation, conceived in liberty,", 
         "and dedicated to the proposition that all men are created equal. ", 
         "Now we are engaged in a great civil war, testing whether that nation,", 
         "or any nation so conceived, and so dedicated, can long endure. ", 
         "We are met on a great battle-field of that war. ", 
         "We have come to dedicate a portion of that field,", 
         "as a final resting-place for those who here gave their lives, "
         "that that nation might live. ", 
         "It is altogether fitting and proper that we should do this. ",
         "But, in a larger sense, we cannot dedicate, ",
         "we cannot consecrate—we cannot hallow—this ground.", 
         "The brave men, living and dead, who struggled here, ",
         "have consecrated it far above our poor power to add or detract. "]

# TODO: compare stringPercent, stringFormat, and stringF here
# Use words as the list of words to format
timeCompare([stringPercent, stringFormat, stringF], words)

# Extra print to space out output
print()


#######################################
# Test List Building
#######################################

# TODO: complete the ListRangeObject Iterator Object
class ListRangeObject:
    pass

# TODO: complete the rangeGenerator Function
def rangeGenerator(max):
    pass

# TODO: complete the listRange Function
def listRange(max):
    pass

# TODO: complete the listComprehension Function
def listComprehension(max):
    pass

# TODO: complete the listIterator Function
def listIterator(max):
    pass

# TODO: complete the listIterator Function
def listGenerator(max):
    pass

# TODO: complete the listExpression Function
def listExpression(max):
    pass

max = 100

# TODO: compare listRange, listIterator, listGenerator, and listExpression here
# Use max as the number of items to generate

print()


