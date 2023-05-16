#Python program to create a simple GUI calculator using Tkinter.
 
#Import everything from tkinter module.
from tkinter import * #here '*' is used to import everything from tkinter. 

#Globally declaring the expression variable.
expression = ""

#Function to update expression in the Text Entry Box.
def Press(num):
    global expression
    #Concatenation of string.(appending)
    expression = expression + str(num)
    #Updating the expression by converting it into 'set' form.
    equation.set(expression)

#Function for evaluating the Final Expression
def EqualKey():
    #Try and except statements are used for handling the errors like Zero Division Error.
    #Putting that type of code inside the try block may generate the Error.
   try:
        global expression
        #'eval' function evaluate the expression and 'str' function converts the Result into string format
        total = str(eval(expression))
        #Updating the total by converting it into 'set' form.
        equation.set(total)
        #Initializing the expression variable by declaring the string as an empty string.
        expression = ""
   #If error is generated, then it will be handled by the 'except' block.
   except:
        equation.set(" ERROR ")
        #Re-initializing the expression variable by declaring the string as an empty string.
        expression = ""

#Function to clear the contents in Text Entry Box.
def ClearKey():
    global expression
    #Re-initializing the expression variable by declaring the string as an empty string.
    expression = ""
    #Updating the empty expression by converting it into 'set' form.
    equation.set("")

# Driver code
if __name__ == "__main__":
    #Creating a GUI window.
    gui = Tk()
    #Setting the title of GUI window.       
    gui.title(" GUI Calculator")
    #Setting the configuration(size) of GUI window.
    gui.geometry("323x233")
    #Setting the background colour of GUI window as 'light grey'.
    gui.configure(background="light grey")    

    #StringVar() is the variable class.
    #We create an instance of this class.
    equation = StringVar()
    #Creating the Text Entry Box for showing the expression.
    expression_field = Entry(gui, textvariable=equation,font="lucida 15 ")
    #Grid method is used for placing the widgets at respective positions in a table like structure.
    expression_field.grid(columnspan=100, ipadx=97.3)
    
    #Creating Buttons and placing them at a particular location inside the root window.
    #When User press a Button, the Command or Function related to that Button is executed .
    button1 = Button(gui, text=' 1 ', fg='black', bg='grey',
                    command=lambda: Press(1), height=2, width=10)
    button1.grid(row=5, column=0)
    
    button2 = Button(gui, text=' 2 ', fg='black', bg='grey',
                    command=lambda: Press(2), height=2, width=10)
    button2.grid(row=5, column=1)
    
    button3 = Button(gui, text=' 3 ', fg='black', bg='grey',
                    command=lambda: Press(3), height=2, width=10)
    button3.grid(row=5, column=2)
    
    button4 = Button(gui, text=' 4 ', fg='black', bg='grey',
                    command=lambda: Press(4), height=2, width=10)
    button4.grid(row=4, column=0)
    
    button5 = Button(gui, text=' 5 ', fg='black', bg='grey',
                    command=lambda: Press(5), height=2, width=10)
    button5.grid(row=4, column=1)
    
    button6 = Button(gui, text=' 6 ', fg='black', bg='grey',
                    command=lambda: Press(6), height=2, width=10)
    button6.grid(row=4, column=2)
    
    button7 = Button(gui, text=' 7 ', fg='black', bg='grey',
                    command=lambda: Press(7), height=2, width=10)
    button7.grid(row=3, column=0)
    
    button8 = Button(gui, text=' 8 ', fg='black', bg='grey',
                    command=lambda: Press(8), height=2, width=10)
    button8.grid(row=3, column=1)
    
    button9 = Button(gui, text=' 9 ', fg='black', bg='grey',
                    command=lambda: Press(9), height=2, width=10)
    button9.grid(row=3, column=2)
    
    button0 = Button(gui, text=' 0 ', fg='black', bg='grey',
                    command=lambda: Press(0), height=2, width=10)
    button0.grid(row=6, column=1)
    
    plus = Button(gui, text=' + ', fg='black', bg='grey',
                command=lambda: Press(" + "), height=2, width=10)
    plus.grid(row=2, column=2)
    
    minus = Button(gui, text=' - ', fg='black', bg='grey',
                command=lambda: Press(" - "), height=2, width=10)
    minus.grid(row=2, column=3)
    
    multiply = Button(gui, text=' * ', fg='black', bg='grey',
                    command=lambda: Press(" * "), height=2, width=10)
    multiply.grid(row=3, column=3)
    
    multiply = Button(gui, text=' ^ ', fg='black', bg='grey',
                    command=lambda: Press(" ** "), height=2, width=10)
    multiply.grid(row=6, column=3)
    
    divide = Button(gui, text=' / ', fg='black', bg='grey',
                    command=lambda: Press(" / "), height=2, width=10)
    divide.grid(row=4, column=3)
    
    divide = Button(gui, text=' // ', fg='black', bg='grey',
                    command=lambda: Press(" // "), height=2, width=10)
    divide.grid(row=5, column=3)
    
    equal = Button(gui, text=' = ', fg='black', bg='grey',
                command=EqualKey, height=2, width=10)#Implementing the function 'EqualKey'.
    equal.grid(row=6, column=2)
    
    clear = Button(gui, text=' C ', fg='black', bg='white',
                command=ClearKey, height=2, width=10)#Implementing the function 'ClearKey'.
    clear.grid(row=2, column=0)
   
    Decimal= Button(gui, text=' . ', fg='black', bg='grey',
                    command=lambda: Press('.'), height=2, width=10)
    Decimal.grid(row=6, column=0)
    # start the GUI
    gui.mainloop()