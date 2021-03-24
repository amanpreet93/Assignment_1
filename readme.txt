 commands to add data to following tables.
 from app.models import user_topics    
>>> me = user_topics(1111)                           
>>> db.session.add(me)  
>>> db.session.commit()

from app.models import user_age_groups 
>>> me = user_age_groups(111)
>>> db.session.add(me)
>>> db.session.commit()

#for default datetime addition in table
>>> from app.models import content_date      
>>> hh = content_date ()                  
>>> db.session.add(hh)  
>>> db.session.commit()

# to create tables
>>> from app import db
C:\MY\flask_tutorial\Assignment_1
>>> db.create_all()