import tkinter as tk
from tkinter import ttk

def calculate_bets(event=None):
    try:
        # Get input values from the GUI
        total_bet = float(total_bet_entry.get())
        p1 = float(p1_entry.get())
        p2 = float(p2_entry.get())
        p3 = float(p3_entry.get())
        p4 = float(p4_entry.get())
        
        # Collect bets and payout multipliers dynamically
        payouts = [p1, p2, p3, p4]

        if hedge1_var.get():
            payouts.append(float(hedge1_entry.get()))
        if hedge2_var.get():
            payouts.append(float(hedge2_entry.get()))
        if hedge3_var.get():
            payouts.append(float(hedge3_entry.get()))

        # Calculate weights and bets
        weights = [1 / p for p in payouts]
        total_weight = sum(weights)
        bets = [(weight / total_weight) * total_bet for weight in weights]
        uniform_payout = total_bet / total_weight
        profit = uniform_payout - total_bet

        # Display results in the output box
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"Uniform Payout: {uniform_payout:.2f}\n")
        output_text.insert(tk.END, f"Profit: {profit:.2f}\n\n")
        for i, (bet, payout) in enumerate(zip(bets, payouts), 1):
            output_text.insert(tk.END, f"Bet on outcome {i} (Payout {payout:.1f}x): {bet:.2f}\n")
    except Exception as e:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"Error: {str(e)}")

# Show or hide hedge entry fields based on checkbox state
def toggle_hedge_input(var, entry):
    if var.get():
        entry.grid()
    else:
        entry.grid_remove()
    calculate_bets()

# Create the main Tkinter window
root = tk.Tk()
root.title("Equal Payout Bet Calculator")

# Create input labels and text boxes
ttk.Label(root, text="Total Bet:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
total_bet_entry = ttk.Entry(root)
total_bet_entry.grid(row=0, column=1, padx=5, pady=5)
total_bet_entry.insert(0, "1000")

ttk.Label(root, text="Payout Multiplier 1:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
p1_entry = ttk.Entry(root)
p1_entry.grid(row=1, column=1, padx=5, pady=5)
p1_entry.insert(0, "4.0")

ttk.Label(root, text="Payout Multiplier 2:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
p2_entry = ttk.Entry(root)
p2_entry.grid(row=2, column=1, padx=5, pady=5)
p2_entry.insert(0, "5.0")

ttk.Label(root, text="Payout Multiplier 3:").grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
p3_entry = ttk.Entry(root)
p3_entry.grid(row=3, column=1, padx=5, pady=5)
p3_entry.insert(0, "5.5")

ttk.Label(root, text="Payout Multiplier 4:").grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)
p4_entry = ttk.Entry(root)
p4_entry.grid(row=4, column=1, padx=5, pady=5)
p4_entry.insert(0, "7.5")

# Optional hedge bets
def create_hedge_input(row, label_text, var):
    checkbox = ttk.Checkbutton(root, text=label_text, variable=var, command=lambda: toggle_hedge_input(var, entry))
    checkbox.grid(row=row, column=0, sticky=tk.W, padx=5, pady=5)
    entry = ttk.Entry(root)
    entry.grid(row=row, column=1, padx=5, pady=5)
    entry.insert(0, "10.0")
    entry.grid_remove()  # Initially hidden
    return entry

hedge1_var = tk.BooleanVar()
hedge1_entry = create_hedge_input(5, "Hedge 1:", hedge1_var)

hedge2_var = tk.BooleanVar()
hedge2_entry = create_hedge_input(6, "Hedge 2:", hedge2_var)

hedge3_var = tk.BooleanVar()
hedge3_entry = create_hedge_input(7, "Hedge 3:", hedge3_var)

# Bind the calculate_bets function to the entry fields for real-time updates
total_bet_entry.bind("<KeyRelease>", calculate_bets)
p1_entry.bind("<KeyRelease>", calculate_bets)
p2_entry.bind("<KeyRelease>", calculate_bets)
p3_entry.bind("<KeyRelease>", calculate_bets)
p4_entry.bind("<KeyRelease>", calculate_bets)
hedge1_entry.bind("<KeyRelease>", calculate_bets)
hedge2_entry.bind("<KeyRelease>", calculate_bets)
hedge3_entry.bind("<KeyRelease>", calculate_bets)

# Create an output text box to display the results
output_text = tk.Text(root, height=10, width=50)
output_text.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

# Call calculate_bets once to populate the textbox on first run
calculate_bets()

# Run the Tkinter main loop
root.mainloop()
