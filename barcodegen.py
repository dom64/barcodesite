from io import BytesIO
from barcode import Code128
from barcode.writer import SVGWriter
import re


def barcodeGen(UPC):
    UPC = str(re.sub("[^0-9]", "", UPC))
    if UPC == "":
        real = "Error"
        return real
    if len(UPC) == 14 and UPC[:2] == "00":
        UPC = UPC[:-1] # This whole check is to lazily fix the UPC from the site automatically
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