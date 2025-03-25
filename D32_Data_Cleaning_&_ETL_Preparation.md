# D3.2 Data Cleaning & ETL Preparation

Data cleaning and ETL (Extract, Transform, Load) preparation are critical steps in the Business Intelligence (BI) process. 
They ensure that the data feeding into analytics tools is accurate, consistent, and usable. 
This module covers the key concepts, challenges, and techniques associated with preparing data for ETL.

## Understanding Data Cleaning

Data cleaning involves identifying and correcting inaccuracies and inconsistencies in data to improve its quality.

### Key Tasks in Data Cleaning
- **Removing Duplicates**: Duplicate data can skew analysis and lead to inaccurate results.
- **Handling Missing Values**: Missing data needs to be addressed either by imputation or removal, depending on the context.
- **Correcting Errors**: Typos, mislabeled categories, and other inaccuracies must be corrected to ensure the integrity of your data.
- **Standardizing Data Formats**: Dates, categorical labels, and other data types should be standardized to ensure consistency across the dataset.

### Techniques and Tools
- **Manual Inspection**: Useful for small datasets where anomalies can be easily spotted.
- **Automated Cleaning Tools**: Software solutions can identify and correct inconsistencies in larger datasets.
  - **Examples**: Pandas in Python, DataCleaner, Talend.

## ETL Preparation

ETL stands for Extract, Transform, Load. Before we can do that, we need to get our data ready for the ETL process. General guidelines include:

- Verify attribute names are clear with units for numerical traits. 
- Attribute names have been standardized where possible. 
- Verify all rows have the correct number of entries. 
- Verify all duplication has been removed. 
- Verify all bad, missing, or out of range records have been removed. 
- Verify each column adheres to the expected data type (e.g., dates are in date/time formats, identifiers like phone numbers are consistent). 
- Verify that collection and usage comply with relevant laws and regulations.
  
Once these checks are completed, data is ready for the ETL process. 
This preparation phase is crucial for minimizing issues during data transformation and load stages, ultimately leading to more reliable and robust BI outputs.
