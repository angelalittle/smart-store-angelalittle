
## ✅ Project 1 – Project Initialization & Setup

### Goals
- Set up a professional Python environment for BI projects
- Create a GitHub repository and clone it locally
- Organize project folders and add starter files

### Key Steps Completed
- Installed required tools (Python, Git, VS Code)
- Created and cloned repository: `smart-store-yourname`
- Initialized the project with a `README.md`, `.gitignore`, and `requirements.txt`
- Created key folders:

```
smart-store-yourname/
├── data/
│   └── raw/
├── scripts/
├── utils/
├── .gitignore
├── README.md
└── requirements.txt
```

- Added sample raw data files:
  - `customers_data.csv`
  - `products_data.csv`
  - `sales_data.csv`
- Opened CSVs to explore the data manually

### Notes
- Ensured a strong foundation and clean structure for future BI work
- Used Git frequently for version control: `git add`, `git commit`, `git push`

---

## ✅ Project 2 – Python Environment & First Scripts

### Goals
- Create and activate a local Python virtual environment (`.venv`)
- Install required packages using `requirements.txt`
- Run and verify Python scripts in terminal

### Key Steps Completed
- Created and activated `.venv`:
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
  ```
- Added utility and script files:
  - `utils/logger.py`
  - `scripts/data_prep.py`
- Ran script:
  ```bash
  python3 scripts/data_prep.py
  ```
- Saved progress with Git:
  ```bash
  git add .
  git commit -m "Add starter scripts"
  git push
  ```

### Notes
- Practiced using external packages like `pandas`
- Maintained version control with clean commit messages
- README updated after each task

---

## ✅ Project 3 – Data Cleaning for ETL

### Files Created
- `scripts/data_scrubber.py`: Reusable cleaning class
- `scripts/data_prep.py`: Central script to clean raw data for ETL
- `tests/test_data_scrubber.py`: Unit tests to validate cleaning functions

### Data Cleaning Tasks
- Removed duplicates
- Filled or dropped missing values
- Standardized column names
- Trimmed extra whitespace
- Converted date fields

### Cleaned Output
- `Data/Prepared/customers_data_cleaned.csv`
- `Data/Prepared/products_data_cleaned.csv`
- `Data/Prepared/sales_data_cleaned.csv`

---

## ✅ Project 4 – Create and Populate Data Warehouse

### Goals
- Design a star schema for analytical querying
- Create and load a functional SQLite data warehouse
- Support future BI and dashboard tools

### Files Created
- `scripts/etl_to_dw.py`: ETL script to create schema and load data
- `data/dw/smart_sales.db`: Final data warehouse

### Schema Overview
- **Fact Table**: `sales_transaction`
- **Dimension Tables**: `customer`, `product`
- Star schema enables analysis by customer, product, region, and time

### Data Pipeline Steps
1. Read cleaned files from `Data/Prepared/`
2. Rename columns to match the schema
3. Create and connect to SQLite database
4. Drop existing records
5. Insert data into:
   - `customer`
   - `product`
   - `sales_transaction`

### Populated Tables (Example View)

| Table              | Sample Columns                                           |
|-------------------|----------------------------------------------------------|
| `customer`         | customer_id, name, region, join_date, loyalty_points, gender |
| `product`          | product_id, product_name, category, unit_price          |
| `sales_transaction`| transaction_id, sale_date, customer_id, product_id, sale_amount, bonus_points, payment_type |

### Success Message
After running the script:
```bash
python3 scripts/etl_to_dw.py
```

Output:
```
✅ Data warehouse loaded successfully!


```


# P5: Cross-Platform Reporting with Power BI & Spark

This project uses PySpark and SQLite to perform cross-platform business intelligence analysis on smart store sales data.  
We connected to a local SQLite database using Spark JDBC, queried sales, customer, and product tables, and created temporary SQL views.  
Using Spark SQL, we identified top customers by total spend, analyzed sales trends over time, and grouped results by product category and payment type.  
Visualizations include a bar chart of top customers and a line chart showing monthly sales trends in 2024.  
All code, queries, and visuals were executed on macOS using Jupyter Notebook and documented here.

# P6: OLAP Sales by Region 

# 📊 Smart Sales OLAP Analysis

This project is part of the BI & Data Analytics course (P6). It applies OLAP techniques to uncover actionable sales insights using Python, Pandas, and Seaborn.

## 🎯 Business Goal
**Maximize sales by identifying top-performing regions and customer segments.**  
Use insights to make data-driven decisions on where to focus inventory and marketing efforts.

---

## 📐 OLAP Analysis Techniques Used

| Technique   | Description |
|-------------|-------------|
| **Slicing** | Total sales by region |
| **Dicing**  | Region × Customer Segment |
| **Drilldown** | Monthly sales trends per region |

---

## 📈 Key Insights

- **🥇 East region leads in total sales**
- **🏢 Enterprise customers dominate the South**
- **📆 Q2 shows peak sales in most regions, especially East**

### 📌 Suggested Business Actions

- Shift inventory and marketing focus to **East region**
- Target **Enterprise** customers more heavily in the South
- Launch campaigns in Q2 to capitalize on seasonal surges

---

## 🛠 Tools & Tech

- Python 3
- Jupyter Notebook
- Pandas, Matplotlib, Seaborn
- Git & GitHub

---

## 📁 Notebooks

- `P6_OLAP_Sales_by_Region.ipynb`: Main OLAP analysis notebook with visualizations and insights

---

## ✍️ Author

**Brandon J.**  
[GitHub: @brandonjbbb](https://github.com/brandonjbbb)

