
# Product & Supplier API

This is a simple API that allows you to manage products and suppliers. It was built using Python Flask and PostgreSQL database. You can use Docker to run this application on your machine.

## Requirements
To run this application, you will need to have the following tools installed on your machine:
- Docker


## Getting started
To get started, follow these steps:

- Clone this repository to your local machine.
- Navigate to the cloned directory.
- Run ```docker-compose up``` to start the application.

Access the application by visiting http://localhost:5000 in your web browser.

## Usage
Here are the available endpoints for this API:

Test with POSTMAN

`GET /suppliers`: Get all suppliers.

`GET /suppliers/<int:id>`: Get a specific supplier by ID.

`POST /suppliers`: Create a new supplier.

`PUT /suppliers/<int:id>`: Update an existing supplier.

`DELETE /suppliers/<int:id>`: Delete a specific supplier by ID.

`GET /suppliers/<int:id>/products`: Get all products for a specific supplier by ID.

`GET /products`: Get all products.

`GET /products/<int:id>`: Get a specific product by ID.

`POST /products`: Create a new product.

`PUT /products/<int:id>`: Update an existing product.

`DELETE /products/<int:id>`: Delete a specific product by ID.SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
