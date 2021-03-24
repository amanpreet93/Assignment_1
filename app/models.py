from app import db
from datetime import datetime

 
class user_age_groups(db.Model): 
    user_id = db.Column(db.Integer, primary_key=True)
    age_group_id  = db.Column(db.Integer)
    
    def __init__(self, age_group_id =None):
        self.age_group_id = age_group_id
        

class user_topics(db.Model): 
    user_id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer)

    def __init__(self, topic_id =None):
        self.topic_id = topic_id

class content_age_groups(db.Model): 
    item_id  = db.Column(db.Integer, primary_key=True)
    age_group_id = db.Column(db.Integer)

    def __init__(self, age_group_id= None):
        self.age_group_id = age_group_id


class content_topics(db.Model): 
    item_id  = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer)

    def __init__(self, topic_id =None):
        self.topic_id = topic_id


class content_date (db.Model): 
    item_id = db.Column(db.Integer, primary_key=True)
    cdate = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    
    def __init__(self, cdate =None):
        self.cdate= datetime.datetime.now()

class visitor_data(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    item_id = db.Column(db.Integer)
    visit_count = db.Column(db.Integer,default= 0 )
    

    def __init__(self, item_id =None, user_id =None, visit_count = None ):
        self.user_id = user_id
        self.item_id = item_id
        self.visit_count = visit_count
