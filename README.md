⚙️ How the Universal Data Pipeline Works
This script acts as an automated funnel. Instead of hardcoding specific column names (like Revenue or Age), it analyzes the underlying structure of any CSV file and cleans it dynamically.

1. Data Ingestion & Validation

The script asks the user for a file path. It uses the os module to verify the file actually exists before trying to open it, preventing basic crash errors.

It loads the CSV into a Pandas DataFrame and prints a quick snapshot (the .head()) and the dimensions (the .shape) so the user can see what the raw data looks like.

2. Automated Cleaning (The Core Logic)

Dropping Dead Weight: It immediately scans for and deletes any columns that are completely empty.

Dynamic Type Separation: It uses select_dtypes to split the dataset into two distinct categories: Mathematical Data (numbers) and Categorical Data (text).

Smart Imputation: * If a number is missing, it calculates the mathematical average (mean()) of that specific column and fills the blank with it.

If text is missing, it safely replaces the blank space with the word "Unknown".

3. Dynamic Aggregation (Data Grouping)

To prove it can manipulate data without knowing the column names in advance, the script automatically grabs the very first text column it finds and the very first number column it finds.

It runs a Pandas .groupby() to calculate the average of those numbers and count the total rows for each text category, mimicking a standard SQL GROUP BY report.

4. Safe Export

It takes the freshly cleaned DataFrame and exports it back to your computer using .to_csv().

It automatically adds cleaned_ to the front of the filename so the original raw dataset is never accidentally overwritten or destroyed.
