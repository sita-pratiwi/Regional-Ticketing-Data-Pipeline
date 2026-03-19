import pandas as pd

# Dummy exchange rates to USD
exchange_rates = {
    "IDR": 0.000065,
    "MYR": 0.21,
    "SGD": 0.74
}

def load_data():
    df_id = pd.read_csv("sales_id.csv")
    df_my = pd.read_csv("sales_my.csv")
    df_sg = pd.read_csv("sales_sg.csv")
    
    return df_id, df_my, df_sg

def transform_data(df, country_code):
    df["Country"] = country_code
    df["Price_USD"] = df.apply(
        lambda row: row["Price"] * exchange_rates[row["Currency"]], axis=1
    )
    return df

def main():
    df_id, df_my, df_sg = load_data()
    
    df_id = transform_data(df_id, "Indonesia")
    df_my = transform_data(df_my, "Malaysia")
    df_sg = transform_data(df_sg, "Singapore")
    
    # Combine all datasets
    df_all = pd.concat([df_id, df_my, df_sg], ignore_index=True)
    
    print("=== Combined Data ===")
    print(df_all)

    # Save output
    df_all.to_csv("regional_sales_usd.csv", index=False)
    print("\nData successfully transformed and saved!")

if __name__ == "__main__":
    main()

Dummy CSV Data
Event,Price,Currency
Concert A,500000,IDR
Concert B,750000,IDR
Concert C,650000,IDR
Concert D,800000,IDR
Concert E,550000,IDR

sales_my.csv
Event,Price,Currency
Concert A,200,MYR
Concert B,250,MYR
Concert C,300,MYR
Concert D,180,MYR
Concert E,220,MYR

sales_sg.csv
Event,Price,Currency
Concert A,120,SGD
Concert B,150,SGD
Concert C,180,SGD
Concert D,130,SGD
Concert E,160,SGD
