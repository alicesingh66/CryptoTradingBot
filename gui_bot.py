import tkinter as tk
from tkinter import messagebox
from basic_bot import BasicBot


def place_order():
    try:
        api_key = api_key_entry.get().strip()
        api_secret = api_secret_entry.get().strip()
        symbol = symbol_entry.get().upper()
        side = side_var.get()
        order_type = order_type_var.get()
        quantity = float(quantity_entry.get())
        price = price_entry.get()

        if not api_key or not api_secret:
            raise ValueError("API key and secret are required")

        bot = BasicBot(api_key, api_secret)

        # Mandatory for futures
        bot.set_leverage(symbol, leverage=1)

        if order_type == "MARKET":
            order = bot.place_market_order(symbol, side, quantity)
        else:
            if not price:
                raise ValueError("Price required for LIMIT order")
            order = bot.place_limit_order(symbol, side, quantity, float(price))

        output_text.set(
            f"Order Placed Successfully!\n"
            f"Symbol: {order.get('symbol')}\n"
            f"Side: {order.get('side')}\n"
            f"Type: {order.get('type')}\n"
            f"Status: {order.get('status')}\n"
            f"Order ID: {order.get('orderId', 'Not returned')}"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))


# -------------------- UI --------------------
root = tk.Tk()
root.title("Binance Futures Testnet Bot")
root.geometry("420x520")

tk.Label(root, text="API Key").pack()
api_key_entry = tk.Entry(root, width=50)
api_key_entry.pack()

tk.Label(root, text="API Secret").pack()
api_secret_entry = tk.Entry(root, width=50, show="*")
api_secret_entry.pack()

tk.Label(root, text="Symbol (e.g. ETHUSDT)").pack()
symbol_entry = tk.Entry(root)
symbol_entry.pack()

tk.Label(root, text="Side").pack()
side_var = tk.StringVar(value="BUY")
tk.OptionMenu(root, side_var, "BUY", "SELL").pack()

tk.Label(root, text="Order Type").pack()
order_type_var = tk.StringVar(value="MARKET")
tk.OptionMenu(root, order_type_var, "MARKET", "LIMIT").pack()

tk.Label(root, text="Quantity").pack()
quantity_entry = tk.Entry(root)
quantity_entry.pack()

tk.Label(root, text="Price (for LIMIT only)").pack()
price_entry = tk.Entry(root)
price_entry.pack()

tk.Button(root, text="Place Order", command=place_order).pack(pady=10)

output_text = tk.StringVar()
tk.Label(root, textvariable=output_text, wraplength=380, justify="left").pack()

root.mainloop()
