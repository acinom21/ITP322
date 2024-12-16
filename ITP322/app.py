from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

API_KEY = 'kwye9X7Be8RXnDaB160ZNw==z51fojYHh39mdpxz'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    brand = request.args.get('brand')
    if not brand:
        return jsonify({'error': 'Brand is required'}), 400
    
    try:
        
        url = f'https://api.api-ninjas.com/v1/motorcycles?make={brand}'
        headers = {'X-Api-Key': API_KEY}
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            return jsonify({'error': 'Failed to fetch data'}), 500
        
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
