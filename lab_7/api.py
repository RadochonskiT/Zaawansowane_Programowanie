from flask import Flask, request
from flask_restful import Resource, Api, reqparse, abort
from csv_handler import CsvHandler

app = Flask(__name__)
api = Api(app)

class GetMovies(Resource):
    def get(self):
        movies = CsvHandler.getJson('Movie')
        return movies

class GetLinks(Resource):
    def get(self):
        links = CsvHandler.getJson('Link')
        return links

class GetRatings(Resource):
    def get(self):
        ratings = CsvHandler.getJson('Rating')
        return ratings

class GetTags(Resource):
    def get(self):
        tags = CsvHandler.getJson('Tag')
        return tags

api.add_resource(GetMovies, '/movies')
api.add_resource(GetLinks, '/links')
api.add_resource(GetRatings, '/ratings')
api.add_resource(GetTags, '/tags')

if __name__ == '__main__':
    app.run(debug=True)