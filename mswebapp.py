
import joblib
import pickle
from flask import Flask, request, jsonify, render_template

app = Flask(__name__, template_folder='hmtl_documents')


@app.route('/', methods=['GET', 'POST'])

@app.route('/redis', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        data = request.data
    return render_template('redis.html', url1=data)

if __name__ == '__main__':
    app.run(debug=True)
