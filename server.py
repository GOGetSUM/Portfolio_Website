from flask import Flask, render_template, redirect, url_for, request


#~~~~~~~~~~~~~~~~~~~~~create flask app~~~~~~~~~~~~~~~~~

app = Flask(__name__)


# Home _ Index ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/')
def home():
    return render_template('index.html')

# text to morse _ Index ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/text2mrs')
def text2mrse():
    return render_template('t2m.html')

# tic tac toe _ Index ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/tictactoe')
def tictactoe():
    return render_template('tictactoe.html')

# watermark _ Index ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/watermark')
def watermark():
    return render_template('watermark.html')

# typing speed _ Index ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/typingspeed')
def typingspeed():
    return render_template('typingspeed.html')

# writers block _ Index ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/writersblock')
def writersblock():
    return render_template('writersblock.html')

# TodoTaskTracker_ Index ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/tasktracker')
def tasktracker():
    return render_template('tasktracker.html')

# colourpallette_ Index ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/colourpallette')
def colourpallette():
    return render_template('colourpallette.html')

# onlineshop_ Index ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/onlineshop')
def onlineshop():
    return render_template('onlineshop.html')

# PDF to Audio_ Index ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/pdftoaudio')
def pdftoaudio():
    return render_template('pdftoaudio.html')

# Web Scraper_ Index ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/wscrapper')
def wscrapper():
    return render_template('webscrapper.html')


#--------run app------------------------
if __name__=='__main__':
    app.run(debug=True)