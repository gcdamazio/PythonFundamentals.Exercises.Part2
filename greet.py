# ## Exercise 2

# Create a script called *greet.py*.

# * Define a function called *greet* that meets the following criteria: 
#     * Takes an argument called *name*.
#     * Prints a greeting using the *name* parameter.

def greet(name):
    print ("Hello " + str(name))

# * Define another function called *name_input* that meets the following criteria:
#     * Takes no arguments.
#     * Prints a message to the screen requesting the user to provide a name.
#     * Returns a string with the value equals to that of the provided name.
# * Using these two functions, prompt the user for a name and print it to the screen.
# * Each function must have an appropriate docstring.

def name_input():
    print ("Please provide a name")
    requestedName = str(input("Enter your name ")) 
    return requestedName

givenName = name_input()
greet(givenName)