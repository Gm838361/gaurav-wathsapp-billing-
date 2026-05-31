import tkinter as tk
from tkinter import messagebox
import pywhatkit as kit
import pyautogui as pg  # 🤖 यह दबाएगा खुद 'Enter' बटन!
import time

class RealAutoWhatsAppBillingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🧾 GAURAV 100% AUTOMATIC INVOICER")
        self.root.geometry("650x550+350+100")
        self.root.configure(bg="#0A0915")

        self.cart = []
        self.items_preset = {
            "Laptop Stand": 850,
            "Ceramic Coffee Mug": 350,
            "Wireless Mouse": 499,
            "Gaming Keyboard": 1299
        }

        # --- 👑 हेडर ---
        tk.Label(root, text="🤖 GAURAV FULLY AUTO-BILLING", bg="#0A0915", fg="#00E676", font=("Arial", 18, "bold")).pack(pady=10)

        # --- 📱 कस्टमर डिटेल्स ---
        cust_frame = tk.Frame(root, bg="#1E222B", bd=1, relief="solid", padx=10, pady=10)
        cust_frame.pack(fill="x", padx=20, pady=5)

        tk.Label(cust_frame, text="Customer WhatsApp No (With +91):", bg="#1E222B", fg="white", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w")
        self.phone_entry = tk.Entry(cust_frame, width=25, font=("Arial", 10), bg="#2C3E50", fg="white", insertbackground="white")
        self.phone_entry.insert(0, "+9198XXXXXXXX")
        self.phone_entry.grid(row=0, column=1, padx=10)

        # --- 🛍️ आइटम सिलेक्शन ---
        item_frame = tk.Frame(root, bg="#1E222B", bd=1, relief="solid", padx=10, pady=10)
        item_frame.pack(fill="x", padx=20, pady=5)

        tk.Label(item_frame, text="Select Item:", bg="#1E222B", fg="white", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w")
        
        self.selected_item = tk.StringVar(root)
        self.selected_item.set("Laptop Stand")
        item_menu = tk.OptionMenu(item_frame, self.selected_item, *self.items_preset.keys())
        item_menu.config(bg="#2C3E50", fg="white", bd=0)
        item_menu.grid(row=0, column=1, padx=10)

        add_btn = tk.Button(item_frame, text="➕ Add to Invoice", bg="#27AE60", fg="white", font=("Arial", 10, "bold"), bd=0, padx=10, command=self.add_item)
        add_btn.grid(row=0, column=2, padx=10)

        # --- 📄 बिल रसीद एरिया ---
        self.bill_text = tk.Text(root, height=12, bg="#0E1117", fg="#FFFFFF", font=("Courier", 10, "bold"), bd=0, padx=10, pady=10)
        self.bill_text.pack(fill="both", expand=True, padx=20, pady=10)
        self.update_bill_display()

        # --- 🚀 व्हाट्सएप ऑटो बटन ---
        send_btn = tk.Button(root, text="🤖 SEND MESSAGE (100% AUTOMATIC) 🚀", bg="#00E676", fg="#000000", 
                             font=("Arial", 12, "bold"), bd=0, cursor="hand2", pady=10, command=self.send_automatic_whatsapp)
        send_btn.pack(fill="x", padx=20, pady=15)

    def add_item(self):
        item_name = self.selected_item.get()
        price = self.items_preset[item_name]
        self.cart.append({"name": item_name, "price": price})
        self.update_bill_display()

    def update_bill_display(self):
        self.bill_text.delete("1.0", tk.END)
        bill_content = "========================================\n"
        bill_content += "         GAURAV DIGITAL STORE          \n"
        bill_content += "          Jaipur, Rajasthan            \n"
        bill_content += "========================================\n"
        bill_content += f"{'Item Name':<25} {'Price':<10}\n"
        bill_content += "----------------------------------------\n"
        
        total = 0
        for item in self.cart:
            bill_content += f"{item['name']:<25} ₹{item['price']:<10}\n"
            total += item['price']
            
        bill_content += "----------------------------------------\n"
        bill_content += f"GRAND TOTAL:              ₹{total}\n"
        bill_content += "========================================\n"
        
        self.bill_text.insert(tk.END, bill_content)
        self.total_amount = total

    def send_automatic_whatsapp(self):
        phone = self.phone_entry.get().strip()
        if not phone.startswith("+91") or len(phone) != 13:
            messagebox.showerror("Error", "कृपया नंबर के आगे +91 ज़रूर लगाएँ भाई!")
            return
        if not self.cart:
            messagebox.showerror("Error", "बिल खाली है भाई!")
            return

        msg = f"📦 *GAURAV DIGITAL STORE INVOICE*\n\n"
        msg += f"Thank you for shopping! Here is your bill:\n"
        msg += f"----------------------------------------\n"
        for item in self.cart:
            msg += f"• {item['name']}: ₹{item['price']}\n"
        msg += f"----------------------------------------\n"
        msg += f"*💰 GRAND TOTAL: ₹{self.total_amount}*\n\n"
        msg += f"🎉 Have a great day!"

        messagebox.showinfo("Automation Active", "अलर्ट! ओके करने के बाद माउस-कीबोर्ड छोड़ देना भाई। 15 सेकंड में रोबोट खुद एंटर दबाकर मैसेज भेज देगा! 😎")
        
        # 1. यह ब्राउज़र में व्हाट्सएप चैट खोलेगा और मैसेज लिखेगा
        kit.sendwhatmsg_instantly(phone, msg, wait_time=15, tab_close=False)
        
        # 2. ⏳ हम 3 सेकंड और रुकेंगे ताकि चैट पूरी तरह सेट हो जाए
        time.sleep(3)
        
        # 3. 🔥 जादुई लाइन: पायथन खुद कीबोर्ड का 'Enter' बटन दबा देगा!
        pg.press("enter")

if __name__ == "__main__":
    root = tk.Tk()
    app = RealAutoWhatsAppBillingApp(root)
    root.mainloop()
