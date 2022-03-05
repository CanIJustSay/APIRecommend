from flask import Flask, jsonify, request
import csv

app = Flask(__name__)

with open('movies.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)
    allMovies = data[1:]

likeMovies = []
dislikeMovies = []
notWatched = []


@app.route('/getMovies')
def GetAllMovies():
    return jsonify({
        'data': allMovies[0],
        'status': 'Success'
    })


@app.route('/dislikeMovies', methods=['POST'])
def dislikedMovies():
    movie = allMovies[0]
    allMovies = allMovies[1:]
    dislikeMovies.append(movie)
    return jsonify({
        'data': movie,
        'status': 'Success'
    })


if(__name__ == '__main__'):
    app.run(debug=True)
