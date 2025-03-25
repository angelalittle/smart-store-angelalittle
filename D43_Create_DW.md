# Create an Initial Data Warehouse Creation Script

Goal: Use SQLite to define and create tables for your data warehouse. The script will set up the database schema based on your design.

In this step, we'll sketch out a new script but leave the details until later. 
This is a common way to develop code. First, get the basics running, and then complete the details. 

## Open Project in VS Code, Create a New Script

Open your project in VS Code. Create a file in your scripts folder named create_dw.py. 

Start with some initial code. Maybe something like the following. 

```python
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


def create_dw() -> None:
    """Create the data warehouse by creating customer, product, and sale tables."""
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(DB_PATH)

        # Will need more magic here....

        # Close the connection
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

In the Python script, use the sqlite3 library in the Python Standard Library to connect to SQLite and execute SQL commands to create tables.

- Define the schema for your fact and dimension tables.
- Ensure that your fact table includes foreign keys that reference the primary keys of your dimension tables.
- Follow conventions for naming tables and columns.

## Activate .venv and Excecute the Script

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

Execute the script to create the database and tables - use the command that works for your operating system. 

In Windows / PowerShell

```shell
py scripts/create_dw.py
```

In Mac / Linux terminal

```shell
python3 scripts/create_dw.py
```

## Verify And Plan Ahead

Make sure this version runs correctly. 
In the next session, we'll write code to create the tables. 
We will NOT populate them. We'll do that separately using our prepared data in Module 5. 
