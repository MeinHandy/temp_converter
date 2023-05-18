from tkinter import *
from tkinter import ttk
history = {}


def c_convert_func():  # converts the input to a fahrenheit output
    temp_f = fahrenheit_input.get()
    try:
        temp_f = float(temp_f)
        temp_c = (temp_f - 32) * (5/9)
        temp_c = round(temp_c, 2)
        if temp_c < -273.15:  # absolute zero in C
            temp_c = str(temp_c) + "°C"
            c_out.set("Invalid input, temperature is\nbelow absolute zero.\n({} < 273.15°C)".format(temp_c))
            return  # ends the subroutine
        temp_c = str(temp_c) + "°C"
        c_out.set(temp_c)
        temp_f = str(temp_f) + "°F"
        history[temp_f] = temp_c
        print(history)
    except ValueError:
        c_out.set("Please input a number")


def f_convert_func():  # converts the input to a celsius output
    temp_c = celsius_input.get()
    try:
        temp_c = float(temp_c)
        temp_f = (temp_c * (9/5)) + 32
        temp_f = round(temp_f, 2)
        if temp_f < -459.67:  # absolute zero in F
            temp_f = str(temp_f) + "°F"
            f_out.set("Invalid input, temperature is\nbelow absolute zero. ({} < 459.67°F)".format(temp_f))
            return  # ends the subroutine
        temp_f = str(temp_f) + "°F"
        f_out.set(temp_f)
        temp_c = str(temp_c) + "°C"
        history[temp_c] = temp_f
        print(history)
    except ValueError:
        f_out.set("Please input a number")


def help_window_func():
    help_window = Toplevel(root)
    help_window.title("Help")
    help_label = ttk.Label(help_window, text="Temp Converter Help\n Input a number in either box and press the corresponding 'Convert' button\n ")
    help_label.grid()



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

help_button = ttk.Button(main_frame, text="Help", command=help_window_func)
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
