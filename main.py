from tkinter import *
from tkinter import ttk


def c_convert_func():  # converts the input to a fahrenheit output
    temp = fahrenheit_input.get()
    try:
        temp = float(temp)
        temp = (temp - 32) * (5/9)
        temp = round(temp, 2)
        if temp < -273.15:  # absolute zero in C
            temp = str(temp) + "°C"
            c_out.set("Invalid input, temperature is\nbelow absolute zero.\n({} < 273.15°C)".format(temp))
            return
        temp = str(temp) + "°C"
        c_out.set(temp)
    except ValueError:
        c_out.set("Please input a number")


def f_convert_func():  # converts the input to a celsius output
    temp = celsius_input.get()
    try:
        temp = float(temp)
        temp = (temp * (9/5)) + 32
        temp = round(temp, 2)
        if temp < -459.67:  # absolute zero in F
            temp = str(temp) + "°F"
            f_out.set("Invalid input, temperature is\nbelow absolute zero. ({} < 459.67°F)".format(temp))
            return
        temp = str(temp) + "°F"
        f_out.set(temp)
    except ValueError:
        f_out.set("Please input a number")


root = Tk()
root.title("Temperature Converter")
# create all buttons
main_frame = ttk.LabelFrame(root)
main_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

f_convert_button = ttk.Button(main_frame, text="Convert to fahrenheit", command=f_convert_func)
f_convert_button.grid(row=1, column=0, padx=10, pady=10)

c_convert_button = ttk.Button(main_frame, text="Convert to celsius", command=c_convert_func)
c_convert_button.grid(row=1, column=1, padx=10, pady=10)

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

fahrenheit_input = ttk.Entry(main_frame)
fahrenheit_input.grid(row=0, column=1, padx=10, pady=10)

f_out = DoubleVar()
f_out.set("fahrenheit_output")
fahrenheit_output = ttk.Label(main_frame, textvariable=f_out)
fahrenheit_output.grid(row=2, column=0)

c_out = DoubleVar()
c_out.set("celsius_output")
celsius_output = ttk.Label(main_frame, textvariable=c_out)
celsius_output.grid(row=2, column=1)


root.mainloop()
