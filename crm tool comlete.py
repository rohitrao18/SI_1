from datetime import datetime, timedelta

class Customer:
    def __init__(self, customer_id, name, email, phone):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.interactions = []
        self.purchases = []
        self.last_contact_date = None
        self.score = 0  # Score to measure engagement level

    def add_interaction(self, interaction):
        """Log an interaction and update the last contact date."""
        self.interactions.append({
            "interaction": interaction,
            "date": datetime.now()
        })
        self.last_contact_date = datetime.now()

    def add_purchase(self, amount):
        """Record a purchase and increase the customer score."""
        self.purchases.append({
            "amount": amount,
            "date": datetime.now()
        })
        self.score += amount  # Increase score based on purchase amount

    def get_total_purchases(self):
        """Calculate total amount spent by the customer."""
        return sum(purchase["amount"] for purchase in self.purchases)

    def calculate_engagement_score(self):
        """Calculate a basic engagement score based on interactions and purchases."""
        interaction_score = len(self.interactions) * 10
        purchase_score = self.get_total_purchases() * 0.1
        self.score = interaction_score + purchase_score
        return self.score

    def get_details(self):
        """Return customer details, including interaction and purchase history."""
        return {
            "Customer ID": self.customer_id,
            "Name": self.name,
            "Email": self.email,
            "Phone": self.phone,
            "Total Purchases": self.get_total_purchases(),
            "Score": self.calculate_engagement_score(),
            "Interactions": self.interactions,
            "Purchases": self.purchases,
            "Last Contact Date": self.last_contact_date,
        }


class CRM:
    def __init__(self):
        self.customers = {}

    def add_customer(self, customer_id, name, email, phone):
        """Add a new customer to the CRM system."""
        if customer_id in self.customers:
            print("Customer ID already exists. Use a unique ID.")
        else:
            customer = Customer(customer_id, name, email, phone)
            self.customers[customer_id] = customer
            print(f"Customer {name} added successfully.")

    def record_interaction(self, customer_id, interaction):
        """Record an interaction with a specific customer."""
        if customer_id in self.customers:
            self.customers[customer_id].add_interaction(interaction)
            print("Interaction recorded.")
        else:
            print("Customer not found.")

    def record_purchase(self, customer_id, amount):
        """Record a purchase for a specific customer."""
        if customer_id in self.customers:
            self.customers[customer_id].add_purchase(amount)
            print(f"Purchase of ${amount} recorded.")
        else:
            print("Customer not found.")

    def get_customer_details(self, customer_id):
        """Retrieve a customer's details and interactions."""
        if customer_id in self.customers:
            return self.customers[customer_id].get_details()
        else:
            return "Customer not found."

    def search_customers(self, query):
        """Search customers by name or email."""
        results = []
        for customer in self.customers.values():
            if query.lower() in customer.name.lower() or query.lower() in customer.email.lower():
                results.append(customer.get_details())
        return results if results else "No matching customers found."

    def segment_customers(self):
        """Segment customers based on their engagement score."""
        high_value = []
        medium_value = []
        low_value = []
        
        for customer in self.customers.values():
            score = customer.calculate_engagement_score()
            if score >= 100:
                high_value.append(customer.get_details())
            elif score >= 50:
                medium_value.append(customer.get_details())
            else:
                low_value.append(customer.get_details())
        
        return {
            "High Value Customers": high_value,
            "Medium Value Customers": medium_value,
            "Low Value Customers": low_value
        }

    def follow_up_reminders(self, days=30):
        """List customers who haven't been contacted within the specified days."""
        reminders = []
        cutoff_date = datetime.now() - timedelta(days=days)
        
        for customer in self.customers.values():
            if customer.last_contact_date and customer.last_contact_date < cutoff_date:
                reminders.append(customer.get_details())
        
        return reminders

    def get_top_customers(self, top_n=5):
        """Return the top N customers based on engagement score."""
        sorted_customers = sorted(self.customers.values(), key=lambda c: c.calculate_engagement_score(), reverse=True)
        return [customer.get_details() for customer in sorted_customers[:top_n]]


# Example Usage
crm_system = CRM()

# Add customers
crm_system.add_customer(1, "Alice Johnson", "alice.johnson@example.com", "123-456-7890")
crm_system.add_customer(2, "Bob Smith", "bob.smith@example.com", "234-567-8901")

# Record interactions
crm_system.record_interaction(1, "Discussed product options")
crm_system.record_interaction(2, "Sent email about promotions")

# Record purchases
crm_system.record_purchase(1, 250)
crm_system.record_purchase(2, 150)

# Retrieve customer details
print(crm_system.get_customer_details(1))

# Segment customers
print("Customer Segments:")
print(crm_system.segment_customers())

# Follow-up reminders for customers not contacted in the last 30 days
print("Follow-up Reminders:")
print(crm_system.follow_up_reminders(30))

# Get top customers by engagement
print("Top Customers:")
print(crm_system.get_top_customers(2))
import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

# Existing Customer and CRM classes (shortened for readability)
class Customer:
    def __init__(self, customer_id, name, email, phone):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.interactions = []
        self.purchases = []
        self.last_contact_date = None
        self.score = 0

    def add_interaction(self, interaction):
        self.interactions.append({"interaction": interaction, "date": datetime.now()})
        self.last_contact_date = datetime.now()

    def add_purchase(self, amount):
        self.purchases.append({"amount": amount, "date": datetime.now()})
        self.score += amount

    def get_total_purchases(self):
        return sum(purchase["amount"] for purchase in self.purchases)

    def calculate_engagement_score(self):
        interaction_score = len(self.interactions) * 10
        purchase_score = self.get_total_purchases() * 0.1
        self.score = interaction_score + purchase_score
        return self.score

    def get_details(self):
        return {
            "Customer ID": self.customer_id,
            "Name": self.name,
            "Email": self.email,
            "Phone": self.phone,
            "Total Purchases": self.get_total_purchases(),
            "Score": self.calculate_engagement_score(),
            "Interactions": self.interactions,
            "Purchases": self.purchases,
            "Last Contact Date": self.last_contact_date,
        }

class CRM:
    def __init__(self):
        self.customers = {}

    def add_customer(self, customer_id, name, email, phone):
        if customer_id in self.customers:
            return "Customer ID already exists."
        else:
            self.customers[customer_id] = Customer(customer_id, name, email, phone)
            return "Customer added successfully."

    def record_interaction(self, customer_id, interaction):
        if customer_id in self.customers:
            self.customers[customer_id].add_interaction(interaction)
            return "Interaction recorded."
        else:
            return "Customer not found."

    def record_purchase(self, customer_id, amount):
        if customer_id in self.customers:
            self.customers[customer_id].add_purchase(amount)
            return f"Purchase of ${amount} recorded."
        else:
            return "Customer not found."

    def get_customer_details(self, customer_id):
        if customer_id in self.customers:
            return self.customers[customer_id].get_details()
        else:
            return "Customer not found."

    def get_top_customers(self, top_n=5):
        sorted_customers = sorted(self.customers.values(), key=lambda c: c.calculate_engagement_score(), reverse=True)
        return [customer.get_details() for customer in sorted_customers[:top_n]]


# Setting up the Tkinter UI
class CRMApp:
    def __init__(self, root):
        self.crm = CRM()
        self.root = root
        self.root.title("CRM System")
        self.root.geometry("600x400")

        # Labels and Entries for Customer Data
        self.customer_id_label = tk.Label(root, text="Customer ID:")
        self.customer_id_label.pack()
        self.customer_id_entry = tk.Entry(root)
        self.customer_id_entry.pack()

        self.name_label = tk.Label(root, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.email_label = tk.Label(root, text="Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(root)
        self.email_entry.pack()

        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_label.pack()
        self.phone_entry = tk.Entry(root)
        self.phone_entry.pack()

        # Buttons
        self.add_customer_button = tk.Button(root, text="Add Customer", command=self.add_customer)
        self.add_customer_button.pack()

        self.interaction_label = tk.Label(root, text="Interaction:")
        self.interaction_label.pack()
        self.interaction_entry = tk.Entry(root)
        self.interaction_entry.pack()

        self.record_interaction_button = tk.Button(root, text="Record Interaction", command=self.record_interaction)
        self.record_interaction_button.pack()

        self.purchase_label = tk.Label(root, text="Purchase Amount:")
        self.purchase_label.pack()
        self.purchase_entry = tk.Entry(root)
        self.purchase_entry.pack()

        self.record_purchase_button = tk.Button(root, text="Record Purchase", command=self.record_purchase)
        self.record_purchase_button.pack()

        self.view_details_button = tk.Button(root, text="View Customer Details", command=self.view_customer_details)
        self.view_details_button.pack()

        # Display for Results
        self.result_text = tk.Text(root, height=10, width=50)
        self.result_text.pack()

    def add_customer(self):
        customer_id = self.customer_id_entry.get()
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        if customer_id and name and email and phone:
            message = self.crm.add_customer(int(customer_id), name, email, phone)
            messagebox.showinfo("Info", message)
        else:
            messagebox.showwarning("Warning", "Please fill all fields.")

    def record_interaction(self):
        customer_id = self.customer_id_entry.get()
        interaction = self.interaction_entry.get()
        if customer_id and interaction:
            message = self.crm.record_interaction(int(customer_id), interaction)
            messagebox.showinfo("Info", message)
        else:
            messagebox.showwarning("Warning", "Please enter customer ID and interaction.")

    def record_purchase(self):
        customer_id = self.customer_id_entry.get()
        amount = self.purchase_entry.get()
        if customer_id and amount:
            try:
                amount = float(amount)
                message = self.crm.record_purchase(int(customer_id), amount)
                messagebox.showinfo("Info", message)
            except ValueError:
                messagebox.showerror("Error", "Invalid amount entered.")
        else:
            messagebox.showwarning("Warning", "Please enter customer ID and purchase amount.")

    def view_customer_details(self):
        customer_id = self.customer_id_entry.get()
        if customer_id:
            details = self.crm.get_customer_details(int(customer_id))
            if isinstance(details, dict):
                details_text = "\n".join(f"{key}: {value}" for key, value in details.items())
            else:
                details_text = details
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, details_text)
        else:
            messagebox.showwarning("Warning", "Please enter a customer ID.")


# Run the CRM App
root = tk.Tk()
app = CRMApp(root)
root.mainloop()
