import tkinter as tk
from tkinter import ttk
import sys

sys.setrecursionlimit(1500)  # Or higher, as needed
import sv_ttk

# Main app window
root = tk.Tk()
root.overrideredirect(True)  # Remove window decorations (title bar, borders)
root.title("Trading Bot")
root.geometry("1250x750")
root.resizable(True, True)  # Allow resizing
sv_ttk.set_theme("dark")

# Configure root grid for proper resizing
root.grid_rowconfigure(0, weight=0)  # Title bar
root.grid_rowconfigure(1, weight=1)  # Center content
root.grid_rowconfigure(2, weight=0)  # Bottom section (alerts, analysis)
root.grid_columnconfigure(0, weight=1)  # Sidebar left
root.grid_columnconfigure(1, weight=3)  # Center chart
root.grid_columnconfigure(2, weight=1)  # Sidebar right

# Title bar
title_bar = tk.Frame(root, bg="#333333", relief='raised', bd=0, height=30)
title_bar.grid(row=0, column=0, columnspan=3, sticky="new")

title_label = tk.Label(title_bar, text="Smart Money Concept Trading Bot", bg="#333333", fg="white")
title_label.pack(side=tk.LEFT, padx=10)

close_button = tk.Button(title_bar, text="✕", bg="#333333", fg="white", borderwidth=0, command=root.destroy)
close_button.pack(side=tk.RIGHT, padx=10)

def move_window(event):
    root.geometry(f"+{event.x_root}+{event.y_root}")

title_bar.bind("<B1-Motion>", move_window)
title_label.bind("<B1-Motion>", move_window)

# Styles
style = ttk.Style()
style.configure("Sidebar.TFrame", background="#333333")
style.configure("SidebarButton.TButton", background="#1d9bf5", foreground="white")
style.configure("SidebarLabel.TLabel", foreground="white", background="#333333")

def toggle_pairs_menu():
    if pairs_menu.winfo_ismapped():
        pairs_menu.grid_forget()
    else:
        pairs_menu.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

def update_rrr(value=None):
    try:
        rrr_value = float(value) if value else rrr_slider.get()
        rrr_value = max(1, min(10, rrr_value))
        current_value = rrr_slider.get()
        if rrr_value != current_value:
            rrr_display.config(text=f"RRR: {rrr_value}:1")
            rrr_slider.set(int(rrr_value))
    except ValueError:
        print("Invalid input for RRR.")

# Left Sidebar Tabs
tabs_frame = ttk.Frame(root, width=200, style="Sidebar.TFrame")
tabs_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

toggle_pairs_button = ttk.Button(tabs_frame, text="Toggle Pairs Menu", command=toggle_pairs_menu, style="SidebarButton.TButton")
toggle_pairs_button.grid(row=0, column=0, padx=10, pady=10)

backtesting_button = ttk.Button(tabs_frame, text="Backtesting", width=20, style="SidebarButton.TButton")
backtesting_button.grid(row=1, column=0, padx=10, pady=10)

live_trading_button = ttk.Button(tabs_frame, text="Live Trading", width=20, style="SidebarButton.TButton")
live_trading_button.grid(row=2, column=0, padx=10, pady=10)

alerts_button = ttk.Button(tabs_frame, text="Alerts", width=20, style="SidebarButton.TButton")
alerts_button.grid(row=3, column=0, padx=10, pady=10)

# Pairs Menu (Collapsible)
pairs_menu = ttk.Frame(root, width=200, relief="solid")
pairs_list = ["SOLUSD", "XAUUSD", "EURUSD", "BTCUSD", "GBPUSD"]
for i, pair in enumerate(pairs_list):
    btn = ttk.Button(pairs_menu, text=pair, width=20, style="SidebarButton.TButton")
    btn.grid(row=i, column=0, padx=10, pady=5)

# Center Chart Frame
chart_frame = tk.Frame(root, width=700, height=600, relief="solid", borderwidth=2)
chart_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
chart_frame.grid_propagate(True)  # Allow chart to resize with the window

chart_label = tk.Label(chart_frame, text="Interactive Chart Here", font=("Helvetica", 16), width=60, height=30)
chart_label.grid(row=0, column=0, padx=10, pady=10)

# Right Sidebar
sidebar_frame = ttk.Frame(root, width=300, style="Sidebar.TFrame")
sidebar_frame.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")
sidebar_frame.grid_propagate(True)  # Allow sidebar to resize with the window

trade_info_label = ttk.Label(sidebar_frame, text="Trade Info", font=("Helvetica", 16), style="SidebarLabel.TLabel")
trade_info_label.grid(row=0, column=0, padx=10, pady=10)

sl_tp_label = tk.Label(sidebar_frame, text="SL: $0 | TP: $0 | Entry: $0", bg="#555555", fg="white", font=("Helvetica", 12))
sl_tp_label.grid(row=1, column=0, padx=10, pady=10)

rrr_label = ttk.Label(sidebar_frame, text="Risk-to-Reward Ratio", font=("Helvetica", 12), style="SidebarLabel.TLabel")
rrr_label.grid(row=2, column=0, padx=10, pady=10)

rrr_display = tk.Label(sidebar_frame, text="1:1", font=("Helvetica", 14), bg="#444444", fg="white")
rrr_display.grid(row=3, column=0, padx=10, pady=10)

rrr_slider = ttk.Scale(sidebar_frame, from_=1, to=10, orient="horizontal", command=update_rrr)
rrr_slider.set(1)
rrr_slider.grid(row=4, column=0, padx=10, pady=10)

rrr_entry = ttk.Entry(sidebar_frame, font=("Helvetica", 12))
rrr_entry.grid(row=5, column=0, padx=10, pady=10)
rrr_entry.insert(0, "1")

def update_rrr_from_entry(event):
    update_rrr(rrr_entry.get())

rrr_entry.bind("<Return>", update_rrr_from_entry)  # Update RRR when 'Enter' is pressed

lot_size_label = ttk.Label(sidebar_frame, text="Custom Lot Size", font=("Helvetica", 12), style="SidebarLabel.TLabel")
lot_size_label.grid(row=6, column=0, padx=10, pady=10)

lot_size_entry = ttk.Entry(sidebar_frame, font=("Helvetica", 12))
lot_size_entry.grid(row=7, column=0, padx=10, pady=10)

def calculate_lot_size():
    risk_percent = 0.05
    account_balance = 1000
    risk_amount = account_balance * risk_percent
    rrr_value = rrr_slider.get()
    lot_size = risk_amount / (rrr_value * 100)
    lot_size_entry.delete(0, tk.END)
    lot_size_entry.insert(0, str(round(lot_size, 2)))

calc_button = ttk.Button(sidebar_frame, text="Calculate Lot Size", command=calculate_lot_size, style="SidebarButton.TButton")
calc_button.grid(row=8, column=0, padx=10, pady=10)

# Trading Session Dropdown
session_frame = ttk.Frame(root, width=500, height=50, relief="solid")
session_frame.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
session_frame.grid_propagate(True)

session_label = ttk.Label(session_frame, text="Select Trading Session", font=("Helvetica", 12))
session_label.grid(row=0, column=0, padx=10, pady=10)

session_var = tk.StringVar()
session_dropdown = ttk.Combobox(session_frame, textvariable=session_var, values=["NY Session", "London Session", "Asian Session"])
session_dropdown.set("NY Session")
session_dropdown.grid(row=0, column=1, padx=10, pady=10)

# Analysis & Alerts
alert_label = ttk.Label(root, text="Live Alerts: No active alerts", font=("Helvetica", 14), foreground="lightgreen")
alert_label.grid(row=3, column=1, padx=10, pady=10)

analysis_label = ttk.Label(root, text="Trade Analysis: ", font=("Helvetica", 14))
analysis_label.grid(row=4, column=1, padx=10, pady=10)

def analyze_trade():
    analysis_label.config(text="Trade Setup: Bullish (BOS, FVG, 3 confluences met)")

analyze_button = ttk.Button(root, text="Analyze Trade", command=analyze_trade, style="SidebarButton.TButton")
analyze_button.grid(row=5, column=1, padx=10, pady=10)

# Alerts Window (new instance)
def open_alerts_window():
    alert_window = tk.Toplevel(root)
    alert_window.title("Trade Alert")
    alert_window.geometry("300x200")
    alert_window.resizable(False, False)

    alert_label = tk.Label(alert_window, text="Pair: XAUUSD\nConfluences: FVG, BOS, Liquidity Sweep", font=("Helvetica", 12))
    alert_label.pack(padx=20, pady=20)

    close_alert_button = tk.Button(alert_window, text="Close", command=alert_window.destroy)
    close_alert_button.pack(pady=10)

# Trigger alerts window from the Alerts button
alerts_button.config(command=open_alerts_window)

# Run the app
root.mainloop()
