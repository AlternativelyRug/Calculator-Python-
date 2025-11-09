import tkinter

button_values = [
    ["AC", "+/-", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row_count = len(button_values)#5
column_count = len(button_values) #4


color_light_gray = "#D4D4D2"
color_black = "#1C1C1C"
color_dark_gray = "#505050"
color_orange = "#FF9500"
color_white = "white"

#wind setup
window = tkinter.Tk() #create the window
window.title ("Calculator")
window.resizable(False, False)
window.mainloop()

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text ="0", )