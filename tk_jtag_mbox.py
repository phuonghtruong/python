import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def send_command():
    """_summary_
    """
    command = command_entry.get()
    input_data = input_data_entry.get()
    argument = argument_entry.get()

    if not command:
        messagebox.showerror("Error", "Command cannot be empty.")
        return

    # Simulating the response and output data generation
    # Replace this with actual JTAG mailbox communication logic
    try:
        response = f"Response for Command: {command}, Argument: {argument}"
        output_data = f"Processed Input Data: {input_data}"

        response_label.config(text=response)
        output_data_label.config(text=output_data)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


# Function to handle the selection and display the output
def execute_command():
    """_summary_
    """
    selected_command = command_var.get()
    if selected_command:
        output_text.configure(state="normal")  # Enable editing to update the text
        output_text.delete(1.0, tk.END)  # Clear any existing text
        output_text.insert(
            tk.END, f"Executing: {selected_command}\n"
        )  # Insert the output text
        output_text.configure(state="disabled")  # Disable editing
    else:
        output_text.configure(state="normal")
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Please select a command!\n")
        output_text.configure(state="disabled")


# Create the main application window
root = tk.Tk()
root.title("JTAG Mailbox Command Interface")
root.geometry("1000x3000")

# Command Input
# Dropdown menu (Combobox)
command_label = tk.Label(root, text="JTAG Command:")
command_label.pack(pady=5)
command_var = tk.StringVar()
commands = [
    "READ DEVICE SERIAL NUMBER",
    "CRYPTO READY",
    "COMMIT_BOOTCFG",
    "TEST_BOOTCFG",
    "DOWNLOAD_FKEY",
    "DOWNLOAD_KEY",
    "GET_LOG",
]
command_combobox = ttk.Combobox(
    root,
    textvariable=command_var,
    values=commands,
    state="readonly",
    font=("Arial", 10),
    width=50,
)
command_combobox.pack(pady=10)

# Input Data
input_data_label = tk.Label(root, text="Input Data:")
input_data_label.pack(pady=5)
input_data_entry = tk.Entry(root, width=50)
input_data_entry.pack(pady=5)

# Argument
argument_label = tk.Label(root, text="Argument:")
argument_label.pack(pady=5)
argument_entry = tk.Entry(root, width=50)
argument_entry.pack(pady=5)

# Submit Button
submit_button = tk.Button(root, text="Send Command", command=execute_command)
submit_button.pack(pady=10)

# Response
response_label = tk.Label(
    root, text="Response will be displayed here.", wraplength=380, justify="left"
)
response_label.pack(pady=5)

# Output Data
output_label = tk.Label(
    root, text="Output data will be displayed here.", wraplength=380, justify="left"
)
output_label.pack(pady=5)
output_text = tk.Text(root, height=5, bg="black", fg="white", font=("Courier", 12))
output_text.pack(pady=10, fill="x")
output_text.configure(state="disabled")  # Initially set to read-only

# Run the application
root.mainloop()
