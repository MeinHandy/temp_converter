from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Temperature Converter")
# create all buttons
main_frame = ttk.LabelFrame(root)
main_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

f_convert = ttk.Button(main_frame, text="Convert to fahrenheit")
f_convert.grid(row=1, column=0, padx=10, pady=10)

c_convert = ttk.Button(main_frame, text="Convert to celsius")
c_convert.grid(row=1, column=1, padx=10, pady=10)

exit_button = ttk.Button(main_frame, text="Exit")
exit_button.grid(row=0, column=4, padx=10, pady=10)

export_button = ttk.Button(main_frame, text="Export as .csv")
export_button.grid(row=1, column=4, padx=10, pady=10)

help_button = ttk.Button(main_frame, text="Help")
help_button.grid(row=4, column=4, padx=10, pady=10)

conversion_history = ttk.Button(main_frame, text="History")
conversion_history.grid(row=2, column=4, padx=10, pady=10)

celsius_input = ttk.Entry(main_frame)
celsius_input.grid(row=0, column=0, padx=10, pady=10)

celsius_input = ttk.Entry(main_frame)
celsius_input.grid(row=0, column=1, padx=10, pady=10)

fahrenheit_output = ttk.Label(main_frame, text="fahrenheit_output")
fahrenheit_output.grid(row=2, column=0)

celsius_output = ttk.Label(main_frame, text="celsius_output")
celsius_output.grid(row=2, column=1)


root.mainloop()
