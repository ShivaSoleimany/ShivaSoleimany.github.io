from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/path/to/your/python/script.py', methods=['POST'])
def process_selected_genres():
    selected_genres = request.form.get('selectedGenres').split(",")
    # Do whatever you need to do with the selected genres
    return "Selected genres: " + ", ".join(selected_genres)

if __name__ == '__main__':
    app.run(debug=True)
