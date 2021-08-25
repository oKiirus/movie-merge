from flask import Flask, jsonify
import csv


f = open('movies.csv', encoding="utf8")
file = csv.reader(f)
data = list(file)

headers = data[0]
movies = data[1:]
app = Flask(__name__)

@app.route('/getMovies')
def allMovies():
    return jsonify({
        'data' : movies,
        'status' : 'success'
    })

if __name__ == '__main__':
    app.run() 