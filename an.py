from flask import Flask, render_template,request,session, url_for,redirect
from flask_mail import Mail, Message
from waitress import serve
import secrets 
import os
secrets.token_hex(16)


app = Flask(__name__)
app.secret_key = 'fbd1_efad885bf@35e1d5ea08424xenel221'

@app.route("/")
@app.route("/index.html")
@app.route("/index")
def home():
    return render_template('index.html', title='Home Page')


@app.route("/about_us.html")
@app.route("/about_us")
def about_us():
    return render_template('about_us.html', title='About Us')



app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'ahmad18laban@gmail.com'
app.config['MAIL_PASSWORD'] = 'hpjnckmuoowfyypq'

mail = Mail(app)




@app.route("/contact_us.html",methods=["POST","GET"])
@app.route("/contact_us")
def contact_us():
    return render_template('contact_us.html')
    




@app.route('/handle_email',methods=['GET','POST'])
def handle_email():
    if request.method  =='POST':
        nam = request.form['name_us']
        email = request.form['email_us']
        texarea= request.form['textare_us']
        msg=Message('title',recipients=[email],sender='ahmad18laban@gmail.com')
        msg.body= texarea
        mail.send(msg)
        return redirect(url_for("home")) 








@app.route("/sign_up.html", methods=["POST","GET"])
@app.route("/sign up")
def register():
    # if session ['em'] != None:
    #     return render_template('index.html')

    return render_template('sign_up.html')
    


    
@app.route('/handle_data',methods=['POST','GET'])
def handle_data():
    session['signed_up']=None
    if request.method  =='POST' and session['signed_up']==None:
        session['signed_up']=None        
        em = request.form['email']
        pw = request.form['password']
        c_pw= request.form['confirm_password']
        session['em']=em
        session['pw']=pw
        session['signed_up']=True
        return render_template('index.html')
    # elif session['em']==em and session['pw']==pw :
    #     render_template('index.html',message=f"{em} is already registered {pw}",
    #     msg_class= "alert alert-success")
    else:
        return render_template('index.html')

@app.route("/users_reqin.html")
@app.route("/users")
def users():
    return render_template('users_reqin.html', title='users List')


@app.route('/airing.html')
@app.route('/airing')
def airing():
    return render_template('airing.html', title='airing')

@app.route('/news.html')
@app.route('/news')
def news():
    return render_template('news.html', title='News')

@app.route('/pop/')
def pop():
    em=session.pop('current_user')
    return f"{em} is removed"






if __name__ == '__main__':
    app.run(debug=True)
    # p= os.environ.get('POST')
    # p='5000' if p == None else p
    # serve(app,host='0.0.0.0')

