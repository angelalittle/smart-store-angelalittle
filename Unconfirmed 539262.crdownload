import pandas as pd
import sqlite3
import pathlib
import sys

# Add project root to Python path for local imports
PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

# Constants
DW_DIR = pathlib.Path("data") / "dw"
DB_PATH = DW_DIR / "smart_sales.db"
OLAP_OUTPUT_DIR = pathlib.Path("data") / "olap_cubing_outputs"

# Create output folder if it doesn't exist
OLAP_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def load_sales_data() -> pd.DataFrame:
    """Load sales and customer data, then merge them on customer_id."""
    try:
        conn = sqlite3.connect(DB_PATH)
        sales_df = pd.read_sql_query("SELECT * FROM sale", conn)
        customers_df = pd.read_sql_query("SELECT * FROM customer", conn)
        conn.close()

        # Merge sales and customer data on customer_id
        merged_df = pd.merge(sales_df, customers_df[["customer_id", "region"]], on="customer_id", how="left")
        print("Sales and customer data successfully loaded and merged.")
        return merged_df
    except Exception as e:
        print(f"Error loading or merging data: {e}")
        raise



def generate_column_names(dimensions: list, metrics: dict) -> list:
    """Generate clear column names for the OLAP cube."""
    columns = dimensions.copy()
    for col, aggs in metrics.items():
        if isinstance(aggs, list):
            for func in aggs:
                columns.append(f"{col}_{func}")
        else:
            columns.append(f"{col}_{aggs}")
    return [col.rstrip("_") for col in columns]


def create_olap_cube(df: pd.DataFrame, dimensions: list, metrics: dict) -> pd.DataFrame:
    """Aggregate sales data into an OLAP cube format."""
    try:
        grouped = df.groupby(dimensions)
        cube = grouped.agg(metrics).reset_index()
        cube["transaction_ids"] = grouped["transaction_id"].apply(list).reset_index(drop=True)
        cube.columns = generate_column_names(dimensions, metrics) + ["transaction_ids"]
        print(f"OLAP cube created using dimensions: {dimensions}")
        return cube
    except Exception as e:
        print(f"Error during OLAP cube creation: {e}")
        raise


def save_cube_to_csv(cube: pd.DataFrame, filename: str) -> None:
    """Save the OLAP cube as a CSV file."""
    try:
        output_path = OLAP_OUTPUT_DIR / filename
        cube.to_csv(output_path, index=False)
        print(f"OLAP cube saved to: {output_path}")
    except Exception as e:
        print(f"Error saving cube to CSV: {e}")
        raise


def main():
    """Run the OLAP cubing process end-to-end."""
    print("Starting OLAP cube generation process...")

    # Step 1: Load data
    df = load_sales_data()

    # Step 2: Create additional time-based columns
    df["sale_date"] = pd.to_datetime(df["sale_date"])
    df["day_of_week"] = df["sale_date"].dt.day_name()
    df["month"] = df["sale_date"].dt.month
    df["month_name"] = df["sale_date"].dt.month_name()
    df["year"] = df["sale_date"].dt.year
    df["date"] = df["sale_date"].dt.strftime("%m/%d/%y")

    # Step 3: Define dimensions and metrics
    dimensions = ["date", "day_of_week", "product_id", "customer_id", "month", "month_name", "region"]
    metrics = {
        "sale_amount": ["sum", "mean"],
        "transaction_id": "count"
    }

    # Step 4: Create OLAP cube
    cube = create_olap_cube(df, dimensions, metrics)

    # Step 5: Save the result
    save_cube_to_csv(cube, "multidimensional_olap_cube.csv")

    print("OLAP cube generation completed.")


if __name__ == "__main__":
    main()
