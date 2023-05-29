from tkinter import *
from tkinter import ttk
import os
import pandas as pd
import time

history = {"Input": "Output"}  # input/output for .csv convenience


def c_convert_func():  # converts the input to a fahrenheit output
    temp_f = fahrenheit_input.get()
    try:
        temp_f = float(temp_f)
        temp_c = (temp_f - 32) * (5 / 9)
        temp_c = round(temp_c, 2)
        if temp_c < -273.15:  # absolute zero in C
            temp_c = str(temp_c) + "°C"
            c_out.set("Invalid input, temperature is\nbelow absolute zero.\n({} < 273.15°C)".format(temp_c))
            return  # ends the subroutine
        temp_c = str(temp_c) + "°C"
        c_out.set(temp_c)
        temp_f = str(temp_f) + "°F"
        history[temp_f] = temp_c  # sets a new input temperature in the dictionary with the value of the output
    except ValueError:
        c_out.set("Please input a number")


def f_convert_func():  # converts the input to a celsius output
    temp_c = celsius_input.get()
    try:
        temp_c = float(temp_c)
        temp_f = (temp_c * (9 / 5)) + 32
        temp_f = round(temp_f, 2)
        if temp_f < -459.67:  # absolute zero in F
            temp_f = str(temp_f) + "°F"
            f_out.set("Invalid input, temperature is\nbelow absolute zero. ({} < 459.67°F)".format(temp_f))
            return  # ends the subroutine
        temp_f = str(temp_f) + "°F"
        f_out.set(temp_f)
        temp_c = str(temp_c) + "°C"
        history[temp_c] = temp_f  # sets a new input temperature in the dictionary with the value of the output
    except ValueError:
        f_out.set("Please input a number")


def help_window_func():
    def close_help():
        help_window.destroy()

    help_window = Toplevel(root)  # creates new window
    help_window.title("Help")
    help_frame = ttk.LabelFrame(help_window)
    help_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")
    help_label = ttk.Label(help_frame, text="Temp Converter Help\n"  # all the text for the help menu
                                            "Input a number in either box and press the corresponding 'Convert' button\n"
                                            "to convert temperatures.\n\n"
                                            "Press 'export as .csv' to export the temperatures recorded.\n"
                                            "This file will export to the local directory at: \n"
                                            "{0}\n\n"
                                            "Press 'History' to view the program's conversion history. "
                                            "This is the exported data. \n\n"
                                            "Pressing the 'Help' button brings up this menu.\n\n"
                                            "Pressing the 'Exit' button will close the program without saving.\n"
                                            "Warning: All non-exported data will be lost."
                           .format(os.path.dirname(os.path.realpath(__file__)))
                           )
    help_label.grid()
    close_help_button = ttk.Button(help_window, text="Dismiss", command=close_help)
    close_help_button.grid(row=1, column=0, padx=10, pady=10)


def history_box_func():
    def close_history():
        history_window.destroy()

    history_window = Toplevel(root)  # creates new window
    history_window.title("History")
    history_frame = ttk.LabelFrame(history_window)
    history_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

    history_input = Listbox(history_frame)
    history_input.grid(row=1, column=0)
    history_input.insert(0, *list(history.keys()))

    history_output = Listbox(history_frame)
    history_output.grid(row=1, column=1)
    history_output.insert(0, *list(history.values()))

    close_history = ttk.Button(history_window, text="Dismiss", command=close_history)
    close_history.grid(row=2, column=0)


def exit_program():
    exit("Closed program.")


def export_csv():  # function called by button to export
    global history
    output = pd.DataFrame(history, index=[0])  # saves dictionary to output in 'panda-speak'
    output.to_csv("history.csv", encoding="utf-8-sig")  # outputs to history.csv locally into the program directory
    history = {}
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    export_complete = ttk.Label(main_frame, text="Export completed at [{}]".format(current_time))
    export_complete.grid(row=3, column=1, padx=10, pady=10)


root = Tk()
root.title("Temperature Converter")
# create all buttons
main_frame = ttk.LabelFrame(root)
main_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

f_convert_button = ttk.Button(main_frame, text="Convert to fahrenheit", command=f_convert_func)
f_convert_button.grid(row=1, column=0, padx=10, pady=10)

c_convert_button = ttk.Button(main_frame, text="Convert to celsius", command=c_convert_func)
c_convert_button.grid(row=1, column=1, padx=10, pady=10)

exit_button = ttk.Button(main_frame, text="Exit", command=exit_program)
exit_button.grid(row=0, column=4, padx=10, pady=10)

export_button = ttk.Button(main_frame, text="Export as .csv", command=export_csv)
export_button.grid(row=3, column=0, padx=10, pady=10)

help_button = ttk.Button(main_frame, text="Help", command=help_window_func)
help_button.grid(row=3, column=4, padx=10, pady=10)

conversion_history = ttk.Button(main_frame, text="History", command=history_box_func)
conversion_history.grid(row=2, column=4, padx=10, pady=10)

celsius_input = ttk.Entry(main_frame)
celsius_input.grid(row=0, column=0, padx=10, pady=10)

fahrenheit_input = ttk.Entry(main_frame)
fahrenheit_input.grid(row=0, column=1, padx=10, pady=10)

f_out = StringVar()
f_out.set("0°F")
fahrenheit_output = ttk.Label(main_frame, textvariable=f_out)
fahrenheit_output.grid(row=2, column=0)

c_out = StringVar()
c_out.set("0°C")
celsius_output = ttk.Label(main_frame, textvariable=c_out)
celsius_output.grid(row=2, column=1)

root.mainloop()
