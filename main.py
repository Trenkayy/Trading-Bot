#Trading Bot
#2025

import tkinter as tk
from tkinter import ttk
import sys

sys.setrecursionlimit(1500)  # Or higher, as needed
import sv_ttk

# Main app window
root = tk.Tk()
root.title("Smart Money Concept Trading Bot")
root.geometry("1250x750")
sv_ttk.set_theme("dark")

# Create custom style for the sidebar frame and other elements
style = ttk.Style()

# Define a custom style for the sidebar frame
style.configure("Sidebar.TFrame", background="#333333")

# Define a custom style for buttons and labels with a background color
style.configure("SidebarButton.TButton", background="#1d9bf5", foreground="white")
style.configure("SidebarLabel.TLabel", foreground="white", background="#333333")

# Function to toggle pairs menu visibility
def toggle_pairs_menu():
    if pairs_menu.winfo_ismapped():
        pairs_menu.grid_forget()
    else:
        pairs_menu.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Function to update RRR based on the slider or text box
def update_rrr(value=None):
    try:
        # If a value is passed, use it. Otherwise, use the slider value
        rrr_value = float(value) if value else rrr_slider.get()

        # Ensure the value is within the slider's range
        if rrr_value < 1:
            rrr_value = 1
        elif rrr_value > 10:
            rrr_value = 10

        # Only update if the new value is different
        current_value = rrr_slider.get()
        if rrr_value != current_value:
            # Update the RRR display label and slider value
            rrr_display.config(text=f"RRR: {rrr_value}:1")
            rrr_slider.set(int(rrr_value))  # Set slider with integer value

    except ValueError:
        # In case of invalid value input (non-numeric input in the text box)
        print("Invalid input for RRR.")

# Main Frame (left vertical tab menu)
main_frame = ttk.Frame(root, width=200, height=800)
main_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Sidebar (Right side for SL, TP, Entry) using the custom style
sidebar_frame = ttk.Frame(root, width=300, height=800, relief="solid", style="Sidebar.TFrame")
sidebar_frame.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

# Frame for the interactive chart (Center) with border
chart_frame = tk.Frame(root, width=1000, height=600, relief="solid", borderwidth=2)  # Use tk.Frame instead of ttk.Frame
chart_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

# Chart Panel Placeholder (will later use TradingView chart)
chart_label = tk.Label(chart_frame, text="Interactive Chart Here", font=("Helvetica", 16), width=60, height=30)
chart_label.grid(row=0, column=0, padx=10, pady=10)

# Sidebar: SL, TP, Entry, and RRR info (combined display)
trade_info_label = ttk.Label(sidebar_frame, text="Trade Info", font=("Helvetica", 16), anchor="w", padding=(10, 10), style="SidebarLabel.TLabel")
trade_info_label.grid(row=0, column=0, padx=10, pady=10)

# SL, TP, Entry info in the sidebar
sl_tp_label = tk.Label(sidebar_frame, text="SL: $0 | TP: $0 | Entry: $0", background="#555555", font=("Helvetica", 12), fg="white")  # Darker background for better visibility
sl_tp_label.grid(row=1, column=0, padx=10, pady=10)

# Risk-to-Reward Ratio Display
rrr_label = ttk.Label(sidebar_frame, text="Risk-to-Reward Ratio", font=("Helvetica", 12), style="SidebarLabel.TLabel")
rrr_label.grid(row=2, column=0, padx=10, pady=10)

# Dynamic RRR Display
rrr_display = tk.Label(sidebar_frame, text="1:1", font=("Helvetica", 14), background="#444444", foreground="white")
rrr_display.grid(row=3, column=0, padx=10, pady=10)

# RRR Slider (Update function on change)
rrr_slider = ttk.Scale(sidebar_frame, from_=1, to=10, orient="horizontal", command=update_rrr)
rrr_slider.set(1)
rrr_slider.grid(row=4, column=0, padx=10, pady=10)

# Manual RRR Entry Box
rrr_entry = ttk.Entry(sidebar_frame, font=("Helvetica", 12))
rrr_entry.grid(row=5, column=0, padx=10, pady=10)
rrr_entry.insert(0, "1")  # Default RRR value

# Risk Management: Custom Lot Size Entry
lot_size_label = ttk.Label(sidebar_frame, text="Custom Lot Size", font=("Helvetica", 12), style="SidebarLabel.TLabel")
lot_size_label.grid(row=7, column=0, padx=10, pady=10)

lot_size_entry = ttk.Entry(sidebar_frame, font=("Helvetica", 12))
lot_size_entry.grid(row=8, column=0, padx=10, pady=10)

# Calculate Lot Size Button
def calculate_lot_size():
    risk_percent = 0.05  # Assume 5% risk
    account_balance = 1000  # Placeholder
    risk_amount = account_balance * risk_percent
    rrr_value = rrr_slider.get()
    lot_size = risk_amount / (rrr_value * 100)
    lot_size_entry.delete(0, tk.END)
    lot_size_entry.insert(0, str(round(lot_size, 2)))

calc_button = ttk.Button(sidebar_frame, text="Calculate Lot Size", command=calculate_lot_size, style="SidebarButton.TButton")
calc_button.grid(row=9, column=0, padx=10, pady=10)

# Toggle Pairs Menu Button
toggle_pairs_button = ttk.Button(main_frame, text="Toggle Pairs Menu", command=toggle_pairs_menu, style="SidebarButton.TButton")
toggle_pairs_button.grid(row=0, column=0, padx=10, pady=10)

# Pairs Menu (collapsible menu for selecting pairs)
pairs_menu = ttk.Frame(root, width=200, height=400, relief="solid")
pairs_menu.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
pairs_list = ["SOLUSD", "XAUUSD", "EURUSD", "BTCUSD", "GBPUSD"]
for i, pair in enumerate(pairs_list):
    pair_button = ttk.Button(pairs_menu, text=pair, width=20, style="SidebarButton.TButton")
    pair_button.grid(row=i, column=0, padx=10, pady=5)

# Trading Session Dropdown (on top of the screen)
session_frame = ttk.Frame(root, width=500, height=50, relief="solid")
session_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

session_label = ttk.Label(session_frame, text="Select Trading Session", font=("Helvetica", 12))
session_label.grid(row=0, column=0, padx=10, pady=10)

session_var = tk.StringVar()
session_dropdown = ttk.Combobox(session_frame, textvariable=session_var, values=["NY Session", "London Session", "Asian Session"])
session_dropdown.set("NY Session")  # Default session
session_dropdown.grid(row=0, column=1, padx=10, pady=10)

# Tabs on the left
tabs_frame = ttk.Frame(root, width=200, height=800, relief="solid", style="Sidebar.TFrame")  # Use style instead of background
tabs_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

backtesting_button = ttk.Button(tabs_frame, text="Backtesting", width=20, style="SidebarButton.TButton")
backtesting_button.grid(row=1, column=0, padx=10, pady=10)

live_trading_button = ttk.Button(tabs_frame, text="Live Trading", width=20, style="SidebarButton.TButton")
live_trading_button.grid(row=2, column=0, padx=10, pady=10)

alerts_button = ttk.Button(tabs_frame, text="Alerts", width=20, style="SidebarButton.TButton")
alerts_button.grid(row=3, column=0, padx=10, pady=10)

# Bot Notifications (example)
alert_label = ttk.Label(root, text="Live Alerts: No active alerts", font=("Helvetica", 14), foreground="lightgreen")
alert_label.grid(row=1, column=1, padx=10, pady=10)

# Function to Analyze Trades based on selected pairs
def analyze_trade():
    analysis_label.config(text="Trade Setup: Bullish (BOS, FVG, 3 confluences met)")

analyze_button = ttk.Button(root, text="Analyze Trade", command=analyze_trade, style="SidebarButton.TButton")
analyze_button.grid(row=2, column=1, padx=10, pady=20)

# Analysis feedback label
analysis_label = ttk.Label(root, text="Trade Analysis: ", font=("Helvetica", 14))
analysis_label.grid(row=2, column=1, padx=10, pady=10)

# Start the app
root.mainloop()
 
