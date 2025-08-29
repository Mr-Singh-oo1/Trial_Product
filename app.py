from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# ✅ Your actual Google Apps Script Web App URL
GOOGLE_SHEETS_URL = "https://script.google.com/macros/s/AKfycbxANVbluF6EcFAFWLwoV9kbaC2eU5X7yv4SW3PwWEXKL6VcLvkhMRi7anG7YAz84XTxYg/exec"

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Extract form data
    form_data = {
        "Product_id": request.form.get("Product_id"),
        "ProductName": request.form.get("ProductName"),
        "Brand_id": request.form.get("Brand_id"),
        "category_id": request.form.get("category_id"),
        "subcategory": request.form.get("subcategory"),
        "size": request.form.get("size"),
        "unit_of_measurment": request.form.get("unit_of_measurment"),
        "productDescription": request.form.get("productDescription"),
        "ThumbnailURL": request.form.get("ThumbnailURL"),
        "MRP": request.form.get("MRP"),
        "DiscountEligible": request.form.get("DiscountEligible", "False"),
        "IsActive": request.form.get("IsActive", "False"),
        "BatchNumber": request.form.get("BatchNumber"),
        "ExpiryDate": request.form.get("ExpiryDate"),
        "ReorderLevel": request.form.get("ReorderLevel"),
        "Tags": request.form.get("Tags")
    }

    # Send data to Google Sheets
    try:
        response = requests.post(GOOGLE_SHEETS_URL, data=form_data)
        print("✅ Google Sheets response:", response.text)

        if response.status_code == 200 and "Success" in response.text:
            return f"✅ Product '{form_data['ProductName']}' submitted successfully!"
        else:
            return f"⚠️ Submission failed. Response: {response.text}"
    except Exception as e:
        print("❌ Error submitting to Google Sheets:", str(e))
        return f"❌ Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
