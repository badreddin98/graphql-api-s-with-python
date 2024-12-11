import graphene

# Store our bakery products in memory
bakery_products = []

class Product(graphene.ObjectType):
    """A bakery product"""
    id = graphene.ID(required=True)
    name = graphene.String(required=True)
    price = graphene.Float(required=True)
    quantity = graphene.Int(required=True)
    category = graphene.String(required=True)

class CreateProduct(graphene.Mutation):
    """Mutation to create a new bakery product"""
    class Arguments:
        name = graphene.String(required=True)
        price = graphene.Float(required=True)
        quantity = graphene.Int(required=True)
        category = graphene.String(required=True)

    product = graphene.Field(lambda: Product)

    def mutate(self, info, name, price, quantity, category):
        product_id = str(len(bakery_products) + 1)
        product = Product(
            id=product_id,
            name=name,
            price=price,
            quantity=quantity,
            category=category
        )
        bakery_products.append(product)
        return CreateProduct(product=product)

class UpdateProduct(graphene.Mutation):
    """Mutation to update an existing bakery product"""
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        price = graphene.Float()
        quantity = graphene.Int()
        category = graphene.String()

    product = graphene.Field(lambda: Product)

    def mutate(self, info, id, **kwargs):
        product = next((p for p in bakery_products if p.id == id), None)
        if not product:
            raise Exception('Product not found')

        for key, value in kwargs.items():
            if value is not None:
                setattr(product, key, value)

        return UpdateProduct(product=product)

class DeleteProduct(graphene.Mutation):
    """Mutation to delete a bakery product"""
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        global bakery_products
        product = next((p for p in bakery_products if p.id == id), None)
        if not product:
            raise Exception('Product not found')
        
        bakery_products = [p for p in bakery_products if p.id != id]
        return DeleteProduct(success=True)

class Query(graphene.ObjectType):
    """Query type for bakery products"""
    products = graphene.List(Product, description="List all bakery products")
    product = graphene.Field(
        Product,
        id=graphene.ID(required=True),
        description="Get a specific bakery product by ID"
    )

    def resolve_products(self, info):
        return bakery_products

    def resolve_product(self, info, id):
        return next((p for p in bakery_products if p.id == id), None)

class Mutation(graphene.ObjectType):
    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()
    delete_product = DeleteProduct.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
