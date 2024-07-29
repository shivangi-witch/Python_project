import pandas as pd

# This part is like putting all the stickers in a pile.
def load_data(file_path):
    try:
        # We try to open the sticker pile (CSV file)
        df = pd.read_csv(file_path, parse_dates=['order_date'])
        return df
    except FileNotFoundError:
        # If we can't find the sticker pile, we tell you it's missing.
        print(f"Error: File '{file_path}' not found.")
        return None
    except pd.errors.ParserError:
        # If the sticker pile is messed up, we tell you it's broken.
        print("Error: Error parsing CSV file.")
        return None

# This part figures out how much each sticker is worth.
def calculate_revenue(df):
    # We look at how many toys are on the sticker and how much each toy costs.
    df['revenue'] = df['product_price'] * df['quantity']
    return df

# This part puts the stickers together by month.
def monthly_revenue(df):
    # We look at the month on each sticker and add up how much all the stickers in that month are worth.
    df['year_month'] = df['order_date'].dt.to_period('M')
    return df.groupby('year_month')['revenue'].sum().reset_index()

# This part puts the stickers together by toy.
def product_revenue(df):
    # We look at the toy on each sticker and add up how much all the stickers for that toy are worth.
    return df.groupby(['product_id', 'product_name'])['revenue'].sum().reset_index()

# This part puts the stickers together by who bought them.
def customer_revenue(df):
    # We look at who bought the sticker and add up how much all the stickers for that person are worth.
    return df.groupby('customer_id')['revenue'].sum().reset_index()

# This part finds the people who bought the most expensive toys.
def top_10_customers(df):
    # We sort the stickers by how much each person spent and pick the top 10.
    customer_rev = customer_revenue(df)
    return customer_rev.sort_values(by='revenue', ascending=False).head(10)

# This part does all the work.
def main():
    # We get all the stickers.
    df = load_data('orders.csv')
    if df is None:
        return

    # We figure out how much each sticker is worth.
    df = calculate_revenue(df)

    # We show you how much money we made each month.
    print("Monthly Revenue:")
    print(monthly_revenue(df))

    # We show you how much money each toy made.
    print("\nTotal Revenue by Product:")
    print(product_revenue(df))

    # We show you how much money each person spent.
    print("\nTotal Revenue by Customer:")
    print(customer_revenue(df))

    # We show you the 10 people who spent the most money.
    print("\nTop 10 Customers by Revenue:")
    print(top_10_customers(df))

if __name__ == '__main__':
    main()
