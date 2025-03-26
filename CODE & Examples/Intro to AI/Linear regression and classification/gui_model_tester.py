import tkinter as tk
from tkinter import ttk

import pickle
import numpy as np

phone_models = {
    "linear": "phone_model.pkl"
}

selected_model = phone_models['linear']

with open(selected_model, 'rb') as f:
    selected_model = pickle.load(f)

BRANDS = ['Honor', 'Others', 'HTC', 'Huawei', 'Infinix', 'Lava', 'Lenovo', 'LG',
       'Meizu', 'Micromax', 'Motorola', 'Nokia', 'OnePlus', 'Oppo', 'Realme',
       'Samsung', 'Vivo', 'Xiaomi', 'ZTE', 'Apple', 'Asus', 'Coolpad', 'Acer',
       'Alcatel', 'BlackBerry', 'Celkon', 'Gionee', 'Google', 'Karbonn',
       'Microsoft', 'Panasonic', 'Sony', 'Spice', 'XOLO']
OSs = ['Android', 'Others', 'iOS', 'Windows']

def get_brand_number(brand):
    return BRANDS.index(brand)

def get_os_number(os):
    return OSs.index(os)

def get_4g_number(string):
    return 0

def get_5g_number(string):
    return 0

# Function to simulate a model prediction
def predict_model():
    # Fetch input values in the form of a numpy array
    values = np.array([
        get_brand_number(brand_var.get()),
        get_os_number(os_var.get()),
        float(screen_size_var.get()),
        get_4g_number(four_g_var.get()),
        get_5g_number(five_g_var.get()),
        float(rear_camera_var.get()),
        float(front_camera_var.get()),
        float(internal_memory_var.get()),
        float(ram_var.get()),
        float(battery_var.get()),
        float(weight_var.get()),
        float(release_year_var.get()),
        float(days_used_var.get())
    ])

    # Use the collected numpy array to predict the outcome
    result = selected_model.predict(values.reshape(1, -1))
    print(result)

    prediction_result = f"The prediction for these values is: {result[0]}"
    
    # Display the result in the text area
    output_text.config(state=tk.NORMAL)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, prediction_result)
    output_text.config(state=tk.DISABLED)

# Initialize the main window
root = tk.Tk()
root.title("AI Model Tester")
root.geometry("600x900")

# Create a tabbed interface
notebook = ttk.Notebook(root)
tab_regression = ttk.Frame(notebook)
tab_classification = ttk.Frame(notebook)

notebook.add(tab_regression, text="Regression")
notebook.add(tab_classification, text="Classification")
notebook.pack(expand=True, fill="both")

# ============ Regression Tab UI ============
frame = ttk.Frame(tab_regression, padding=10)
frame.pack(fill="both", expand=True)

# Variables
brand_var = tk.StringVar(value="Huawei")
os_var = tk.StringVar(value="Android")
screen_size_var = tk.StringVar(value=5.7)
four_g_var = tk.StringVar(value="Yes")
five_g_var = tk.StringVar(value="No")
rear_camera_var = tk.StringVar(value="13")
front_camera_var = tk.StringVar(value="8")
internal_memory_var = tk.StringVar(value="4")
ram_var = tk.StringVar(value="3")
battery_var = tk.StringVar(value="4000")
weight_var = tk.StringVar(value="6.8")
release_year_var = tk.StringVar(value="2018")
days_used_var = tk.StringVar(value="1284")

# Function to create labeled inputs (label on top)
def create_input(label, variable, input_type="entry", values=None):
    frame_inner = ttk.Frame(frame)
    frame_inner.pack(fill="x", pady=5)

    ttk.Label(frame_inner, text=label).pack(anchor="w")  # Label on top
    if input_type == "combobox":
        widget = ttk.Combobox(frame_inner, textvariable=variable, values=values)
    else:
        widget = ttk.Entry(frame_inner, textvariable=variable)
    
    widget.pack(fill="x")

# Add fields
create_input("Device Brand", brand_var, "combobox", BRANDS)
create_input("OS", os_var, "combobox", OSs)
create_input("Screen Size (inches)", screen_size_var)
create_input("4G", four_g_var, "combobox", ["Yes", "No"])
create_input("5G", five_g_var, "combobox", ["Yes", "No"])
create_input("Rear Camera (MP)", rear_camera_var)
create_input("Front Camera (MP)", front_camera_var)
create_input("Internal Memory (GB)", internal_memory_var)
create_input("RAM (GB)", ram_var)
create_input("Battery (mAh)", battery_var)
create_input("Weight (g)", weight_var)
create_input("Release Year", release_year_var)
create_input("Days Used", days_used_var)

# Predict Button
predict_button = ttk.Button(frame, text="Predict", command=predict_model)
predict_button.pack(pady=10)

# Output Text Area
output_text = tk.Text(frame, height=5, width=70, state=tk.DISABLED)
output_text.pack(pady=5)

# ============ Classification Tab ============
frame_classification = ttk.Frame(tab_classification, padding=10)
frame_classification.pack(fill="both", expand=True)

ttk.Label(frame_classification, text="Classification model will be tested here...").pack()

# Run the Tkinter loop
root.mainloop()
