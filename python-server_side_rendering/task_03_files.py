from flask import Flask, request, render_template
import json
import csv

app = Flask(__name__)

def read_json_products():
    """Reads product data from products.json."""
    try:
        with open("products.json", "r") as file:
            data = json.load(file)
            return data
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return None


def read_csv_products():
    """Reads product data from products.csv."""
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
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None
    
    return products


@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    # Validate source parameter
    if source not in ["json", "csv"]:
        return render_template("product_display.html",
                               error="Wrong source",
                               products=None)

    # Load appropriate data file
    if source == "json":
        data = read_json_products()
    else:
        data = read_csv_products()

    if data is None:
        return render_template("product_display.html",
                               error="Error reading data file",
                               products=None)

    # Filter by id if provided
    if product_id:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template("product_display.html",
                                   error="Invalid ID format",
                                   products=None)

        filtered = [p for p in data if p["id"] == product_id]

        if not filtered:
            return render_template("product_display.html",
                                   error="Product not found",
                                   products=None)

        return render_template("product_display.html",
                               products=filtered)

    # If no id provided, return all products
    return render_template("product_display.html",
                           products=data)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
