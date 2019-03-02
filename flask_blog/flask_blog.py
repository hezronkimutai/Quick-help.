from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author':'corey schafer',
        'title':'Blog post 1',
        'content':'First post content',
        'date_posted':'April 20, 2018'

    },
    {
        'author':'John Doe',
        'title':'Blog post 2',
        'content':'Second  post content',
        'date_posted':'April 22, 2018'

    },
]

@app.route("/")
def hello():
    return render_template("home.html", posts=posts)

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html" ,title='about')

if __name__ == '__main__':
    app.run(debug=True)
