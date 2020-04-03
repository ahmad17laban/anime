from flask import Flask, render_template,request,session, url_for,redirect
from flask_mail import Mail, Message
from waitress import serve
import secrets 
import os
from data import storeData,readData
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
    getpost = readData('top.json')
    post=getpost['about']
    return render_template('about_us.html', title='About Us', post=post)


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
    


# for handle email (contact_us)
@app.route('/handle_email',methods=['GET','POST'])
def handle_email():
    nam = request.form['name_us']
    email = request.form['email_us']
    texarea= request.form['textarea_us']
    msg=Message(f"Message {email}",recipients=['ahmad18laban@gmail.com'],sender=email)
    msg.body= f''' {nam} said {texarea} '''
    mail.send(msg)
    return render_template('index.html',message= f"{nam} your email was sent ", msgstat=True) 




@app.route("/sign_up.html", methods=["POST","GET"])
@app.route("/sign up")
def register():
    if session.get('signed_up') == True:
        render_template('index.html' ,message=f"you are already registred", msgstat=True)
    return render_template('sign_up.html')
    


# for sign_up.html
@app.route('/handle_data',methods=['POST','GET'])
def handle_data():
    name_=request.form['name_']
    em = request.form['email']
    pw = request.form['password']
    c_pw= request.form['confirm_password']
    session['em']=em
    session['pw']=pw
    members = readData('data.json')
    if em in members:
        session['signed_up'] = True
        return render_template('index.html', 
        name_ = name_,
        pw = pw,
        em = em, 
        message=f"{name_} is already regestred {em}",msgstat=True)
    else:
        storeData(members, 'data.json', 'data','none', name_, pw, em)
        return render_template(
            'index.html',
            message=f"{name_} is registered using, {em}",
            msgstat=True)
    
    
    
    
    
    # if session['em']== em and session['pw'] == pw :
    #     session['signed_up']=True
    #     return render_template('index.html',message=f"{name_} you signed up using {em}",msgstat=True)

@app.route("/users_reqin.html")
@app.route("/users")
def users():
    return render_template('users_reqin.html', title='users List')


@app.route('/airing.html')
@app.route('/airing')
def airing():
    getpost = readData('top.json')
    post=getpost['airing']
    return render_template('airing.html', title='Top Airing',post=post)

@app.route("/trailers.html")
@app.route("/trailers")
def trailers():
    getpost = readData('top.json')
    post=getpost['trailers']
    return render_template('trailers.html', title='Top Trailers',post=post)





@app.route('/news.html')
@app.route('/news')
def news():
    return render_template('news.html', title='News')






@app.errorhandler(404)
def err_404(error):
   return render_template( '404.html' ), 404



@app.route('/pop/')
def pop():
    em=session.pop('em')
    # session.pop('signed_up')
    if not em :
        return  render_template('index.html',message=f" no one you signed out ",msgstat=True)

    else:
        return  render_template('index.html',message=f"{em} you signed out ",msgstat=True)

    


@app.route('/get/')
def get():
    c = session.get('em')
    if c:
        return f"{c} is signed up"
        
    return 'no one is signed up'




@app.route('/dtable.html')
def dtable():
    return render_template('dtable.html')


if __name__ == '__main__':
    # Debug Mode
    # app.run(debug=True)
    # production mode 
    p= os.environ.get('PORT')
    p='5000' if p == None else p
    serve(app,host='0.0.0.0', port=p)