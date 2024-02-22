import pandas as pd
import sqlite3

def extract_item_quantities(database_name):
    try:
        conn = sqlite3.connect(database_name)
        query = """
                SELECT c.customer_id, 
                       i.item_name, 
                       SUM(CASE WHEN o.quantity IS NULL THEN 0 ELSE o.quantity END) AS total_quantity
                FROM Customer c
                JOIN Sales s ON c.customer_id = s.customer_id
                JOIN Orders o ON s.sales_id = o.sales_id
                JOIN Items i ON o.item_id = i.item_id
                WHERE c.age BETWEEN 18 AND 35
                GROUP BY c.customer_id, i.item_name
                HAVING total_quantity > 0;
                """
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df
    except sqlite3.Error as e:
        print(e)
        return None

def main():
    database_name = "company_xyz.db"
    result_df = extract_item_quantities(database_name)
    if result_df is not None:
        print(result_df)

if __name__ == "__main__":
    main()