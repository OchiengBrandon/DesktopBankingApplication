from backend import createConnection
import values
from tkinter import messagebox
import customtkinter as ctk

connection = createConnection(values.msql_password)
cursor = connection.cursor()



# LOGICS
# Account Creation
def account_creation_logic(first_name, surname, last_name, id_number, dob, email,location, telno, pin,pass2):
    connection = createConnection(values.msql_password)
    cursor = connection.cursor()
    theQuery = "INSERT INTO accounts(id_number,firstName,surname,lastname,birthYear,location,phoneNumber,userPassword,pinNumber,accountBalance) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (id_number,first_name, surname, last_name, dob, location, telno, pass2, pin, 0.00)
    cursor.execute(theQuery, val)
    # Closing and saving 
    connection.commit()
    messagebox.showinfo("Account", "Account Created Sucessfully")
    connection.close()

# Getting username
def get_username(user_id):
    cursor.execute(f"SELECT firstName FROM accounts WHERE id_number = {user_id}")
    for row in cursor:
        username = row[0]
    return username

# Getting balance
def get_balance(user_id):
    cursor.execute(f"SELECT accountBalance FROM accounts WHERE id_number = {user_id}")
    for row in cursor:
        balance= row[0]
    return float(balance)

# Deposit 
def deposit_update(user_id, amount):
    current_balance = get_balance(user_id)
    new_balance = float(current_balance + float(amount))
    cursor.execute(f"UPDATE accounts SET accountBalance = {new_balance} WHERE id_number = {user_id}")
    connection.commit()

# Routing
def transaction_routing(recepient_account, amount):
    try:
        current_balance = get_balance(recepient_account)
        new_balance = float(current_balance + float(amount))
        cursor.execute(f"UPDATE accounts SET accountBalance = {new_balance} WHERE id_number = {recepient_account}")
        connection.commit()
    except:
        pass
# Received Statement
def received_statement(recepient_account, amount, senders_account ):
    transactionType = "Received"
    try:
        transaction_logic(recepient_account, transactionType, amount, senders_account)
    except:
        pass
        # To the routing reference, EDIT
    
# Login from the back End
def login_logic(user_id, password):
    connection = createConnection(values.msql_password)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM accounts WHERE id_number= %s AND userPassword= %s",(user_id, password))
    account = cursor.fetchone()
    if account: 
        return 1


# Deductive Transaction
def deduction_validation(user_id, amount):
    current_balance = get_balance(user_id)
    if int(current_balance) != 0: 
        if float(amount)<= float(current_balance + 100):
            return 1
        else: 
            return 0
    else:
        return 0
    
# Pin Validation
def pin_validation(user_id):
    cursor.execute(f"SELECT pinNumber FROM accounts WHERE id_number = {user_id}")
    for row in cursor:
        pin = row[0]
    return pin

# Update Deduction
def deduction_update(user_id, amount):
    current_balance = get_balance(user_id)
    new_balance = float(current_balance - float(amount))
    cursor.execute(f"UPDATE accounts SET accountBalance = {new_balance} WHERE id_number = {user_id}")
    connection.commit()
    
# Transaction Logic
def transaction_logic(id_number, transaction_type, amount, recepient_account):
    theQuery = "INSERT INTO transaction(id_number, transactionType, transactionAmount, recepientAccount) VALUES(%s, %s,%s, %s)"
    val = (id_number, transaction_type, amount, recepient_account)
    cursor.execute(theQuery, val)
    connection.commit()
    
# The Transaction history    
def transaction_history_logic(user_id, location1, location2, location3, location4):
    cursor.execute(f"SELECT recepientAccount,transactionDate, transactionAmount, transactionType FROM transaction WHERE id_number = {user_id} ORDER BY transactionDate DESC ")
    for result in cursor:
        ctk.CTkLabel(location1, text=result[0]).pack()
        ctk.CTkLabel(location2, text=result[1]).pack()
        ctk.CTkLabel(location3, text=result[2]).pack()
        ctk.CTkLabel(location4, text=result[3]).pack()
        

        



    
