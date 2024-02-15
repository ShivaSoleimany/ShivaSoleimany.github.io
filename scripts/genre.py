from flask import Flask, request, jsonify

print("hii")
app = Flask(__name__)

@app.route('/Users/shiva/Desktop/Courses/website/shbaranbahar.github.io/scripts/genre.py', methods=['POST'])
def process_selected_genres():
    data = request.get_json()
    selected_genres = data.get('selectedGenres', [])
    print("Received selected genres:", selected_genres)  # Debugging print statement
    uppercase_genres = [genre.upper() for genre in selected_genres]
    print("Uppercase genres:", uppercase_genres)  # Debugging print statement
    return jsonify(uppercase_genres)

if __name__ == '__main__':
    app.run(debug=True)
    process_selected_genres()
