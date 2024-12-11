from flask import Flask
from flask_graphql import GraphQLView
from schema import schema

app = Flask(__name__)

# Add GraphQL endpoint
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # Enable GraphiQL interface
    )
)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
