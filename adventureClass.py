class AdventureClass: #Prints out text and displays choices
    def __init__(self, text, choices_input=[]):
        self.text = text
        self.choices_input = choices_input
        self.choices_array = range(len(choices_input)) #This array will be used to assign the values from self.choices_input to their repective keys in the self.choice dictionary.
        self.choices = {} #This will be used to store all the choices available to the user.
        for choice in self.choices_array: #Assigning each choice to it's repective key in the dictionary.
            key = self.choices_array[choice]+1 #Correction, else choice 1 will have a key of 0.
            value = self.choices_input[choice]
            self.choices[key] = value
            print("Adding {value} to {key}".format(value=value, key=key))
        

    def printAdventure(self):
        printedText = self.text + "\n\n" #Assigns the description text to a variable.
        if self.choices != None: #Checks if there have been any choices defined to branch to
            for key in self.choices:
                printedText += (str(key) + ": " + self.choices[key] + "\n") #Adds all the choices assigned to the story node to the variable.
        print(printedText) #returns the variable.

testPara = AdventureClass("""
This is a test case""", ["choice 1", "choice 2"])
testPara2 = AdventureClass("""
This is also a test case""")

testPara.printAdventure()
testPara2.printAdventure()
