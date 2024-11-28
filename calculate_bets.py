import tkinter as tk
from tkinter import ttk

def calculate_bets():
    try:
        # Get input values from the GUI
        total_bet = float(total_bet_entry.get())
        p1 = float(p1_entry.get())
        p2 = float(p2_entry.get())
        p3 = float(p3_entry.get())
        p4 = float(p4_entry.get())
        
        # Calculate weights and bets
        weights = [1 / p for p in [p1, p2, p3, p4]]
        total_weight = sum(weights)
        bets = [(weight / total_weight) * total_bet for weight in weights]
        uniform_payout = total_bet / total_weight
        profit = uniform_payout - total_bet
        
        # Display results in the output box
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"Uniform Payout: {uniform_payout:.2f}\n")
        output_text.insert(tk.END, f"Profit: {profit:.2f}\n\n")
        for i, bet in enumerate(bets, 1):
            output_text.insert(tk.END, f"Bet on outcome {i} (Payout {eval(f'p{i}'):.1f}x): {bet:.2f}\n")
    except Exception as e:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"Error: {str(e)}")

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

# Create a button to calculate bets
calculate_button = ttk.Button(root, text="Calculate Bets", command=calculate_bets)
calculate_button.grid(row=5, column=0, columnspan=2, pady=10)

# Create an output text box to display the results
output_text = tk.Text(root, height=10, width=50)
output_text.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

# Run the Tkinter main loop
root.mainloop()
