"""Seed file to make sample data for db."""
from models import User, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add sample data
user1 = User(username='user1', password='password1')
user2 = User(username='user2', password='password2')
user3 = User(username='user3', password='password3')


db.session.add_all([user1, user2, user3])

db.session.commit()
