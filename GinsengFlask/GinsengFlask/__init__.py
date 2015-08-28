from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

@app.route('/')
def homepage():
	title = "HOLY JESUS LORD"
	paragraph = "akjhsdfkjasdlkjfbawklalaaaaaaaalaaaaaaaaaaaaaaaaaaaaaaaaallalalal klalaaaaaaaalaaaaaklalaaaaaaaalaaaaaklalaaaaaaaalaaaaaklalaaaaaaaalaaaaaklalaaaaaaaalaaaaaklalaaaaaaaalaaaaaklalaaaaaaaalaaaaaklalaaaaaaaalaaaaaa"
	
	return render_template("index.html", title = title, paragraph = paragraph)
	
@app.route('/about')
def aboutpage():
	pageType = 'about'
	return render_template("index.html",pageType = pageType, title = "Information about this Site" , paragraph = "8554435484851321321321 blah blah")


@app.route('/contact')
def contactpage():
	return render_template("contactpage.html")


@app.route('/ginseng')
def ginsengpage():
	return render_template("productpage.html")

@app.route('/testpage')
def testpage():
	return render_template("/Trials/fullpagescroll.html")


if __name__ == "__main__":
	app.run()

