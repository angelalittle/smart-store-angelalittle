import pandas as pd
import sqlite3
import pathlib
import sys

# Set up paths
PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

# Constants
DW_DIR = pathlib.Path("data").joinpath("dw")
DB_PATH = DW_DIR.joinpath("smart_sales.db")
PREPARED_DATA_DIR = pathlib.Path("Data").joinpath("Prepared")

def create_schema(cursor: sqlite3.Cursor) -> None:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customer (
            customer_id INTEGER PRIMARY KEY,
            name TEXT,
            region TEXT,
            join_date TEXT,
            loyalty_points INTEGER,
            gender TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS product (
            product_id INTEGER PRIMARY KEY,
            product_name TEXT,
            category TEXT,
            unit_price REAL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales_transaction (
            transaction_id INTEGER PRIMARY KEY,
            customer_id INTEGER,
            product_id INTEGER,
            sale_date TEXT,
            sale_amount REAL,
            bonus_points REAL,
            payment_type TEXT,
            FOREIGN KEY (customer_id) REFERENCES customer (customer_id),
            FOREIGN KEY (product_id) REFERENCES product (product_id)
        )
    """)

def delete_existing_records(cursor: sqlite3.Cursor) -> None:
    cursor.execute("DELETE FROM customer")
    cursor.execute("DELETE FROM product")
    cursor.execute("DELETE FROM sales_transaction")

def insert_customers(customers_df: pd.DataFrame, cursor: sqlite3.Cursor) -> None:
    customers_df.to_sql("customer", cursor.connection, if_exists="append", index=False)

def insert_products(products_df: pd.DataFrame, cursor: sqlite3.Cursor) -> None:
    products_df.to_sql("product", cursor.connection, if_exists="append", index=False)

def insert_sales(sales_df: pd.DataFrame, cursor: sqlite3.Cursor) -> None:
    sales_df.to_sql("sales_transaction", cursor.connection, if_exists="append", index=False)

def load_data_to_db() -> None:
    conn = None
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        create_schema(cursor)
        delete_existing_records(cursor)

        # Load and rename customer columns
        customers_df = pd.read_csv(PREPARED_DATA_DIR.joinpath("customers_data_prepared.csv"), sep='\t')
        customers_df.columns = ['customer_id', 'name', 'region', 'join_date', 'loyalty_points', 'gender']

        # Load and rename product columns
        products_df = pd.read_csv(PREPARED_DATA_DIR.joinpath("products_data_prepared.csv"))
        products_df.columns = ['product_id', 'product_name', 'category', 'unit_price']

        # Load and transform sales columns
        sales_df = pd.read_csv(PREPARED_DATA_DIR.joinpath("sales_data_prepared.csv"), sep='\t')
        sales_df.columns = ['transaction_id', 'sale_date', 'customer_id', 'product_id', 'store_id', 'campaign_id', 'sale_amount', 'discount_percent', 'payment_type']
        sales_df = sales_df[['transaction_id', 'customer_id', 'product_id', 'sale_date', 'sale_amount', 'discount_percent', 'payment_type']]
        sales_df.rename(columns={'discount_percent': 'bonus_points'}, inplace=True)

        # Insert data
        insert_customers(customers_df, cursor)
        insert_products(products_df, cursor)
        insert_sales(sales_df, cursor)

        conn.commit()
        print("✅ Data warehouse loaded successfully!")

    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    load_data_to_db()
