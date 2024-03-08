from flask import Flask

app = Flask(__name__)

@app.route('/add/<num1>/<num2>')
def add_nums(num1,num2):
    return f'<h1>Sum of {num1} and {num2} equals {str(int(num1) + int(num2))}</h1>'

@app.route('/sub/<num1>/<num2>')
def sub_nums(num1,num2):
    return f'<h1>Difference of {num1} and {num2} equals {str(int(num1) - int(num2))}</h1>'

@app.route('/mult/<num1>/<num2>')
def mult_nums(num1,num2):
    return f'<h1>Product of {num1} and {num2} equals {str(int(num1) * int(num2))}</h1>'

@app.route('/div/<num1>/<num2>')
def div_nums(num1,num2):
    return f'<h1>Quotient of {num1} and {num2} equals {str(int(num1) / int(num2))}</h1>' 
        
       
