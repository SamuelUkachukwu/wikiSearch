# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Use a breakpoint in the code line below to debug your script.
# Press F9 to toggle the breakpoint.
# Press the green button in the gutter to run the script.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from flask import Flask, render_template, request, url_for, flash
from werkzeug.utils import redirect
app = Flask(__name__)
app.config['ENV'] = "Development"
app.config['DEBUG'] = True
# @app.route('/')
# def hello_world():
#     return 'hello test'
@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        query = request.form['query']
        result = "I have no clue"
    return render_template("index.html", result=result)

if __name__ == '__main__':
    app.run()