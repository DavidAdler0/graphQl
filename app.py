from flask import Flask
from flask_graphql import  GraphQLView
from database import db_session, init_db, connection_url
from schema import schema
import psycopg2

app = Flask(__name__)
app.debug =True


# הכרת הdb לאפליקציה- app_context
# app.config["SQLALCHEMY_DATABASE_URI"] = connection_url
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# with app.app_context():
#     init_db()

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run(host='localhost', port=5001)