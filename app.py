<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Inventory Entry Form</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 40px;
      background-color: #f9f9f9;
    }
    form {
      background: #fff;
      padding: 20px;
      border-radius: 8px;
      max-width: 600px;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }
    label {
      display: block;
      margin-top: 15px;
      font-weight: bold;
    }
    input, textarea {
      width: 100%;
      padding: 8px;
      margin-top: 5px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
    button {
      margin-top: 20px;
      padding: 10px 20px;
      background-color: #0078D4;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    button:hover {
      background-color: #005fa3;
    }
  </style>
</head>
<body>

  <h2>Inventory Entry Form</h2>

  <form method="POST" action="https://script.google.com/macros/s/AKfycbzxkcYCwzdYk0MVYy0rAABdcKwZDiwpI2elDDxjK1ynx2fhJcDNsMR84Z8_rkFiLwqzMw/exec">
    <label for="ProductName">Product Name:</label>
    <input type="text" id="ProductName" name="ProductName" required>

    <label for="Brand_id">Brand ID:</label>
    <input type="text" id="Brand_id" name="Brand_id">

    <label for="category_id">Category ID:</label>
    <input type="text" id="category_id" name="category_id">

    <label for="subcategory">Subcategory:</label>
    <input type="text" id="subcategory" name="subcategory">

    <label for="size">Size:</label>
    <input type="text" id="size" name="size">

    <label for="unit_of_measurment">Unit of Measurement:</label>
    <input type="text" id="unit_of_measurment" name="unit_of_measurment">

    <label for="productDescription">Product Description:</label>
    <textarea id="productDescription" name="productDescription"></textarea>

    <label for="ThumbnailURL">Thumbnail URL:</label>
    <input type="text" id="ThumbnailURL" name="ThumbnailURL">

    <label for="MRP">MRP:</label>
    <input type="number" id="MRP" name="MRP" step="0.01">

    <label>
      <input type="checkbox" name="DiscountEligible"> Discount Eligible
    </label>

    <label>
      <input type="checkbox" name="IsActive"> Is Active
    </label>

    <label for="BatchNumber">Batch Number:</label>
    <input type="text" id="BatchNumber" name="BatchNumber">

    <label for="ExpiryDate">Expiry Date:</label>
    <input type="date" id="ExpiryDate" name="ExpiryDate">

    <label for="ReorderLevel">Reorder Level:</label>
    <input type="number" id="ReorderLevel" name="ReorderLevel">

    <label for="Tags">Tags:</label>
    <input type="text" id="Tags" name="Tags">

    <button type="submit">Submit</button>
  </form>

</body>
</html>
