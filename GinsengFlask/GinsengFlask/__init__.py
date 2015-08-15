from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
	title = "HOLY JESUS LORD"
	paragraph = "akjhsdfkjasdlkjfbawklalaaaaaaaalaaaaaaaaaaaaaaaaaaaaaaaaallalalal klalaaaaaaaalaaaaaklalaaaaaaaalaaaaaklalaaaaaaaalaaaaaklalaaaaaaaalaaaaaklalaaaaaaaalaaaaaklalaaaaaaaalaaaaaklalaaaaaaaalaaaaaklalaaaaaaaalaaaaaa"
	
	return render_template("index.html", title = title, paragraph = paragraph)
	
@app.route('/about')
def aboutpage():
    return render_template("index.html",title = "Information about this Site" , paragraph = "8554435484851321321321 blah blah")


@app.route('/contact')
def contactpage():
	return "This is Contact Page"



if __name__ == "__main__":
    app.run()

