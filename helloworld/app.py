from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world(
):
    return "Hello world!"


@app.route('/about')
def welcome():
    return "Welcome to my Flask site, ©2018"


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    fulfillmentText = ''
    sum = 0
    query_result = req.get('queryResult')
    if query_result.get('action') == 'add.numbers':
        num1 = int(query_result.get('parameters').get('number'))
        num2 = int(query_result.get('parameters').get('number1'))
        sum = str(num1 + num2)
        print('here num1 = {0}'.format(num1))
        print('here num2 = {0}'.format(num2))
        fulfillmentText = 'The sum of the two numbers is ' + sum
    elif query_result.get('action') == 'multiply.numbers':
        num1 = int(query_result.get('parameters').get('number'))
        num2 = int(query_result.get('parameters').get('number1'))
        product = str(num1 * num2)
        print('here num1 = {0}'.format(num1))
        print('here num2 = {0}'.format(num2))
        fulfillmentText = 'The product of the two numbers is ' + product
    return {"fulfillmentText": fulfillmentText, "source": "webhookdata"}