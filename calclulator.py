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
column_count = len(button_values[0])  # 4


color_light_gray = "#D4D4D2"
color_black = "#1C1C1C"
color_dark_gray = "#505050"
color_orange = "#FF9500"
color_white = "white"

#wind setup
window = tkinter.Tk() #create the window
window.title ("Calculator")
window.resizable(False, False)
window.geometry("360x520")

frame = tkinter.Frame(window)
frame.configure(background=color_black)
label = tkinter.Label(
    frame,
    text="0",
    font=("Arial", 45),
    background=color_black,
    foreground=color_white
)

label.grid(row=0, column=0, columnspan=column_count, sticky="nsew", pady=5)
label.lift()
label.configure(anchor="e")
frame.grid_rowconfigure(0, weight=0, minsize=90)

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(
            frame,
            text=value,
            font=("Arial", 30),
            background=color_light_gray,
            foreground=color_black,
            activebackground="#E5E5E5",
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            command=lambda value=value: button_clicked(value)
        )
        button.grid(row=row+1, column=column, padx=5, pady=5, ipady=10, sticky="nsew")


frame.pack(fill="both", expand=True)

def button_clicked(value):
    pass

for c in range(column_count):
    frame.grid_columnconfigure(c, weight=1)
for r in range(1, row_count + 1):
    frame.grid_rowconfigure(r, weight=1)

window.mainloop()