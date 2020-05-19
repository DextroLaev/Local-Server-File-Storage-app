from flask import Flask,render_template,redirect,request,send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_ngrok import run_with_ngrok
import pymysql
from werkzeug.utils import secure_filename
import os
import requests

app = Flask(__name__)

app.secret_key = 'super-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/DATA'

# The below line is the path where u want to save your uploaded files, try to use your one
app.config['UPLOAD_FOLDER'] = '/home/dextrolaev/Desktop/SERVER/static'
db = SQLAlchemy(app)

class Files(db.Model):
    sno = db.Column(db.Integer,primary_key = True)
    data = db.Column(db.String(50),nullable=True)

@app.route('/',methods=['GET','POST'])
def home():
    files = Files.query.filter_by().all()         
    return render_template('index.html',files=files)
    
@app.route('/add',methods=['GET','POST'])    
def add():
    if request.method=='POST':
        return render_template('add.html')

@app.route('/add-post',methods=['GET','POST'])
def addPost():
    if (request.method == 'POST'):
        file = request.files['file']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))    
        data = file.filename
        # if len(Files.query.all())==0:        
        #     files = Files(sno=1,data=data)
        # else:
        files = Files(data=data)    
        db.session.add(files)
        db.session.commit()
        return redirect('/')

@app.route('/delete/<string:sno>')
def delete(sno):
    file = Files.query.filter_by(sno=sno).first()
    os.remove(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(file.data)))
    db.session.delete(file)    
    db.session.commit()
    return redirect('/')

@app.route('/edit/<string:sno>',methods=['GET','POST'])
def edit(sno):
    fileData = Files.query.filter_by(sno=sno).first()
    if request.method=='POST':
        newFileName = request.form.get('file')                                
        os.rename(os.path.join(app.config['UPLOAD_FOLDER'],fileData.data),os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(newFileName)))
        fileData.data = newFileName
        db.session.commit()
        return redirect('/')
    else:
        return render_template('edit.html',files=fileData)    

@app.route('/downloads/<path:data>')
def download_file(data):
    return send_from_directory(app.config['UPLOAD_FOLDER'],data,as_attachment=True)	    

    #with open(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(fileData.data)),'rb') as d:
     #   fileContent = d.read()

    #downlaodFolder = os.path.join(os.path.expanduser('~'),'Downloads/')
    
    #print(downlaodFolder+fileData.data)
   # with open(downlaodFolder+fileData.data,'wb') as data:
    #    data.write(fileContent)       

    

if __name__=='__main__':
    app.run(host = '192.168.43.155')    
