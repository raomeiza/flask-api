from mongoengine import Document, StringField, BooleanField

class User(Document):
    username = StringField(required=True, unique=True)
    password = StringField(required=True)
    admin = BooleanField(default=False)
    role = StringField(default='user', choices=('user', 'admin', 'superadmin'))
