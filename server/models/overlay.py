from mongoengine import Document, StringField, IntField

class Overlay(Document):
    name = StringField(required=True)
    content = StringField(required=True)
    position = StringField(required=True)
    size = StringField(required=True)