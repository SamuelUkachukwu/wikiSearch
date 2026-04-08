# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Use a breakpoint in the code line below to debug your script.
# Press F9 to toggle the breakpoint.
# Press the green button in the gutter to run the script.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from flask import Flask, render_template, request
from run_wiki_on_ec2 import run_wiki_on_ec2
from database import check_cache, save_cache
app = Flask(__name__)
app.config['ENV'] = "Development"
app.config['DEBUG'] = True
# @app.route('/')
# def hello_world():
#     return 'hello test'
@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    query = None
    if request.method == 'POST':
        query = request.form['query'].strip()
        if not query:
            return render_template("index.html", result="Please enter a search term.")

        cached_result = check_cache(query)
        if cached_result:
            result = cached_result
        else:
            result = run_wiki_on_ec2(query)
            save_cache(query, result)
    return render_template("index.html", result=result, query=query)

if __name__ == '__main__':
    # app.run()
    app.run(host="0.0.0.0", port=8888)