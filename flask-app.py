from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # return jsonify(data)
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('search')
    
    api_url = 'https://h9sw3948ci.execute-api.us-east-1.amazonaws.com/dev/search'
    # query_param = request.args.get('param_name', '')  # Replace 'param_name' with your desired query parameter name
    url_with_query = f'{api_url}?q={query}'

    response = requests.get(url_with_query)
    if response.status_code == 200:
        data = response.json()

    data= None
    # return jsonify(data)
    return render_template('index.html', song=data)

if __name__ == '__main__':
    app.run(debug=True)