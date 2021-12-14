from flask import render_template, request, redirect, url_for, abort, session
from server import app
from src.main import Main
from src.wrap import Wrap
from server import system
'''
Main Page
'''

@app.route('/',methods=["GET","POST"])
def home():
    print(len(system.mains))
    return render_template('home.html',system = system) 

@app.route('/mains',methods=["GET","POST"])
def Mains():
    if request.method == 'POST':
        if "order" in request.form:
            return render_template("burger.html")

    return render_template('Mains.html')

@app.route('/mains/burger',methods=["GET","POST"])
def burger():
    if request.method == 'POST':
        
        # qty = int(request.form['qty'])
        if request.form['qty']:
            qty = int(request.form['qty'])
        else:
            qty = 0
        
        if request.form['qty1']:
            qty1 = int(request.form['qty1'])
        else:
            qty1 = 0

        if request.form['qty2']:
            qty2 = int(request.form['qty2'])
        else:
            qty2 = 0
        

        if request.form['qty3']:
            qty3 = int(request.form['qty3'])
        else:
            qty3 = 0
        
        if request.form['qty4']:
            qty4 = int(request.form['qty4'])
        else:
            qty4 = 0

        if request.form['qty5']:
            qty5 = int(request.form['qty5'])
        else:
            qty5 = 0

        if request.form['qty6']:
            qty6 = int(request.form['qty6'])
        else:
            qty6 = 0

        if request.form['qty7']:
            qty7 = int(request.form['qty7'])
        else:
            qty7 = 0

        

        # for i in request.form:
        #     print (i)
        # print('qty1')

        main = Main('seasame',qty,'muffin', qty1,'chicken',qty2,'beef',qty3,'vegeterian',qty4,'tomato', qty5,'lettuce',qty6,'cheese',qty7)
        system.add_mains(main)
        return render_template('order.html', system = system, main=main, tp = 'burger')
    return render_template('burger.html')



@app.route('/mains/wrap',methods=["GET","POST"])
def wrap():
    if request.method == 'POST':
        
        # qty = int(request.form['qty'])
        if request.form['qty']:
            qty = int(request.form['qty'])
        else:
            qty = 0
        
        if request.form['qty1']:
            qty1 = int(request.form['qty1'])
        else:
            qty1 = 0

        if request.form['qty2']:
            qty2 = int(request.form['qty2'])
        else:
            qty2 = 0
        

        if request.form['qty3']:
            qty3 = int(request.form['qty3'])
        else:
            qty3 = 0
        
        if request.form['qty4']:
            qty4 = int(request.form['qty4'])
        else:
            qty4 = 0

        if request.form['qty5']:
            qty5 = int(request.form['qty5'])
        else:
            qty5 = 0

        if request.form['qty6']:
            qty6 = int(request.form['qty6'])
        else:
            qty6 = 0

        if request.form['qty7']:
            qty7 = int(request.form['qty7'])
        else:
            qty7 = 0

        

        # for i in request.form:
        #     print (i)
        # print('qty1')

        main = Wrap('wheat',qty,'fry', qty1,'chicken',qty2,'beef',qty3,'vegeterian',qty4,'tomato', qty5,'lettuce',qty6,'cheese',qty7)
        system.add_mains(main)
        return render_template('order.html', system = system, main=main, tp = 'Wrap')
    return render_template('Wrap.html')

@app.route('/order',methods=["GET","POST"])
def Order():

    return render_template('order.html')
