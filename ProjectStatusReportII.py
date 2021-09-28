"""  Grocery Getter by Erin McGuire Magrey
Version 3 .  Last updated 28 Sep 2021
"""
from breezypythongui import EasyFrame   # Lambert's shell for book exercises
 
class GroceryGetter(EasyFrame):       # create class.
    def __init__(self):       # set initial state.
        
        #create first window
        EasyFrame.__init__(self)
        self.addLabel(text= 'Welcome to Grocery Getter. \
             \n Enter how many pounds of each vegetable you would like. \
             \nTo see how many pounds of vegetables you have ordered, click "Total". \
             \n To have your vegetables delivered, click "Delivery".  \
             \nTo pick up your vegetables at the grocery store, click "Pick Up".', row=0, column=0)
        
        #create second window
        EasyFrame.__init__(self,title="Grocery Getter") # create the window
        # create the window with header
        # Add three labels and fields for the input
        self.addLabel(text ="Broccoli",row=0,column=0)
        self.inputField1 = self.addIntegerField(value=0,row=0,column=1,
                                             width=10) 
        self.addLabel(text ="Carrots",row=1,column=0)
        self.inputField2 = self.addIntegerField(value=0,row=1,column=1,
                                             width=10) 
        self.addLabel(text ="Parsnips",row=2,column=0)
        self.inputField3 = self.addIntegerField(value=0,row=2,column=1,
                                             width=10)                                       
        # Add single label and field for the output
        self.addLabel(text ="Total",row=3,column=0)
        self.outputField = self.addFloatField(value=0.0,row=3,column=1,
                                             width=8,precision=2,
                                             state="readonly")
                # the command button with event handler method
        # place buttons in a panel
        buttonPanel=self.addPanel(row=4, column=0,
                                background="black") #create panel
        buttonPanel.addButton(text ="Total",row=4,column=0,columnspan=1,
                      command = self.total)
        buttonPanel.addButton(text ="Delivery",row=4,column=1,columnspan=1)
#                      command = self.delivery)
        buttonPanel.addButton(text ="Pick Up",row=4,column=2,columnspan=1)
#                      command = self.pickUp)

        # Methods to handle user events
    def total(self):
        try:                # error handling and message box pop up
        #resets the label to empty string and updates the button states
            number1 = self.inputField1.getNumber()
            number2 = self.inputField2.getNumber()
            number3 = self.inputField3.getNumber()
                     # Calculate from data entered
            result=number1+number2+number3
            self.outputField.setNumber(result)
        except ValueError:
            self.messageBox(title="ERROR",
                            message="Input must be an integer.")

               
def main():     # instantiation and pops up the window - infinite loop
    GroceryGetter().mainloop()
        
# execute main() module
if __name__=="__main__":
     main()
        
