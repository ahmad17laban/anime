from flask import Flask,render_template,request

app = Flask(__name__)
@app.route("/")
@app.route("/index.html")
@app.route("/index")
def home():
    return render_template('index.html', title = 'Home Page')
    
@app.route("/about_us.html")
@app.route("/about_us")
def about_us():
    return render_template('about_us.html', title = 'About Us')

@app.route("/contact_us.html")
@app.route("/contact_us")
def contact_us():
    return render_template('contact_us.html', title = 'Contact Us')

@app.route("/sign_up.html")
@app.route("/sign up")
def register():
    return render_template('sign_up.html', title = 'Sign Up')

@app.route("/users_reqin.html")
@app.route("/users")
def users():
    return render_template('users_reqin.html', title = 'users List')

@app.route('/airing.html')
@app.route('/airing')
def airing():
    return render_template('airing.html',title='Airing')


@app.route('/news.html')
@app.route('/news')
def news():
     return render_template('news.html',title='News' )


if __name__ == '__main__':
    app.run(debug=True)