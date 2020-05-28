from main import app
from models import db

db.create_all(app=app)

print('database initialized!')

bob = User(username="bob", email="bob@mail.com") 
bob.set_password("bobpass")
john = User(username="susan", email="susan@mail.com")
john.set_password('susanpass')
db.session.add(bob)
db.session.add(john)
db.session.commit()
