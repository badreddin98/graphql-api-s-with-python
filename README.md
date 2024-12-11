# Bakery Inventory Management GraphQL API

This project implements a GraphQL API for managing bakery inventory, allowing users to perform CRUD operations on bakery products.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Access GraphiQL interface at: http://localhost:5000/graphql

## Example Queries

### Query all products
```graphql
query {
  products {
    id
    name
    price
    quantity
    category
  }
}
```

### Create a new product
```graphql
mutation {
  createProduct(
    name: "Chocolate Croissant"
    price: 3.99
    quantity: 50
    category: "Pastries"
  ) {
    product {
      id
      name
      price
      quantity
      category
    }
  }
}
```

### Update a product
```graphql
mutation {
  updateProduct(
    id: "1"
    price: 4.99
    quantity: 45
  ) {
    product {
      id
      name
      price
      quantity
      category
    }
  }
}
```

### Delete a product
```graphql
mutation {
  deleteProduct(id: "1") {
    success
  }
}
```
