from app import db
from app import app
from flask import Flask, render_template , request
from  app.models import content_date, user_age_groups , content_topics, visitor_data,content_age_groups, user_topics
from flask import current_app, flash, jsonify, make_response, redirect, request, url_for
#from .models import db




@app.route('/')
def new_student():
   return render_template('public/login.html')


@app.route('/visitor_count', methods=["GET","POST"])
def visitor_page():
    user_id = request.form.get("user_id")
    item_id = request.form.get("item_id")
    #user_id = request.args.get('user_id')
    print("here")
    print(type(user_id))
    print(item_id)

    admin_role1 = db.session.query(user_age_groups ).filter_by(user_id = user_id).first()
    admin_role2 = db.session.query(content_topics ).filter_by(item_id = item_id).first()
    if admin_role1 and admin_role2:
        admin_role1 = db.session.query(user_age_groups ).filter_by(user_id = user_id).first()
        admin_role2 = db.session.query(content_topics ).filter_by(item_id = item_id).first()
        print(admin_role1.age_group_id)
        print(admin_role2.topic_id)
        print(admin_role2.item_id)
        print(type(admin_role1.user_id))

        if admin_role1.user_id ==int(user_id) and admin_role2.item_id ==int(item_id)  :
            print ("in count")
            v = db.session.query(visitor_data).filter_by(user_id = user_id).first()
            if not v:
                me = visitor_data(user_id =admin_role1.user_id ,item_id = admin_role2.item_id, visit_count = 1 )
                db.session.add(me)
                db.session.commit()
            else:
                print(v.visit_count)    
                me = visitor_data(user_id =admin_role1.user_id ,item_id = admin_role2.item_id,visit_count = 1 )
                v.visit_count += 1
                db.session.add(v)
                db.session.commit()
            

        rows = visitor_data.query.all()
        return render_template("public/list.html",rows = rows) 
    else:
            return make_response(jsonify({'error': 'No ID matched'}), 404)
        
@app.route('/content_ids', methods=["GET","POST"])
def content_ids():
    return render_template('public/content.html')

@app.route('/whole_content', methods=["GET","POST"])
def whole_content():
    user_id = request.form.get("user_id")
    AGID =  db.session.query(user_age_groups).filter_by(user_id = user_id).first()
    if AGID:
        AGID = db.session.query(user_age_groups).filter_by(user_id = user_id).first().age_group_id
        ITID = db.session.query(content_age_groups).filter_by(age_group_id  = AGID).first().item_id
        TID = db.session.query(user_topics).filter_by(user_id = user_id).first().topic_id
        CD = db.session.query(content_date).filter_by(item_id  = ITID ).first().cdate
        print(AGID)
        print(ITID)
        print(TID)
        print(CD)
        return render_template("public/content_disp.html",AGID = AGID,ITID = ITID, TID = TID, CD = CD, user_id = user_id) 
    else:
        return "wrong userID"
    

    
   

    
         