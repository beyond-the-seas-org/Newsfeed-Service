from flask import request,jsonify
from flask_restful import Resource
from sqlalchemy import func
from app import db

import sys
# append the path of both the
# parent and grandparent directory
sys.path.append("....")
sys.path.append("..")


from Database_Service.models.student import *


#this class is for adding a student obejct(i.e adding a row) in "student table"

class Create_profile(Resource):
    def post(self):
        new_student = StudentModel()

        #for getting the next "id" for next entry of the "post" table
        max_id = db.session.query(func.max(StudentModel.id)).scalar()
        if (max_id == 'None'):
            max_id = 1
        else:
            max_id = max_id + 1

        new_student.id = max_id
        new_student.username = request.json['username']
        new_student.first_name= request.json['first_name']
        new_student.last_name = request.json['last_name']
        new_student.primary_email = request.json['primary_email']
        new_student.gender = request.json['gender']
        new_student.age = request.json['age']
        new_student.secondary_email = request.json['secondary_email']
        new_student.bsc_year_of_passing  = request.json['bsc_year_of_passing']
        new_student.ms_year_of_passing = request.json['ms_year_of_passing']
        new_student.bsc_cgpa = request.json['bsc_cgpa']
        new_student.ms_cgpa = request.json['bsc_cgpa']
        new_student.bsc_university = request.json['bsc_university']
        new_student.ms_university = request.json['ms_university']
        new_student.github_link = request.json['github_link']
        new_student.linkedin_link = request.json['linkedin_link']
        new_student.current_address = request.json['current_address']
        new_student.website_link = request.json['website_link']
        new_student.gre_verbal_quant_score = request.json['gre_verbal_quant_score']
        new_student.gre_awa_score = request.json['gre_awa_score']
        new_student.toefl_score = request.json['toefl_score']
        new_student.ielts_score = request.json['ielts_score']


        db.session.add(new_student)
        db.session.commit()

        #print(new_student.json())
        return jsonify(new_student.json())