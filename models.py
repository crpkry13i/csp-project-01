from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()


def connect_db(app):
    db.app = app
    db.init_app(app)

# MODELS GO BELOW!


class User(db.Model):
    """User in the system."""

    __tablename__ = "users"

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    username = db.Column(
        db.Text,
        nullable=False,
        unique=True,
    )

    password = db.Column(
        db.Text,
        nullable=False,
    )

    def __repr__(self):
        return f"<User #{self.id}: {self.username}>"

    @classmethod
    def register(cls, username, password):
        """Register user. Hashes password and adds user to system."""

        # Hashed password. Turn bytestring into normal (unicode utf8) string
        hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')

        # return instance of user with username and hashed password
        return cls(username=username, password=hashed_pwd)
    # end register

    @classmethod
    def authenticate(cls, username, password):
        """Find user with `username` and `password`.

        This is a class method (call it on the class, not an individual user.)
        It searches for a user whose password hash matches this password
        and, if it finds such a user, returns that user instance.

        If can't find matching user (or if password is wrong), returns False.
        """

        user = cls.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            # return user instance
            return user
        else:
            return False

# class Album(db.Model):
#     """Albums Model"""

#     __tablename__ = "albums"

#     id = db.Column(db.Text, primary_key=True)
#     name = db.Column(db.Text)
#     release_date = db.Column(db.Text)
#     image = db.Column(db.Text)
#     link = db.Column(db.Text)
