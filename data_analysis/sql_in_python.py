# This program demonstrates basic database management using SQL in Python.

import sqlite3

# Connect to a database and create a table
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS customers (id INTEGER PRIMARY KEY, name TEXT, email TEXT)")

# Insert some data into the table
cursor.execute("INSERT INTO customers (name, email) VALUES (?, ?)", ("John Doe", "john.doe@example.com"))
cursor.execute("INSERT INTO customers (name, email) VALUES (?, ?)", ("Jane Doe", "jane.doe@example.com"))
cursor.execute("INSERT INTO customers (name, email) VALUES (?, ?)", ("Bob Smith", "bob.smith@example.com"))
conn.commit()

# Retrieve data from the table
cursor.execute("SELECT * FROM customers")
rows = cursor.fetchall()

# Print the retrieved data
print("Retrieved Data:")
for row in rows:
    print(row)

# Update a record in the table
cursor.execute("UPDATE customers SET email = ? WHERE id = ?", ("jane.doe2@example.com", 2))
conn.commit()

# Retrieve the updated record from the table
cursor.execute("SELECT * FROM customers WHERE id = ?", (2,))
row = cursor.fetchone()

# Print the updated record
print("Updated Record:")
print(row)

# Delete a record from the table
cursor.execute("DELETE FROM customers WHERE id = ?", (3,))
conn.commit()

# Retrieve the remaining records from the table
cursor.execute("SELECT * FROM customers")
rows = cursor.fetchall()

# Print the remaining records
print("Remaining Records:")
for row in rows:
    print(row)

# Close the connection to the database
conn.close()
