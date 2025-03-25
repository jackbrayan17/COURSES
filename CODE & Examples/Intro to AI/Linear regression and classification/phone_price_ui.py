import tkinter as tk
from tkinter import ttk

class PhonePriceUI(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.brand_var = tk.StringVar()
        self.os_var = tk.StringVar()
        self.screen_size_var = tk.StringVar()
        self.four_g_var = tk.StringVar()
        self.five_g_var = tk.StringVar()
        self.rear_camera_var = tk.StringVar()
        self.front_camera_var = tk.StringVar()
        self.internal_memory_var = tk.StringVar()
        self.ram_var = tk.StringVar()
        self.battery_var = tk.StringVar()
        self.weight_var = tk.StringVar()
        self.release_year_var = tk.StringVar()
        self.days_used_var = tk.StringVar()

        features = ["device_brand", "os", "screen_size", "4g", "5g", "rear_camera_mp", "front_camera_mp", "internal_memory", "ram", "battery", "weight", "release_year", "days_used"]
        feature_groups = [
            ("device_brand", "os"),
            ("screen_size", "4g", "5g"),
            ("rear_camera_mp", "front_camera_mp"),
            ("internal_memory", "ram"),
            ("battery", "weight"),
            ("release_year", "days_used")
        ]

    def create_row(self, feature_group):
        frame = ttk.Frame(self)

        for i, column in enumerate(feature_group):
            _frame = ttk.Frame(frame)
            _frame.grid(row=0, column=i)


    def create_input(self, parent, label, variable, input_type="entry", values=None):
        frame_inner = ttk.Frame(parent)
        frame_inner.pack(fill="x", pady=5)

        ttk.Label(frame_inner, text=label).pack(anchor="w")
        if input_type == "combobox":
            widget = ttk.Combobox(frame_inner, textvariable=variable, values=values)
        else:
            widget = ttk.Entry(frame_inner, textvariable=variable)
        
        widget.pack(fill="x")
    