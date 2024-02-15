from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/path/to/your/python/script.py', methods=['POST'])
def process_selected_genres():
    data = request.get_json()
    selected_genres = data.get('selectedGenres', [])
    uppercase_genres = [genre.upper() for genre in selected_genres]
    return jsonify(uppercase_genres)

if __name__ == '__main__':
    app.run(debug=True)
