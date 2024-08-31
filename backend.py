import mysql.connector
import values

# Connecting to a database
def connection_draft():
    try:
        connection= mysql.connector.connect(
            user=values.mysq_user,
            host= values.host,
            password = values.msql_password
        )
        print(f"Connection in the server {connection} created succesfully")
        
    except:
        print("Connection Failed")
    finally:
        cursor = connection.cursor()
        # cursor.execute("CREATE DATABASE IF NOT EXISTS sql8703994")

# Method For Creating connection
def createConnection(password):
    db_connection = mysql.connector.connect(
        user=values.mysq_user,
        host= values.host,
        password = password,
        database=values.database
        )
    print("Connection Succesfully Created")
    return db_connection



accounts_table_Query = """CREATE TABLE IF NOT EXISTS accounts(
    id_number INT NOT NULL,
    firstName VARCHAR(255) NOT NULL,
    surname VARCHAR(255),
    lastName VARCHAR(255) NOT NULL,
    birthYear INT NOT NULL,
    location VARCHAR(255) NOT NULL,
    phoneNumber VARCHAR(12) NOT NULL,
    userPassword VARCHAR(255) NOT NULL,
    pinNumber INT NOT NULL,
    accountBalance DECIMAL DEFAULT 0.00,
    PRIMARY KEY (id_number, phoneNumber)
    )"""
    

transaction_table_query = """CREATE TABLE IF NOT EXISTS `transaction` (
    transactionId INT NOT NULL AUTO_INCREMENT,
    id_number INT NOT NULL,
    transactionType VARCHAR(255),
    transactionAmount DECIMAL(10, 2) NOT NULL,
    transactionDate TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    recepientAccount INT NOT NULL,
    PRIMARY KEY (transactionId),
    FOREIGN KEY (id_number) REFERENCES accounts(id_number)
)"""

# Table Creation
def create_tables():
    connection = createConnection(values.msql_password)
    my_cursor = connection.cursor()
    my_cursor.execute(accounts_table_Query)
    print("Accounts table created")
    my_cursor.execute(transaction_table_query)
    print("Transaction table created")
    # Committing
    connection.commit()
    connection.close()
    print("Connection closed")
