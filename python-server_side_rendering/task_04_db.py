from flask import Flask, request, render_template
import json
import csv
import sqlite3

app = Flask(__name__)


# --------------------------
# READ JSON
# --------------------------
def read_json_products():
    try:
        with open("products.json", "r") as file:
            return json.load(file)
    except Exception as e:
        print(f"JSON read error: {e}")
        return None


# --------------------------
# READ CSV
# --------------------------
def read_csv_products():
    products = []
    try:
        with open("products.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
        return products
    except Exception as e:
        print(f"CSV read error: {e}")
        return None


# --------------------------
# READ FROM SQLITE DATABASE
# --------------------------
def read_sql_products(product_id=None):
    try:
        conn = sqlite3.connect("products.db")
        cursor = conn.cursor()

        if product_id:
            cursor.execute(
                "SELECT id, name, category, price FROM Products WHERE id = ?",
                (product_id,)
            )
        else:
            cursor.execute("SELECT id, name, category, price FROM Products")

        rows = cursor.fetchall()
        conn.close()

        # Convert rows to dictionary list
        products = [
            {
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            }
            for row in rows
        ]

        return products

    except Exception as e:
        print(f"SQL read error: {e}")
        return None


# --------------------------
# MAIN ROUTE
# --------------------------
@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    # Validate source
    if source not in ["json", "csv", "sql"]:
        return render_template(
            "product_display.html",
            error="Wrong source",
            products=None
        )

    # Parse id if given
    if product_id:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template("product_display.html",
                                   error="Invalid ID format",
                                   products=None)

    # Select data source
    if source == "json":
        data = read_json_products()

    elif source == "csv":
        data = read_csv_products()

    elif source == "sql":
        data = read_sql_products(product_id)

    # When SQL ID provided → already filtered, so skip filtering step
        if product_id is not None:
            if not data:
                return render_template("product_display.html",
                                       error="Product not found",
                                       products=None)
            return render_template("product_display.html", products=data)

    # Handle general read errors
    if data is None:
        return render_template("product_display.html",
                               error="Error reading data file",
                               products=None)

    # Filter JSON/CSV data by ID if needed
    if product_id is not None:
        filtered = [p for p in data if p["id"] == product_id]
        if not filtered:
            return render_template("product_display.html",
                                   error="Product not found",
                                   products=None)
        return render_template("product_display.html", products=filtered)

    # No ID → return full list
    return render_template("product_display.html", products=data)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
