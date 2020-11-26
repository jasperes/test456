#!/usr/bin/python3

import os
import pymysql
from flask import Flask, render_template

MY_DB="mysql://sandy:secret@myhost1:1111/db"
API_PASSWORD="mycoolpassword"

# Adler32
MYCOOLSTRING1="21c8052b"
# CRC32
MYCOOLSTRING2="9becb175"
# Haval
MYCOOLSTRING3="a48675320d3e288be5eda8851dd03636"
# MD2
MYCOOLSTRING4="b99d80c3a62db2553d4c964aea901a89"
# MD4
MYCOOLSTRING5="ffa53b9f5b06c5329421eb7fc736814b"
# MD5
MYCOOLSTRING6="78fda569970677489ec37d3d030d70e2"
# RipeMD128
MYCOOLSTRING7="00d540afb305354f22f4dd80d1cb7d9e"
# RipeMD160
MYCOOLSTRING8="cae2756358e7a54ad616c0419b1381b967f754ce"
# SHA-1
MYCOOLSTRING9="b4bffc839ff08d478584e13dff75e68b64e42720"
# SHA-256
MYCOOLSTRING10="b575b55eb52371f61902c022d92c17a01b67be3ca8ff5cb51ba2bd908e0ced65"
# SHA-384
MYCOOLSTRING11="37fa5cbac1a69b6007413327415262782d194f7e1ed1a1649fdc3fb8d42372945595496e051fb379536cc38e364d5cfd"
# SHA-512
MYCOOLSTRING12="44656b7bd6910230b0f9c3e582bd25040d86e28784c3bee8da983dea40003e1b9c4f246466c2b6bf02ea8bed248d52547cea4bbafc7a61b6b5afd5b1bc854f5c"
# Tiger
MYCOOLSTRING13="b4dee91e420c89bd61544979b66762ec96681dd0def557ba"
# Whirlpool
MYCOOLSTRING14="083cfa8823dcdae0455c43aea03ad971f8fc79004c8efe90a0581fbe14e5cad10171134a8fd684c18dfc1b3fd5d8b9573c662574e3da7ab61e818236d0443cf7"

def run(name):
    db = pymysql.connect("localhost","root","root","mydb" )
    cur = db.cursor()
    cur.execute("SELECT * FROM USER WHERE NAME = '%s'" % name)
    db.close()

def eval_injection(a, b):
  return eval("%s + %s" % (a, b))

def exec_injection(a, b):
  return exec("%s + %s" % (a, b))

def generate_invoice_pdf(email, payment_data):
  os.system('my_pdf_tool %s %s' % (email, payment_data))  

@app.route('/<username>')
def home(username):
   return render_template('index.html', title='Home', user={'username': username})

if __name__ == '__main__':
   app.run()
