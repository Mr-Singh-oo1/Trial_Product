from flask import Flask, request, render_template
from datetime import datetime
import mysql.connector

app = Flask(__name__)

def insert_data(data):
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Password@123456789',
        database='inventory_tm_cosmetic_db'
    )
    cursor = conn.cursor()

    query = """
        INSERT INTO inventory (
            ProductName, Brand_id, category_id, subcategory, size,
            unit_of_measurment, productDescription, ThumbnailURL, MRP,
            DiscountEligible, IsActive, BatchNumber, ExpiryDate,
            ReorderLevel, Tags
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        data["ProductName"],
        data["Brand_id"],
        data["category_id"],
        data["subcategory"],
        data["size"],
        data["unit_of_measurment"],
        data["productDescription"],
        data["ThumbnailURL"],
        data["MRP"],
        data["DiscountEligible"],
        data["IsActive"],
        data["BatchNumber"],
        data["ExpiryDate"],
        data["ReorderLevel"],
        data["Tags"]
    )

    cursor.execute(query, values)
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    form_data = {
        "ProductName": request.form.get("ProductName"),
        "Brand_id": request.form.get("Brand_id"),
        "category_id": request.form.get("category_id"),
        "subcategory": request.form.get("subcategory"),
        "size": request.form.get("size"),
        "unit_of_measurment": request.form.get("unit_of_measurment"),
        "productDescription": request.form.get("productDescription"),
        "ThumbnailURL": request.form.get("ThumbnailURL"),
        "MRP": float(request.form.get("MRP") or 0),
        "DiscountEligible": 'DiscountEligible' in request.form,
        "IsActive": 'IsActive' in request.form,
        "BatchNumber": request.form.get("BatchNumber"),
        "ExpiryDate": request.form.get("ExpiryDate"),
        "ReorderLevel": int(request.form.get("ReorderLevel") or 0),
        "Tags": request.form.get("Tags")
    }

    if form_data["ExpiryDate"]:
        form_data["ExpiryDate"] = datetime.strptime(form_data["ExpiryDate"], "%Y-%m-%d")

    insert_data(form_data)

    return f"✅ Stored product: {form_data['ProductName']} with MRP ₹{form_data['MRP']} successfully."

if __name__ == '__main__':
    app.run(debug=True)