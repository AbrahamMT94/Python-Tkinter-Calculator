from tkinter import *
from float_bin import * # holds the float_bin converter function
#creating a window
window = Tk()
window.title("Programming Calculator")

#### Functions ####
# Detects button and ensures valid input
def btn_click(item): 
    global expression
    length=len(expression)

    if str(item) == '=' : #cehck to see if button is '='
        btn_equal()
        return
    

    if length==0 and str(item) not in '+-/*': # this ensures the first value is not an op and adds it to the string
        expression = expression + str(item)
        input_text.set(expression)

    elif length>=1 and expression[-1] in '+-/*' and str(item) in '+-/*': # if its not the first value then check the last value to avoid reapted signs
        return

    else:  
        expression = expression + str(item)
        input_text.set(expression)


# clears the input field
def btn_clear():
    global expression
    expression = ""
    input_text.set("")


# calculates the expression present in input field
def btn_equal(): 
    global expression

    if len(expression)<=2:#check for valid input
        return
    
    result = str(eval(expression)) # 'eval' function evalutes the string expression directly
    input_text.set(result)
    input_text_bin.set(float_bin(result))# format for binary
    expression = ""

# global variable that holds the current operation
expression = ""


# 'StringVar()' is used to get the instance of input field
input_text = StringVar()
input_text_bin = StringVar()

# creating a frame for the input fields for normal and binary results
input_frame = Frame(window,bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
input_frame.pack(side = TOP)


# creating fields for results
# decimal
input_field = Entry(input_frame, font = ('arial', 18, 'bold'), textvariable = input_text,  bg = "#fff", bd = 0, justify = RIGHT)
input_field.grid(row = 0, column = 0)

#binary
input_field2 = Entry(input_frame, font = ('arial', 18, 'bold'), textvariable = input_text_bin,  bg = "#fff", bd = 0, justify = RIGHT)
input_field2.grid(row = 1,column = 0)


# 'Frame' for the buttons below the 'input_frame'
btns_frame = Frame(window, bg = "grey")
btns_frame.pack()


# First button(clear) is customized for aesthetics.
Button(btns_frame, text = "C", fg = "black", width = 32, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)

buttons='=+-*/' # string containing buttons
number=0# used to fill up our calculator numbers and buttons
index=0

for rows in range(4,-1,-1):# nested loops to instantiate our buttons
    for cols in range(0,4,1):

        if cols==3:# col 3 is where all our op buttons are
            size=1
            if index==0:
                size=2
            Button(btns_frame, text = str(buttons[index]), fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda val= buttons[index] : btn_click(val)).grid(row = rows, columnspan = size, column = cols, padx = 1, pady = 1)
            index+=1
            break


        if rows!=4 and rows!=0:# numbers 1-9
            Button(btns_frame, text = str(number), fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda number = number : btn_click(number)).grid(row = rows, column = cols, padx = 1, pady = 1)
            number+=1


        if rows==4 and cols==1: #number 0 and period
            Button(btns_frame, text = str(number), fg = "black", width = 22, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda number = number : btn_click(number)).grid(row = rows, columnspan=2, column = cols-1, padx = 1, pady = 1)
            Button(btns_frame, text = '.', fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda number = number : btn_click('.')).grid(row = rows, column = cols+1, padx = 1, pady = 1)
            number+=1


window.mainloop()