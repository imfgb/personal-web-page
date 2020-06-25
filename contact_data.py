from google.cloud import ndb

class Contact(ndb.Model):
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    phone = ndb.StringProperty()
    message = ndb.StringProperty()
