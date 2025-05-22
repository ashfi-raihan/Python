import tkinter as tk    # for GUI
from time import strftime  # time and date

root = tk.Tk()  # root is a window to display our element
root.title("Ashfi's Digital Clock")



# Center the window using Chatgpt  
window_width = 550
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f'{window_width}x{window_height}+{x}+{y}')


 # to update time and date to display
def UpdateTime():
    string = strftime('%H:%M:%S %p \n %D')   # the p is for pm/am and is should be in small letter
    label.config(text=string)
    label.after(1000, UpdateTime)  # calls the time func every 1s

#label = tk.Label(root, font=("calibri", 50, 'bold'), background="yellow", foreground='black')
label = tk.Label(root, font=("DS-Digital", 70), background="black", foreground="cyan")  # chatgpt



# pack method is a method to arrage elements in the label 
label.pack(anchor='center')

UpdateTime()

# keeps the program running in a loop and waits for the user input
root.mainloop()