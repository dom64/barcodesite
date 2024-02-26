from flask import Flask, render_template, request
from barcodegen import barcodeGen

app = Flask(__name__)
app.debug = True

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def process():
    UPC = request.form['UPC']
    barcodeNumber = barcodeGen(UPC)
    return render_template("index.html", barcode=barcodeNumber)

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)