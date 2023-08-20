from flask import Flask,request,jsonify
from flask_restx import Resource
from sqlalchemy import func
from newsfeed import db
from newsfeed import api
import boto3
import datetime

from newsfeed.models.post import * 
from newsfeed.models.community import *
#this class is for adding image for new post into database

class Add_image(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def post(self,post_id):

        try:

            post = PostModel.query.get(post_id)
            image_file = request.files['image_file']

            ACCESS_KEY = 'AKIAZJUKI6FIXTQLUVHD'
            SECRET_KEY = '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'
            BUCKET_NAME = 'beyond-the-seas-storage'

            s3_client = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

            image_file = request.files['image_file']
            filename = str(post_id) + "." + image_file.filename.split('.')[-1]  # e.g., "uniquefilename.jpg"
            s3_client.upload_fileobj(image_file, BUCKET_NAME, filename,ExtraArgs={'ACL': 'public-read'})
            url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{filename}"
           

            #insering the image url for the post into database
            post.post_image = url
            db.session.commit()
            
            return jsonify({'url': url})

        except Exception as e:
            print({"message":"exception occured in add_image"})
            print(e)
            return jsonify({"message":"exception occured in add_image"})

