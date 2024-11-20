import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Hello World App")

# Set window size
root.geometry("300x200")

# Add a label
label = tk.Label(root, text="Hello, World!", font=("Arial", 16))
label.pack(pady=20)

# Add a button to close the app
close_button = tk.Button(root, text="Close", command=root.destroy)
close_button.pack(pady=10)

# Run the application
root.mainloop()
