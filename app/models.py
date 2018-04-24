from . import mongo_db
from mongoengine.queryset import queryset_manager


class Post(mongo_db.Document):
    _id = mongo_db.ObjectIdField(required=True)
    topic = mongo_db.StringField()
    title = mongo_db.StringField(max_length=255, required=True)
    media = mongo_db.StringField()
    content = mongo_db.StringField(required=True)
    published_at = mongo_db.DateTimeField()
    created_time = mongo_db.DateTimeField()
    image_urls = mongo_db.ListField(mongo_db.StringField())
    keywords = mongo_db.ListField(mongo_db.StringField())
    id = mongo_db.StringField(required=True)

    url = mongo_db.StringField()
    categories = mongo_db.IntField()
    origin_content = mongo_db.StringField(required=True)
    meta = {'collection': 'test_news'}

    @queryset_manager
    def objects(cls, queryset):
        return queryset.order_by("-published_at")

    def __unicode__(self):
        return self.title

    def __repr__(self):
        return '<Post %r>' % self.title
