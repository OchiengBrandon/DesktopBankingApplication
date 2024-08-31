import customtkinter as ctk
import datetime as dt
import time as tm
from tkinter import *
from middleware import account_creation_logic, login_logic
from middleware import transaction_logic, transaction_history_logic
from middleware import get_balance, get_username, deposit_update, deduction_update, deduction_validation
from middleware import transaction_routing, received_statement, pin_validation
from tkinter import messagebox
import webbrowser
import values
import utility

class main(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("BarselCorp")
        self._set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        self.geometry(f"{values.WIDTH}x{values.HEIGHT}")
        # background_image = PhotoImage(file=r"Assets/background.png")
        # background_image_label = ctk.CTkLabel(self, image=background_image)
        #background_image_label.place(relheight=1, relwidth=1)
        
        ctk.CTkLabel(self, text="WELCOME TO BarselCorp M-BANKING", font=ctk.CTkFont(size=24, weight="bold"), text_color="Red").pack(pady=12)
        
        self.login()
    
    # Switching to Account Creation
    def switch_create_account(self):
        self.login_frame.destroy()
        self.create_account() 
    
    # Switching to Login
    def switch_login(self):
        self.create_account_frame.destroy()
        self.login()
        
    # BACK END configuration for Account Creation
    def account_creation_submit(self):
        try:
            # Back End Logic
            account_creation_logic(self.first_name_entry.get(), self.surname_entry.get(), self.last_name_entry.get(), self.id_number_entry.get(), self.DOB_entry.get(), self.email_entry.get(),self.location_entry.get(),
                            self.number_entry.get(), self.pin_creation_entry.get(),self.confirm_password_entry.get())
            
            # Open LOGIN Window
            self.switch_login()
        except: 
            messagebox.showerror("Error", "Account Creation failed!!")

    # BACK END configuration for login
    def login_check(self): 
        # Database codes  
        if login_logic(self.user_name_entry.get(), self.password_entry.get()) == 1:
            self.withdraw()
            messagebox.showinfo("Login", "Login Successfull")
            self.user_dashboard()
        else:
            messagebox.showerror("Login Error", "Inavlid User or Password")
            


    # Login Frame  
    def login(self):
        self.login_frame = ctk.CTkFrame(self)
        self.login_frame.pack(padx=10, fill="both", expand=True)
        ctk.CTkLabel(self.login_frame, text="LOGIN").pack(padx=5)
        # login frame 
        login_frame = ctk.CTkFrame(self.login_frame)
        login_frame.pack()
        user_name_label = ctk.CTkLabel(login_frame, text="Username").grid(row=0, column=0, padx=2, pady=3)
        self.user_name_entry = ctk.CTkEntry(login_frame, placeholder_text="Id Number")
        self.user_name_entry.grid(row=0, column=1, padx=10,pady=5)
        password_label= ctk.CTkLabel(login_frame, text="Password").grid(row=1, column=0)
        self.password_entry = ctk.CTkEntry(login_frame, placeholder_text="Password")
        self.password_entry.grid(row=1, column=1)
        
        
        sign_in = ctk.CTkButton(self.login_frame, text="Sign In", width=70, command=self.login_check)
        sign_in.pack(pady=10, padx=40)
     
        
        # info frame
        info_frame =ctk.CTkFrame(self.login_frame)
        info_frame.pack()
        ctk.CTkLabel(info_frame, text="Don't have an account?").grid(row=0, column=0)
        create_redirect_button = ctk.CTkButton(info_frame, text="Create account", width=70, height=20, command=self.switch_create_account)
        create_redirect_button.grid(row=0, column=1, padx=4)

    def create_account(self):
        self.create_account_frame = ctk.CTkFrame(self)
        self.create_account_frame.pack(padx=10)
        ctk.CTkLabel(self.create_account_frame, text="Create Account").pack(padx=5)
        # Account Creation frame 
        accounts_frame = ctk.CTkFrame(self.create_account_frame)
        accounts_frame.pack()
        
        
        # Widgets
        first_name_label = ctk.CTkLabel(accounts_frame, text="First_name").grid(row=0, column=0, padx=2, pady=3)
        self.first_name_entry = ctk.CTkEntry(accounts_frame, placeholder_text="First Name", width=values.entry_width)
        self.first_name_entry.grid(row=0, column=1, padx=8)
        
        surname_label = ctk.CTkLabel(accounts_frame, text="Surname").grid(row=0, column=2, padx=2, pady=3)
        self.surname_entry = ctk.CTkEntry(accounts_frame, placeholder_text="Surname",width=values.entry_width)
        self.surname_entry.grid(row=0, column=3, padx=5)
        
        
        last_name_label = ctk.CTkLabel(accounts_frame, text="Last Name").grid(row=1, column=0, padx=2, pady=3)
        self.last_name_entry = ctk.CTkEntry(accounts_frame, placeholder_text="Last name", width=values.entry_width)
        self.last_name_entry.grid(row=1, column=1)
        
        
        id_number_label = ctk.CTkLabel(accounts_frame, text="ID Number").grid(row=2, column=0, padx=2, pady=3)
        self.id_number_entry = ctk.CTkEntry(accounts_frame, placeholder_text="ID Number", width=values.entry_width)
        self.id_number_entry.grid(row=2, column=1)
        
        DOB_label = ctk.CTkLabel(accounts_frame, text="Year Of Birth").grid(row=3, column=0, padx=2, pady=3)
        self.DOB_entry = ctk.CTkEntry(accounts_frame, placeholder_text="YOB", width=values.entry_width)
        self.DOB_entry.grid(row=3, column=1)
        
        email_label = ctk.CTkLabel(accounts_frame, text="Email").grid(row=4, column=0, padx=2, pady=3)
        self.email_entry = ctk.CTkEntry(accounts_frame, placeholder_text="Email", width=values.entry_width)
        self.email_entry.grid(row=4, column=1)
        
        location_label = ctk.CTkLabel(accounts_frame, text="Location").grid(row=5, column=0, padx=2, pady=3)
        self.location_entry = ctk.CTkEntry(accounts_frame, placeholder_text="Location", width=values.entry_width)
        self.location_entry.grid(row=5, column=1)
        
        number_label = ctk.CTkLabel(accounts_frame, text="Tel Number").grid(row=6, column=0, padx=2, pady=3)
        self.number_entry = ctk.CTkEntry(accounts_frame, placeholder_text="Tel Number", width=values.entry_width)
        self.number_entry.grid(row=6, column=1)
        
        pin_label = ctk.CTkLabel(accounts_frame, text="PIN").grid(row=7, column=0, padx=2, pady=3)
        self.pin_creation_entry = ctk.CTkEntry(accounts_frame, placeholder_text="PIN", width=values.entry_width)
        self.pin_creation_entry.grid(row=7, column=1)
        
        password_label = ctk.CTkLabel(accounts_frame, text="Password").grid(row=8, column=0, padx=2, pady=3)
        self.password_entry = ctk.CTkEntry(accounts_frame, placeholder_text="Password", width=values.entry_width)
        self.password_entry.grid(row=8, column=1)
        
        confirm_password_label = ctk.CTkLabel(accounts_frame, text="Confirm Password").grid(row=9, column=0, padx=2, pady=3)
        self.confirm_password_entry = ctk.CTkEntry(accounts_frame, placeholder_text="Confirm Password", width=values.entry_width)
        self.confirm_password_entry.grid(row=9, column=1)
        
        
        # Create Account Button
        create_account_button = ctk.CTkButton(self.create_account_frame, text="Create Account", width=70, command=self.account_creation_submit)
        create_account_button.pack(pady=10, padx=40)
        # info frame
        info_frame =ctk.CTkFrame(self.create_account_frame)
        info_frame.pack()
        ctk.CTkLabel(info_frame, text="You have an account?").grid(row=0, column=0)
        create_redirect_button = ctk.CTkButton(info_frame, text="Login", width=70, height=20, command=self.switch_login)
        create_redirect_button.grid(row=0, column=1, padx=4)
    
    # Show Button Clicked
    def show_Button_clicked(self):
        self.show_button.destroy()
        self.balance_widget()
        self.hide_button_button =ctk.CTkButton(self.balance_top, text="-", width=20, height=10, border_color="green", border_width=1, font=ctk.CTkFont(weight="bold"), command=self.hideButton_clicked)
        self.hide_button_button.place(x=373, y=4)
    # Hide button in user dashboard
    def hideButton_clicked(self):
        self.balance_bottom.destroy()
        # Overidding the Hide button
        self.hide_button.destroy()
        self.show_button =ctk.CTkButton(self.balance_top, text="+", width=20, height=10, border_color="green", border_width=1, font=ctk.CTkFont(weight="bold"), command=self.show_Button_clicked)
        self.show_button.place(x=373, y=4)
    
    # Send Money
    def send_money(self):
        
        # Validating 
        if deduction_validation(self.user_name_entry.get(),self.send_amount_entry.get()) == 1:
            # Database check
            deduction_update(self.user_name_entry.get(),self.send_amount_entry.get())
            #>>>>>
            transaction_type = "Send Money"
            # middleware
            transaction_logic(self.my_account_number, transaction_type, self.send_amount_entry.get(),self.send_account_number_entry.get() )
            messagebox.showinfo("Approved", f"Send Money to {self.send_account_number_entry.get()} successfull")
            
            # Route the transaction if user exists
            transaction_routing(self.send_account_number_entry.get(),self.send_amount_entry.get())
            received_statement(self.send_account_number_entry.get(),self.send_amount_entry.get(), self.user_name_entry.get())
            
        else:
            messagebox.showerror("Error", message=f"Insufficient Balance, current balance is {get_balance(self.user_name_entry.get())} Deposit Funds")
    # Paybill
    def paybill(self):
        # Validation
        if deduction_validation(self.user_name_entry.get(),self.paybill_amount_entry.get()) == 1:
            deduction_update(self.user_name_entry.get(),self.paybill_amount_entry.get())
            transaction_type = "Paybill"
            # middleware
            transaction_logic(self.my_account_number, transaction_type, self.paybill_amount_entry.get(),self.paybiil_no_entry.get() )
            messagebox.showinfo("Approved", f"Paybill to {self.paybiil_no_entry.get()} successfull")
        else:
            messagebox.showerror("Error", message=f"Insufficient Balance, current balance is {get_balance(self.user_name_entry.get())} Deposit Funds")
            
    # Buy Goods
    def buy_goods(self):
        # Validation
        if deduction_validation(self.user_name_entry.get(), self.buy_goods_amount_entry.get())== 1:
            deduction_update(self.user_name_entry.get(), self.buy_goods_amount_entry.get())
            transaction_type = "Buy Goods"
            # middleware
            transaction_logic(self.my_account_number, transaction_type, self.buy_goods_amount_entry.get(),self.buy_goods_no_entry.get() )
            messagebox.showinfo("Approved", f"Buy Goods to {self.buy_goods_no_entry.get()} successfull")
        else:
            messagebox.showerror("Error", message=f"Insufficient Balance, current balance is {get_balance(self.user_name_entry.get())} Deposit Funds")
    
    # Show Transaction History
    def show_history(self):
        # removing history button
        # create widgets
        self.show_history_button.destroy()
        # Creating a hide
        self.show_history_button = ctk.CTkButton(self.history_upper_frame, text="Hide", command=self.hide_history)
        self.show_history_button.pack()
        
        transaction_history_logic(self.my_account_number, self.recepient_header, 
                                  self.transaction_date, self.transaction_history_ammount, self.transaction_history_type)
        

    def hide_history(self):
        self.history_upper_frame.destroy()
        self.history_frame.destroy()
        
        # Adding the widgets
        self.history_widgets()
        #  Destroying the current show button
        self.show_history_button.destroy()
        
        # Creating show button
        self.show_history_button = ctk.CTkButton(self.history_upper_frame, text="Show", command=self.show_history)
        self.show_history_button.pack()
    
    # Creating show widgets
    def history_widgets(self):
        # History Tab
        self.history_upper_frame = ctk.CTkFrame(self.tab_view.tab("History"))
        self.history_upper_frame.pack(pady=0)
        self.show_history_button = ctk.CTkButton(self.history_upper_frame, text="Show", command=self.show_history)
        self.show_history_button.pack()

        self.history_frame = ctk.CTkFrame(self.tab_view.tab("History"), height=320)
        self.history_frame.pack(expand=True, fill="both")
        

        
        
        # Recepient account
        self.recepient_header = ctk.CTkFrame(self.history_frame)
        self.recepient_header.place(relx=0.1, rely=0.3)
        ctk.CTkLabel(self.recepient_header, text="ACCOUNT", font=ctk.CTkFont(weight="bold", underline=True), text_color="brown").pack()
        
        
        self.transaction_date = ctk.CTkFrame(self.history_frame)
        self.transaction_date.place(relx=0.3, rely=0.3)
        ctk.CTkLabel(self.transaction_date, text="DATE", font=ctk.CTkFont(weight="bold",  underline=True), text_color="brown").pack()
        
        self.transaction_history_type = ctk.CTkFrame(self.history_frame)
        self.transaction_history_type.place(relx=0.6, rely=0.3)
        ctk.CTkLabel(self.transaction_history_type,text="DESCRIPTION", font=ctk.CTkFont(weight="bold", underline=True), text_color="brown").pack()  
        
        
        self.transaction_history_ammount = ctk.CTkFrame(self.history_frame)
        self.transaction_history_ammount.place(relx=0.8, rely=0.3)
        ctk.CTkLabel(self.transaction_history_ammount,text="AMOUNT", font=ctk.CTkFont(weight="bold", underline=True), text_color="brown").pack() 
    # Aitime
    def buy_Airtime(self):
        # Validation
        if deduction_validation(self.user_name_entry.get(), self.Aamount_entry.get())== 1:
            deduction_update(self.user_name_entry.get(), self.Aamount_entry.get())
            transaction_type = "Buy Airtime"
            # middleware
            transaction_logic(self.my_account_number, transaction_type, self.Aamount_entry.get(),self.Aphone_number_entry.get() )
            messagebox.showinfo("Approved", f"Airtime purchase for  {self.Aphone_number_entry.get()} successfull")
            
        else:
            messagebox.showerror("Error", message=f"Insufficient Balance, current balance is {get_balance(self.user_name_entry.get())} Deposit Funds")
    # deposit
    def deposit(self):
        transaction_type = "Deposit"
        
        # Database update balance
        deposit_update(self.user_name_entry.get(),self.Damount_entry.get())
        print("Deposit Saved")

        # middleware
        transaction_logic(self.my_account_number, transaction_type, self.Damount_entry.get(),self.deposit_account_entry.get() )
        messagebox.showinfo("Approved", f"Deposit to {self.deposit_account_entry.get()} successfull")
     
    # User Dashboard   
    def user_dashboard(self):
        ctk.set_default_color_theme("green")
        self.dashboard_window = ctk.CTkToplevel(self) 
        self.dashboard_window.title("BarselCorp")
        self.dashboard_window.geometry(f"{utility.width_addition(120)}x{utility.height_addition(180)}")
        self.dashboard_window.resizable(True, True)
        
        
        # Date parameters
        self.date = dt.datetime.now()
        self.time = tm.strftime('%H:%M:%S')
        # Top frame
        top_frame =ctk.CTkFrame(self.dashboard_window, height=40, border_width=2, border_color="blue")
        top_frame.pack(fill=X, padx=5, pady=5)
        
        top1 = ctk.CTkFrame(top_frame, border_width=2, border_color="green")
        top1.place(relx=0,x=4, y=4)
        # f"Hi {get_username(self.user_name_entry.get())} !"
        ctk.CTkLabel(top1, text=f"Hi {get_username(self.user_name_entry.get())}", font=ctk.CTkFont(family="Elephant",size=16, weight="bold")).pack()
        
        top_c = ctk.CTkFrame(top_frame)
        top_c.place(relx=0.5, y=4)
        ctk.CTkLabel(top_c, text=self.time, font=ctk.CTkFont(size=16, weight="bold")).pack()
        
        top2 = ctk.CTkFrame(top_frame)
        top2.place(relx=0.78, y=4)
        ctk.CTkLabel(top2, text=f"{self.date:%B, %d %Y}", font=ctk.CTkFont(size=16, weight="bold")).pack()
        
        sizes = 400
        # Balance frame
        self.balance_frame = ctk.CTkFrame(self.dashboard_window, width=450, corner_radius=10)
        self.balance_frame.pack(pady=10)
        
        # Top
        self.balance_top = ctk.CTkFrame(self.balance_frame, corner_radius=10, border_color="orange", width=sizes, height=40, border_width=2)
        self.balance_top.pack(fill=X, pady=10, padx=4)
        ctk.CTkLabel(self.balance_top, text=self.user_name_entry.get(), width=30, font=ctk.CTkFont(size=14, family="Arial", weight="bold")).place(x=7, y=2)
        
        
        # Hide and unhide buttons
        self.hide_button =ctk.CTkButton(self.balance_top, text="-", width=20, height=10, border_color="green", border_width=1, font=ctk.CTkFont(weight="bold"), command=self.hideButton_clicked)
        self.hide_button.place(x=373, y=4)
        self.balance_widget()
        
          
        # Tab View
        self.tab_view = ctk.CTkTabview(self.dashboard_window, width=500)
        self.tab_view.pack()
        
        # Tabs
        self.tab_view.add("History")
        self.tab_view.add("Send")
        self.tab_view.add("Pay")
        self.tab_view.add("Buy Airtime")
        self.tab_view.add("Deposit")
        
        
        # THE ACCOUNT NUMBER
        self.my_account_number= self.user_name_entry.get()
        
        # History   
        self.history_widgets()
    
       

        # Send Tab
        send_frame = ctk.CTkFrame(self.tab_view.tab("Send"))
        send_frame.pack(pady=16)
        # Widgets
        
        ctk.CTkLabel(send_frame, text="Enter Recepient Account").grid(row=0, column=0)
        self.send_account_number_entry  =ctk.CTkEntry(send_frame, placeholder_text="Account Number")
        self.send_account_number_entry.grid(row=0, column=1)
        
        ctk.CTkLabel(send_frame,text="Amount").grid(row=1, column=0)
        self.send_amount_entry = ctk.CTkEntry(send_frame, placeholder_text="Enter amount")
        self.send_amount_entry.grid(row=1, column=1, pady=10, padx=5)
        ctk.CTkLabel(send_frame, text="PIN").grid(row=2, column=0)
        pin_entry = ctk.CTkEntry(send_frame, placeholder_text="PIN")
        pin_entry.grid(row=2, column=1)
        
        # pin check
        def send_money_pin_check():
            if int(pin_validation(self.user_name_entry.get())) == int(pin_entry.get()):  
                self.send_money()
            else:
                messagebox.showinfo("Error", "Wrong Pin, Try Again")
        
        # Function
        send_button = ctk.CTkButton(send_frame, text="Send", width=50, command=send_money_pin_check)
        send_button.grid(row=3, column=1, pady=10)
        
        # Pay Tab
        pay_tab_view = ctk.CTkTabview(self.tab_view.tab("Pay"))
        pay_tab_view.pack()
        pay_tab_view.add("Paybill")
        pay_tab_view.add("Buy Goods")
        
        # Paybill
        paybill_frame = ctk.CTkFrame(pay_tab_view.tab("Paybill"))
        paybill_frame.pack()
        ctk.CTkLabel(paybill_frame, text="Enter Paybill Number").grid(row=0, column=0)
        self.paybiil_no_entry = ctk.CTkEntry(paybill_frame, placeholder_text="Paybill")
        self.paybiil_no_entry.grid(row=0, column=1, pady=10, padx=5)
        
        ctk.CTkLabel(paybill_frame, text="Enter Amount").grid(row=1, column=0)
        self.paybill_amount_entry = ctk.CTkEntry(paybill_frame, placeholder_text="Amount")
        self.paybill_amount_entry.grid(row=1, column=1)
        
        ctk.CTkLabel(paybill_frame, text="PIN").grid(row=2, column=0, pady=10, padx=5)
        paybill_pin_entry = ctk.CTkEntry(paybill_frame, placeholder_text="PIN")
        paybill_pin_entry.grid(row=2, column=1)
        
        # pin check
        def paybill_pin_check():
            if int(pin_validation(self.user_name_entry.get())) == int(paybill_pin_entry.get()):  
                self.paybill()
            else:
                messagebox.showinfo("Error", "Wrong Pin, Try Again")
        
        # Function
        paybill_button = ctk.CTkButton(paybill_frame, text="Pay", width=50, command=paybill_pin_check)
        paybill_button.grid(row=3, column=1, pady=10)
        
        
        # Buy Goods
        buy_goods_frame = ctk.CTkFrame(pay_tab_view.tab("Buy Goods"))
        buy_goods_frame.pack()
        ctk.CTkLabel(buy_goods_frame, text="Enter Till Number").grid(row=0, column=0)
        self.buy_goods_no_entry = ctk.CTkEntry(buy_goods_frame, placeholder_text="Till Number")
        self.buy_goods_no_entry.grid(row=0, column=1, pady=10, padx=5)
        
        ctk.CTkLabel(buy_goods_frame, text="Enter Amount").grid(row=1, column=0)
        self.buy_goods_amount_entry = ctk.CTkEntry(buy_goods_frame, placeholder_text="Amount")
        self.buy_goods_amount_entry.grid(row=1, column=1)
        
        ctk.CTkLabel(buy_goods_frame, text="PIN").grid(row=2, column=0, pady=10, padx=5)
        buy_goods_pin_entry = ctk.CTkEntry(buy_goods_frame, placeholder_text="PIN")
        buy_goods_pin_entry.grid(row=2, column=1)
        
        # pin check
        def buy_goods_pin_check():
            if int(pin_validation(self.user_name_entry.get())) == int(buy_goods_pin_entry.get()):  
                self.buy_goods()
            else:
                messagebox.showinfo("Error", "Wrong Pin, Try Again")
        
        # Function
        buy_goods_button = ctk.CTkButton(buy_goods_frame, text="Pay", width=50, command = buy_goods_pin_check)
        buy_goods_button.grid(row=3, column=1, pady=10)
    
        # Buy Airtime
        # Widgets
        buy_airtime_frame = ctk.CTkFrame(self.tab_view.tab("Buy Airtime"))
        buy_airtime_frame.pack(pady=10)
        ctk.CTkLabel(buy_airtime_frame, text="Enter Phone Number").grid(row=0, column=0)
        self.Aphone_number_entry= ctk.CTkEntry(buy_airtime_frame, placeholder_text="Phone Number")
        self.Aphone_number_entry.grid(row=0, column=1)
        
        ctk.CTkLabel(buy_airtime_frame,text="Amount" ).grid(row=1, column=0)
        self.Aamount_entry = ctk.CTkEntry(buy_airtime_frame, placeholder_text="Airtime Amount")
        self.Aamount_entry.grid(row=1, column=1, pady=10, padx=5)
        
        ctk.CTkLabel(buy_airtime_frame, text="PIN").grid(row=2, column=0, pady=10, padx=5)
        airtime_pin_entry = ctk.CTkEntry(buy_airtime_frame, placeholder_text="PIN")
        airtime_pin_entry.grid(row=2, column=1)
        
        # pin check
        def buy_airtime_pin_check():
            if int(pin_validation(self.user_name_entry.get())) == int(airtime_pin_entry.get()):  
                self.buy_Airtime()
            else:
                messagebox.showinfo("Error", "Wrong Pin, Try Again")
        
        # Function
        buy_airtime_button = ctk.CTkButton(buy_airtime_frame, text="Buy", width=50, command=buy_airtime_pin_check)
        buy_airtime_button.grid(row=3, column=1, pady=10)
        
        # Deposit
        deposit_frame = ctk.CTkFrame(self.tab_view.tab("Deposit"))
        deposit_frame.pack(pady=10)
        
        ctk.CTkLabel(deposit_frame, text="Account Number").grid(row=0, column=0)
        self.deposit_account_entry = ctk.CTkEntry(deposit_frame)
        self.deposit_account_entry.insert(0, self.user_name_entry.get())
        self.deposit_account_entry.grid(row=0, column=1)
        ctk.CTkLabel(deposit_frame,text="Amount" ).grid(row=1, column=0)
        self.Damount_entry = ctk.CTkEntry(deposit_frame, placeholder_text="Amount")
        self.Damount_entry.grid(row=1, column=1, pady=10, padx=5)
        min_amount_label = ctk.CTkLabel(deposit_frame, text="Minimun amount is Ksh.100", text_color="red")
        min_amount_label.grid(row=1, column=2)
        
        ctk.CTkLabel(deposit_frame, text="PIN").grid(row=2, column=0, pady=10, padx=5)
        deposit_pin_entry = ctk.CTkEntry(deposit_frame, placeholder_text="PIN")
        deposit_pin_entry.grid(row=2, column=1)
        
        # Deposit Amount and PIN Check (Minimum ksh 100)
        def deposit_pin_check():
            if int(self.Damount_entry.get()) > 100:
                
                if int(pin_validation(self.user_name_entry.get())) == int(deposit_pin_entry.get()):  
                    self.deposit()
                else:
                    messagebox.showinfo("Error", "Wrong Pin, Try Again")
            else:
                messagebox.showerror("Minimum Deposit", f"Sorry! Deposit amount of {self.Damount_entry.get()} is lower than ksh 100")
                
        
        # Function
        deposit_button = ctk.CTkButton(deposit_frame, text="Deposit", width=50, command=deposit_pin_check)
        deposit_button.grid(row=3, column=1, pady=10)
        
        
        
        # Lower Frame
        lower_frame = ctk.CTkFrame(self.dashboard_window)
        lower_frame.pack(pady=20, side=BOTTOM)
       
        about_button = ctk.CTkButton(lower_frame, text="About Us", command=self.web_view)
        about_button.grid(row=0, column=0)
        
        logout_button = ctk.CTkButton(lower_frame, text="Log Out",command=self.log_out)
        logout_button.grid(row=0, column=1, padx=10)

        # Change Theme Variables
        self.switch_var_1 = ctk.StringVar(value="on")
        self.switch_var_2 = ctk.StringVar(value="off")
        
        Change_theme = ctk.CTkSwitch(lower_frame, text="Change App Mode", variable=self.switch_var_1, command=self.switch_theme_event, onvalue="on", offvalue="off")
        Change_theme.grid(row=0, column=2)
        lock_theme = ctk.CTkSwitch(lower_frame, text="Lock Theme", variable=self.switch_var_2, onvalue="on", offvalue="off")
        lock_theme.grid(row=0, column=3, padx=10)
    
    # Openning browser hyperlink
    def web_view(self):
        webbrowser.open("https://www.facebook.com/profile.php?id=61557377445231")
      
        
    # The Log Out Function    
    def log_out(self):
        self.dashboard_window.withdraw() 
        # Creating a new window object
        new_app = main()
        new_app.mainloop()
    # Method to change themes
    
    def switch_theme_event(self):
        if self.switch_var_1.get() == "on" and self.switch_var_2.get()== "off":
            ctk.set_appearance_mode("light")
        
        if self.switch_var_1.get()=="off" and self.switch_var_2.get()=="off":
            ctk.set_appearance_mode("system")
            
    # Bottom section of the balance display window
    def balance_widget(self): 
        sizes = 400
        self.balance_bottom = ctk.CTkFrame(self.balance_frame, width=sizes, border_color="Brown", corner_radius=10, border_width=2)
        self.balance_bottom.pack(fill=X, pady=5, padx=4)
        
        title = ctk.CTkLabel(self.balance_bottom, text="Balance:", font=ctk.CTkFont(
            size=16,
            weight="bold"
        ))
        title.pack(pady=4)
        display = ctk.CTkLabel(self.balance_bottom, text=f"Ksh {get_balance(self.user_name_entry.get())}", font=ctk.CTkFont(
            size=24,
            weight="bold"
        ))
        display.pack(pady=4)
            
 
# Running
app = main()
app.mainloop()


