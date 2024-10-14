import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    try:
        with open(filepath, "r") as input_file:
            text = input_file.read()
            txt_edit.insert(tk.END, text)
        window.title(f"text_editor (app project) - {filepath}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open file: {e}")

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    try:
        with open(filepath, "w") as output_file:
            text = txt_edit.get(1.0, tk.END)
            output_file.write(text)
        window.title(f"text_editor (app project) - {filepath}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save file: {e}")

def toggle_edit():
    """Toggle between editable and read-only mode."""
    if txt_edit.cget("state") == "normal":
        txt_edit.config(state="disabled")
        btn_edit.config(text="Edit")
    else:
        txt_edit.config(state="normal")
        btn_edit.config(text="Read Only")

def show_file_info():
    """Display file information."""
    messagebox.showinfo("File Info", "This function would handle file-related tasks.")

def show_view_info():
    """Display view information."""
    messagebox.showinfo("View Info", "This function would handle view-related tasks.")

def show_help():
    """Display help information."""
    messagebox.showinfo("Help", "This is a simple text editor. Use 'Open' to open a file and 'Save As...' to save your work.")

window = tk.Tk()
window.title("text_editor (app project)")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)

btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)
btn_edit = tk.Button(fr_buttons, text="Edit", command=toggle_edit)
btn_file = tk.Button(fr_buttons, text="File", command=show_file_info)
btn_view = tk.Button(fr_buttons, text="View", command=show_view_info)
btn_help = tk.Button(fr_buttons, text="Help", command=show_help)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
btn_edit.grid(row=2, column=0, sticky="ew", padx=5)
btn_file.grid(row=3, column=0, sticky="ew", padx=5)
btn_view.grid(row=4, column=0, sticky="ew", padx=5)
btn_help.grid(row=5, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()
