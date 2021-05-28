from flask import Flask, request

from migration import get_sum

import logging

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    # handle the POST request
    if request.method == 'POST':
        name = request.form.get('name')
        amount = get_sum(name)
        return '''
                  <h3>Name : {}</h3>
                  <h3>Sum  : {}</h3>'''.format(name, amount)

    # otherwise handle the GET request
    return '''
           <form method="POST">
               <div><label>Name: <input type="text" name="name"></label></div>
               <input type="submit" value="Submit">
           </form>'''


if __name__ == '__main__':
    app.run(debug=True, port=5000)