import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

def open_airport_gui():
    def GetValue(event):
        clear_entries()
        row_id = listBox.selection()[0]
        select = listBox.item(row_id)['values']
        for i in range(len(select)):
            entry_fields[i].insert(0, select[i])

    def Add():
        values = [entry.get() for entry in entry_fields]
        try:
            sql = "INSERT INTO airport (airport_id, airport_name, flight_name, flight_id) VALUES (%s, %s, %s, %s)"
            mycursor.execute(sql, values)
            mydb.commit()
            messagebox.showinfo("Information", "Airport added successfully")
            show()
        except Exception as e:
            messagebox.showerror("Error", f"Error adding airport: {e}")

    def update():
        values = [entry.get() for entry in entry_fields]
        airport_id = values[0]
        try:
            sql = "UPDATE airport SET airport_name = %s, flight_name = %s, flight_id = %s WHERE airport_id = %s"
            mycursor.execute(sql, values[1:] + [airport_id])
            mydb.commit()
            messagebox.showinfo("Information", "Airport updated successfully")
            show()
        except Exception as e:
            messagebox.showerror("Error", f"Error updating airport: {e}")

    def delete():
        airport_id = entry_fields[0].get()
        try:
            sql = "DELETE FROM airport WHERE airport_id = %s"
            mycursor.execute(sql, (airport_id,))
            mydb.commit()
            messagebox.showinfo("Information", "Airport deleted successfully")
            show()
        except Exception as e:
            messagebox.showerror("Error", f"Error deleting airport: {e}")

    def show():
        for record in listBox.get_children():
            listBox.delete(record)
        try:
            mycursor.execute("SELECT * FROM airport")
            records = mycursor.fetchall()
            for record in records:
                listBox.insert("", "end", values=record)
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching data: {e}")

    def clear_entries():
        for entry in entry_fields:
            entry.delete(0, tk.END)

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sidmus#25",
        database="ams"
    )
    mycursor = mydb.cursor()

    airport_window = tk.Tk()
    airport_window.geometry("1000x500")
    airport_window.title("Airport Management")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground="#D3D3D3")
    style.map("Treeview", background=[("selected", "#347083")])

    labels = ['Airport ID', 'Airport Name', 'Flight Name', 'Flight ID']
    entry_fields = [tk.Entry(airport_window) for _ in range(len(labels))]

    for i, label in enumerate(labels):
        tk.Label(airport_window, text=label, font=("Helvetica", 10, "bold")).grid(row=i, column=0, padx=5, pady=5, sticky="e")
        entry_fields[i].grid(row=i, column=1, padx=5, pady=5, sticky="ew")

    btn_add = tk.Button(airport_window, text="Add", command=Add, font=("Helvetica", 10, "bold"), bg="#4CAF50", fg="white")
    btn_add.grid(row=8, column=0, padx=5, pady=5, sticky="ew")

    btn_update = tk.Button(airport_window, text="Update", command=update, font=("Helvetica", 10, "bold"), bg="#FFD700", fg="black")
    btn_update.grid(row=8, column=1, padx=5, pady=5, sticky="ew")

    btn_delete = tk.Button(airport_window, text="Delete", command=delete, font=("Helvetica", 10, "bold"), bg="#FF6347", fg="white")
    btn_delete.grid(row=8, column=2, padx=5, pady=5, sticky="ew")

    cols = ['Airport ID', 'Airport Name', 'Flight Name', 'Flight ID']
    listBox = ttk.Treeview(airport_window, columns=cols, show='headings')
    for col in cols:
        listBox.heading(col, text=col)
        listBox.grid(row=9, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

    show()
    listBox.bind('<Double-Button-1>', GetValue)

    for i in range(9):
        airport_window.grid_rowconfigure(i, weight=1)
        airport_window.grid_columnconfigure(i, weight=1)

    airport_window.mainloop()

def open_baggage_gui():
    def GetValue(event):
        clear_entries()
        row_id = listBox.selection()[0]
        select = listBox.item(row_id)['values']
        for i in range(len(select)):
            entry_fields[i].insert(0, select[i])

    def Add():
        values = [entry.get() for entry in entry_fields]
        try:
            sql = "INSERT INTO baggage (baggage_id, cost_amount, baggage_type, customer_name, customer_id) VALUES (%s, %s, %s, %s, %s)"
            mycursor.execute(sql, values)
            mydb.commit()
            messagebox.showinfo("Information", "Baggage added successfully")
            show()
        except Exception as e:
            messagebox.showerror("Error", f"Error adding baggage: {e}")

    def update():
        values = [entry.get() for entry in entry_fields]
        baggage_id = values[0]
        try:
            sql = "UPDATE baggage SET cost_amount = %s, baggage_type = %s, customer_name = %s, customer_id = %s WHERE baggage_id = %s"
            mycursor.execute(sql, values[1:] + [baggage_id])
            mydb.commit()
            messagebox.showinfo("Information", "Baggage updated successfully")
            show()
        except Exception as e:
            messagebox.showerror("Error", f"Error updating baggage: {e}")

    def delete():
        baggage_id = entry_fields[0].get()
        try:
            sql = "DELETE FROM baggage WHERE baggage_id = %s"
            mycursor.execute(sql, (baggage_id,))
            mydb.commit()
            messagebox.showinfo("Information", "Baggage deleted successfully")
            show()
        except Exception as e:
            messagebox.showerror("Error", f"Error deleting baggage: {e}")

    def show():
        for record in listBox.get_children():
            listBox.delete(record)
        try:
            mycursor.execute("SELECT * FROM baggage")
            records = mycursor.fetchall()
            for record in records:
                listBox.insert("", "end", values=record)
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching data: {e}")

    def clear_entries():
        for entry in entry_fields:
            entry.delete(0, tk.END)

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sidmus#25",
        database="ams"
    )
    mycursor = mydb.cursor()

    baggage_window = tk.Tk()
    baggage_window.geometry("1000x500")
    baggage_window.title("Baggage Management")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground="#D3D3D3")
    style.map("Treeview", background=[("selected", "#347083")])

    labels = ['Baggage ID', 'Cost Amount', 'Baggage Type', 'Customer Name', 'Customer ID']
    entry_fields = [tk.Entry(baggage_window) for _ in range(len(labels))]

    for i, label in enumerate(labels):
        tk.Label(baggage_window, text=label, font=("Helvetica", 10, "bold")).grid(row=i, column=0, padx=5, pady=5, sticky="e")
        entry_fields[i].grid(row=i, column=1, padx=5, pady=5, sticky="ew")

    btn_add = tk.Button(baggage_window, text="Add", command=Add, font=("Helvetica", 10, "bold"), bg="#4CAF50", fg="white")
    btn_add.grid(row=8, column=0, padx=5, pady=5, sticky="ew")

    btn_update = tk.Button(baggage_window, text="Update", command=update, font=("Helvetica", 10, "bold"), bg="#FFD700", fg="black")
    btn_update.grid(row=8, column=1, padx=5, pady=5, sticky="ew")

    btn_delete = tk.Button(baggage_window, text="Delete", command=delete, font=("Helvetica", 10, "bold"), bg="#FF6347", fg="white")
    btn_delete.grid(row=8, column=2, padx=5, pady=5, sticky="ew")

    cols = ['Baggage ID', 'Cost Amount', 'Baggage Type', 'Customer Name', 'Customer ID']
    listBox = ttk.Treeview(baggage_window, columns=cols, show='headings')
    for col in cols:
        listBox.heading(col, text=col)
        listBox.grid(row=9, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

    show()
    listBox.bind('<Double-Button-1>', GetValue)

    for i in range(9):
        baggage_window.grid_rowconfigure(i, weight=1)
        baggage_window.grid_columnconfigure(i, weight=1)

    baggage_window.mainloop()

def open_customer_gui():
    def GetValue(event):
        clear_entries()
        row_id = listBox.selection()[0]
        select = listBox.item(row_id)['values']
        for i in range(len(select)):
            entry_fields[i].insert(0, select[i])

    def Add():
        values = [entry.get() for entry in entry_fields]
        try:
            sql = "INSERT INTO customer (customer_id, ticket_id, customer_name, passenger_type, passenger_id, booking_date) VALUES (%s, %s, %s, %s, %s, %s)"
            mycursor.execute(sql, values)
            mydb.commit()
            messagebox.showinfo("Information", "Customer added successfully")
            show()
        except Exception as e:
            messagebox.showerror("Error", f"Error adding customer: {e}")

    def update():
        values = [entry.get() for entry in entry_fields]
        customer_id = values[0]
        try:
            sql = "UPDATE customer SET ticket_id = %s, customer_name = %s, passenger_type = %s, passenger_id = %s, booking_date = %s WHERE customer_id = %s"
            mycursor.execute(sql, values[1:] + [customer_id])
            mydb.commit()
            messagebox.showinfo("Information", "Customer updated successfully")
            show()
        except Exception as e:
            messagebox.showerror("Error", f"Error updating customer: {e}")

    def delete():
        customer_id = entry_fields[0].get()
        try:
            sql = "DELETE FROM customer WHERE customer_id = %s"
            mycursor.execute(sql, (customer_id,))
            mydb.commit()
            messagebox.showinfo("Information", "Customer deleted successfully")
            show()
        except Exception as e:
            messagebox.showerror("Error", f"Error deleting customer: {e}")

    def show():
        for record in listBox.get_children():
            listBox.delete(record)
        try:
            mycursor.execute("SELECT * FROM customer")
            records = mycursor.fetchall()
            for record in records:
                listBox.insert("", "end", values=record)
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching data: {e}")

    def clear_entries():
        for entry in entry_fields:
            entry.delete(0, tk.END)

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sidmus#25",
        database="ams"
    )
    mycursor = mydb.cursor()

    customer_window = tk.Tk()
    customer_window.geometry("1000x500")
    customer_window.title("Customer Management")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground="#D3D3D3")
    style.map("Treeview", background=[("selected", "#347083")])

    labels = ['Customer ID', 'Ticket ID', 'Customer Name', 'Passenger Type', 'Passenger ID', 'Booking Date']
    entry_fields = [tk.Entry(customer_window) for _ in range(len(labels))]

    for i, label in enumerate(labels):
        tk.Label(customer_window, text=label, font=("Helvetica", 10, "bold")).grid(row=i, column=0, padx=5, pady=5, sticky="e")
        entry_fields[i].grid(row=i, column=1, padx=5, pady=5, sticky="ew")

    btn_add = tk.Button(customer_window, text="Add", command=Add, font=("Helvetica", 10, "bold"), bg="#4CAF50", fg="white")
    btn_add.grid(row=8, column=0, padx=5, pady=5, sticky="ew")

    btn_update = tk.Button(customer_window, text="Update", command=update, font=("Helvetica", 10, "bold"), bg="#FFD700", fg="black")
    btn_update.grid(row=8, column=1, padx=5, pady=5, sticky="ew")

    btn_delete = tk.Button(customer_window, text="Delete", command=delete, font=("Helvetica", 10, "bold"), bg="#FF6347", fg="white")
    btn_delete.grid(row=8, column=2, padx=5, pady=5, sticky="ew")

    cols = ['Customer ID', 'Ticket ID', 'Customer Name', 'Passenger Type', 'Passenger ID', 'Booking Date']
    listBox = ttk.Treeview(customer_window, columns=cols, show='headings')
    for col in cols:
        listBox.heading(col, text=col)
        listBox.grid(row=9, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

    show()
    listBox.bind('<Double-Button-1>', GetValue)

    for i in range(9):
        customer_window.grid_rowconfigure(i, weight=1)
        customer_window.grid_columnconfigure(i, weight=1)

    customer_window.mainloop()

def open_benefits_gui():
    def GetValue(event):
        clear_entries()
        row_id = listBox.selection()[0]
        select = listBox.item(row_id)['values']
        for i in range(len(select)):
            entry_fields[i].insert(0, select[i])

    def Add():
        values = [entry.get() for entry in entry_fields]
        try:
            sql = "INSERT INTO benefits (benefit_type, benefit_id, customer_id, miles) VALUES (%s, %s, %s, %s)"
            mycursor.execute(sql, values)
            mydb.commit()
            messagebox.showinfo("Information", "Benefit added successfully")
            show()
        except Exception as e:
            messagebox.showerror("Error", f"Error adding benefit: {e}")

    def update():
        values = [entry.get() for entry in entry_fields]
        benefit_id = values[1]
        try:
            sql = "UPDATE benefits SET benefit_type = %s, customer_id = %s, miles = %s WHERE benefit_id = %s"
            mycursor.execute(sql, values[:1] + values[2:] + [benefit_id])
            mydb.commit()
            messagebox.showinfo("Information", "Benefit updated successfully")
            show()
        except Exception as e:
            messagebox.showerror("Error", f"Error updating benefit: {e}")

    def delete():
        benefit_id = entry_fields[1].get()
        try:
            sql = "DELETE FROM benefits WHERE benefit_id = %s"
            mycursor.execute(sql, (benefit_id,))
            mydb.commit()
            messagebox.showinfo("Information", "Benefit deleted successfully")
            show()
        except Exception as e:
            messagebox.showerror("Error", f"Error deleting benefit: {e}")

    def show():
        for record in listBox.get_children():
            listBox.delete(record)
        try:
            mycursor.execute("SELECT * FROM benefits")
            records = mycursor.fetchall()
            for record in records:
                listBox.insert("", "end", values=record)
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching data: {e}")

    def clear_entries():
        for entry in entry_fields:
            entry.delete(0, tk.END)

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sidmus#25",
        database="ams"
    )
    mycursor = mydb.cursor()

    benefits_window = tk.Tk()
    benefits_window.geometry("1000x500")
    benefits_window.title("Benefit Management")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground="#D3D3D3")
    style.map("Treeview", background=[("selected", "#347083")])

    labels = ['Benefit Type', 'Benefit ID', 'Customer ID', 'Miles']
    entry_fields = [tk.Entry(benefits_window) for _ in range(len(labels))]

    for i, label in enumerate(labels):
        tk.Label(benefits_window, text=label, font=("Helvetica", 10, "bold")).grid(row=i, column=0, padx=5, pady=5, sticky="e")
        entry_fields[i].grid(row=i, column=1, padx=5, pady=5, sticky="ew")

    btn_add = tk.Button(benefits_window, text="Add", command=Add, font=("Helvetica", 10, "bold"), bg="#4CAF50", fg="white")
    btn_add.grid(row=4, column=0, padx=5, pady=5, sticky="ew")

    btn_update = tk.Button(benefits_window, text="Update", command=update, font=("Helvetica", 10, "bold"), bg="#FFD700", fg="black")
    btn_update.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

    btn_delete = tk.Button(benefits_window, text="Delete", command=delete, font=("Helvetica", 10, "bold"), bg="#FF6347", fg="white")
    btn_delete.grid(row=4, column=2, padx=5, pady=5, sticky="ew")

    cols = ['Benefit Type', 'Benefit ID', 'Customer ID', 'Miles']
    listBox = ttk.Treeview(benefits_window, columns=cols, show='headings')
    for col in cols:
        listBox.heading(col, text=col)
        listBox.grid(row=5, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

    show()
    listBox.bind('<Double-Button-1>', GetValue)

    for i in range(5):
        benefits_window.grid_rowconfigure(i, weight=1)
        benefits_window.grid_columnconfigure(i, weight=1)

    benefits_window.mainloop()


def main_gui():
    root = tk.Tk()
    root.geometry("400x200")
    root.title("Menu- Airline Management System")

    btn_user = tk.Button(root, text="Airport", command=open_airport_gui)
    btn_user.pack(pady=10)

    btn_borrower = tk.Button(root, text="Baggage", command=open_baggage_gui)
    btn_borrower.pack(pady=10)

    btn_loan = tk.Button(root, text="Customer", command=open_customer_gui)
    btn_loan.pack(pady=10)

    btn_user = tk.Button(root, text="Benefits", command=open_benefits_gui)
    btn_user.pack(pady=10)
    
    root.mainloop()

main_gui()
