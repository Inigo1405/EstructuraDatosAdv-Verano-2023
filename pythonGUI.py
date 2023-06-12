import tkinter as tk
from estructurasLineales.pila import Pila

# Create the main window
root = tk.Tk()

# Set the window title
root.title("Python GUI - TEST")

# Set the window dimensions
root.geometry("600x500")

username = tk.StringVar()
pila= Pila()
pila.push('Iñigo')
pila.push(8)



def submit():
    print(username.get())
    if username.get():
        tk.Label(root, text=username.get()).pack()
    else:
        tk.Label(root, text=pila.display()).pack()
    
    username.set("")


# Create a Label widget
tk.Label(root, text="Hello, world!").pack()

tk.Button(root, text="Click me!", command = submit).pack() 
tk.Checkbutton(root).pack() 


tk.Entry(justify=tk.LEFT, textvariable=username).pack()



# Pack the Label widget to display it on the window
# label.pack()

# Start the main event loop
root.mainloop()




