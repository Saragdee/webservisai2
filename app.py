from flask import Flask, jsonify, request
import psycopg2
import json

app = Flask(__name__)

# connect to database
conn = psycopg2.connect(host='db', port=5432, user='postgres', password='password', dbname='inventory')
cur = conn.cursor()

# create tables and insert initial data
def create_tables():
    # create suppliers table
    cur.execute('''CREATE TABLE IF NOT EXISTS suppliers
                   (id SERIAL PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    phone TEXT NOT NULL)''')

    # create products table
    cur.execute('''CREATE TABLE IF NOT EXISTS products
                   (id SERIAL PRIMARY KEY,
                    name TEXT NOT NULL,
                    price DECIMAL(10, 2) NOT NULL,
                    supplier_id INTEGER NOT NULL,
                    FOREIGN KEY (supplier_id) REFERENCES suppliers (id))''')

    # insert data from JSON file
    with open('data.json') as f:
        data = json.load(f)

    for supplier in data['suppliers']:
        cur.execute('SELECT COUNT(*) FROM suppliers WHERE name=%s', (supplier['name'],))
        count = cur.fetchone()[0]
        if count == 0:
            cur.execute('INSERT INTO suppliers (name, email, phone) VALUES (%s, %s, %s)', (supplier['name'], supplier['email'], supplier['phone']))
        
    for product in data['products']:
        cur.execute('SELECT COUNT(*) FROM products WHERE name=%s AND supplier_id=%s', (product['name'], product['supplier_id']))
        count = cur.fetchone()[0]
        if count == 0:
            cur.execute('INSERT INTO products (name, price, supplier_id) VALUES (%s, %s, %s)', (product['name'], product['price'], product['supplier_id']))



    conn.commit()

create_tables()

# routes for suppliers
@app.route('/suppliers', methods=['GET'])
def get_suppliers():
    cur.execute('SELECT * FROM suppliers')
    suppliers = cur.fetchall()
    return jsonify(suppliers)

@app.route('/suppliers', methods=['POST'])
def create_supplier():
    data = request.get_json()
    cur.execute('INSERT INTO suppliers (name, email, phone) VALUES (%s, %s, %s)',
                (data['name'], data['email'], data['phone']))
    conn.commit()
    return '', 201

@app.route('/suppliers/<int:id>', methods=['GET'])
def get_supplier(id):
    cur.execute('SELECT * FROM suppliers WHERE id=%s', (id,))
    supplier = cur.fetchone()
    return jsonify(supplier)

@app.route('/suppliers/<int:id>', methods=['PUT'])
def update_supplier(id):
    data = request.get_json()
    cur.execute('UPDATE suppliers SET name=%s, email=%s, phone=%s WHERE id=%s',
                (data['name'], data['email'], data['phone'], id))
    conn.commit()
    return '', 204

@app.route('/suppliers/<int:id>', methods=['DELETE'])
def delete_supplier(id):
    cur.execute('DELETE FROM suppliers WHERE id=%s', (id,))
    conn.commit()
    return '', 204

# routes for products
@app.route('/products', methods=['GET'])
def get_products():
    cur.execute('SELECT * FROM products')
    products = cur.fetchall()
    return jsonify(products)

@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    cur.execute('INSERT INTO products (name, price, supplier_id) VALUES (%s, %s, %s)',
                (data['name'], data['price'], data['supplier_id']))
    conn.commit()
    return '', 201

@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    cur.execute('SELECT * FROM products WHERE id=%s', (id,))
    product = cur.fetchone()
    return jsonify(product)

@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.get_json()
    cur.execute('UPDATE products SET name=%s, price=%s, supplier_id=%s WHERE id=%s',
                (data['name'], data['price'], data['supplier_id'], id))
    conn.commit()
    return '', 204

@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    cur.execute('DELETE FROM products WHERE id=%s', (id,))
    conn.commit()
    return '', 204
@app.route('/')
def home():
    return 'Hello, world!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
