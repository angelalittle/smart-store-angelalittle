# Implement the Data Warehouse (Finish Create DW Script for Initial Columns)

Here we will complete our goal to use SQLite to define and create tables for a data warehouse. The script will set up the database schema based on your design.

## Activate .venv 

Same as before. If not already activated, activate your .venv.

In VS Code, open a terminal. 
Activate the local project virtual environment if not already active. 
Use the variation of this command that works on your machine. 

In Windows / PowerShell (for example)

```shell
.\.venv\Scripts\activate
```

In Mac / Linux terminal (for example)

```shell
source .venv/bin/activate
```

## Execute the Script

Same as before, use this command to execute the script as you progressively build it - use the command that works for your operating system. 

In Windows / PowerShell

```shell
py scripts/create_dw.py
```

In Mac / Linux terminal

```shell
python3 scripts/create_dw.py
```

## Complete the Script 

Finish the code to actually create tables using the initial columns, but do not populate them. We will populate our DW in Module 5. 

To allow the script to be re-run while we are finalizing it, delete the new database if it exists before each run. 

-----

## Example of DW Create Script

Here is an example of the type of code needed to use as a reference. 
Your final P4 version will also reflect your additional columns and your schema design. 

```python
"""
Module 4: Data Warehouse Creation Script
File: scripts/dw_create.py

This script handles the creation of the SQLite data warehouse. It creates tables
for customer, product, and sale in the 'data/smart_sale.db' database.
Each table creation is handled in a separate function for easier testing and error handling.
"""

import sqlite3
import sys
import pathlib

# For local imports, temporarily add project root to Python sys.path
PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

# Now we can import local modules
from utils.logger import logger  # noqa: E402

# Constants
DW_DIR: pathlib.Path = pathlib.Path("data").joinpath("dw")
DB_PATH: pathlib.Path = DW_DIR.joinpath("smart_sales.db")

# Ensure the 'data/dw' directory exists
DW_DIR.mkdir(parents=True, exist_ok=True)

# Delete data warehouse file if it exists
if DB_PATH.exists():
    try:
        DB_PATH.unlink()  # Deletes the file
        logger.info(f"Existing database {DB_PATH} deleted.")
    except Exception as e:
        logger.error(f"Error deleting existing database {DB_PATH}: {e}")

def create_customer_table(cursor: sqlite3.Cursor) -> None:
    """Create customer table in the data warehouse."""
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS customer (
                customer_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                region TEXT,
                join_date TEXT  -- ISO 8601 format recommended for SQLite
            )
        """)
        logger.info("customer table created.")
    except sqlite3.Error as e:
        logger.error(f"Error creating customer table: {e}")

def create_product_table(cursor: sqlite3.Cursor) -> None:
    """Create product table in the data warehouse."""
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS product (
                product_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT,
                unit_price_usd REAL NOT NULL
            )
        """)
        logger.info("product table created.")
    except sqlite3.Error as e:
        logger.error(f"Error creating product table: {e}")

def create_sale_table(cursor: sqlite3.Cursor) -> None:
    """Create sale table in the data warehouse."""
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sale (
                sale_id INTEGER PRIMARY KEY,
                customer_id INTEGER,
                product_id INTEGER,
                store_id INTEGER,
                campaign_id INTEGER,
                sale_date DATE,
                quantity INTEGER NOT NULL,
                sale_amount_usd INTEGER NOT NULL,
                FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
                FOREIGN KEY (product_id) REFERENCES product(product_id)
            )
        """)
        logger.info("sale table created.")
    except sqlite3.Error as e:
        logger.error(f"Error creating sale table: {e}")

def create_dw() -> None:
    """Create the data warehouse by creating customer, product, and sale tables."""
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Create tables
        create_customer_table(cursor)
        create_product_table(cursor)
        create_sale_table(cursor)

        # Commit the changes and close the connection
        conn.commit()
        conn.close()
        logger.info("Data warehouse created successfully.")

    except sqlite3.Error as e:
        logger.error(f"Error connecting to the database: {e}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
    finally:
        if conn:
            conn.close()

def main() -> None:
    """Main function to create the data warehouse."""
    logger.info("Starting data warehouse creation...")
    create_dw()
    logger.info("Data warehouse creation complete.")

if __name__ == "__main__":
    main()

```
