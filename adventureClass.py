class AdventureClass: #Prints out text and displays choices
    def __init__(self, text, choices=None):
        self.text = text
        self.choices = choices

    def printAdventure(self):
        printedText = self.text + "\n\n" #Assigns the description text to a variable.
        if self.choices != None: #Checks if there have been any choices defined to branch to
            for key in self.choices:
                printedText += (str(key) + ": " + self.choices[key] + "\n") #Adds all the choices assigned to the story node to the variable.
        print(printedText) #returns the variable.

testPara = AdventureClass("""
This is a test case""", {1: "choice 1", 2: "choice 2"})

testPara.printAdventure()

    
