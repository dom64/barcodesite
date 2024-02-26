from io import BytesIO
from barcode import Code128
from barcode.writer import SVGWriter
import re


def barcodeGen(UPC):
    UPC = str(re.sub("[^0-9]", "", UPC))
    if UPC == "":
        real = "Error"
        return real
    barcodeMem = BytesIO()
    options = {
        'module_width': 0.7,
        'module_height': 25.0,
        'font_size': 14,
    }
    Code128(UPC, writer=SVGWriter()).write(barcodeMem, options)
    barcodeMem.seek(0)
    real = barcodeMem.read().decode()
    barcodeMem.close()
    return real