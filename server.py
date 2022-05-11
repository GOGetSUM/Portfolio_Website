from flask import Flask, render_template, redirect, url_for, request


#~~~~~~~~~~~~~~~~~~~~~create flask app~~~~~~~~~~~~~~~~~

app = Flask(__name__)


# Home _ Index ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/',methods=["GET", "POST"])
def home():
    return render_template('index.html')

# text to morse _ Index ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/text2mrs',methods=["GET", "POST"])
def text2mrse():
    return render_template('t2m.html')

# tic tac toe _ Index ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/tictactoe',methods=["GET", "POST"])
def tictactoe():
    return render_template('tictactoe.html')

# watermark _ Index ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/watermark',methods=["GET", "POST"])
def watermark():
    return render_template('watermark.html')

# typing speed _ Index ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/typingspeed',methods=["GET", "POST"])
def typingspeed():
    return render_template('typingspeed.html')

# writers block _ Index ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/writersblock',methods=["GET", "POST"])
def writersblock():
    return render_template('writersblock.html')


#--------run app------------------------
if __name__=='__main__':
    app.run(debug=True)