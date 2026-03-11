import pandas as pd
import numpy as np
import os

def process_dynamic_dataset(file_path):
    # 1. Verification & Loading
    if not os.path.exists(file_path):
        print(f"🛑 Error: The file '{file_path}' was not found. Check the path and try again.")
        return

    print(f"\n📂 Loading dataset from: {file_path}...")
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"🛑 Error reading file: {e}")
        return
        
    print("\n--- 📊 RAW DATA PREVIEW ---")
    print(df.head())
    print(f"\nInitial Shape: {df.shape[0]} rows, {df.shape[1]} columns")

    # 2. Automated Data Cleaning Protocol
    print("\n--- 🧹 INITIATING CLEANING PROTOCOL ---")
    
    # Drop columns that are 100% empty
    df.dropna(axis=1, how='all', inplace=True)
    
    # Isolate numeric columns vs text (categorical) columns
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    categorical_cols = df.select_dtypes(include=['object']).columns

    # Fill missing numbers with the mathematical mean of that specific column
    for col in numeric_cols:
        if df[col].isnull().sum() > 0:
            mean_val = df[col].mean()
            df.fillna({col: mean_val}, inplace=True)
            print(f"✅ Filled missing numeric values in '{col}' with mean: {mean_val:.2f}")

    # Fill missing text fields with 'Unknown'
    for col in categorical_cols:
         if df[col].isnull().sum() > 0:
             df.fillna({col: 'Unknown'}, inplace=True)
             print(f"✅ Filled missing text values in '{col}' with 'Unknown'")

    # 3. Dynamic Aggregation
    # Automatically grab the first text column to group by, and the first numeric to calculate
    if len(categorical_cols) > 0 and len(numeric_cols) > 0:
        group_col = categorical_cols[0]
        agg_col = numeric_cols[0]
        
        print(f"\n--- 📈 AUTOMATED AGGREGATION SUMMARY ---")
        print(f"Grouping by '{group_col}' and calculating average '{agg_col}'...\n")
        
        summary = df.groupby(group_col).agg({
            agg_col: 'mean',
            group_col: 'count'
        }).rename(columns={group_col: 'Total_Rows', agg_col: f'Avg_{agg_col}'})
        
        print(summary)
    else:
        print("\n⚠️ Could not perform automated grouping: Dataset needs at least one text and one numeric column.")

    # 4. Export the Processed Data
    output_name = "cleaned_" + os.path.basename(file_path)
    df.to_csv(output_name, index=False)
    print(f"\n🚀 Success! Processed dataset exported as: {output_name}")

if __name__ == "__main__":
    print("=== THE UNIVERSAL DATA PIPELINE ===")
    user_input = input("Enter the path to your CSV file (e.g., raw_client_data.csv): ")
    process_dynamic_dataset(user_input)
