import csv
import json
from Movie import Movie
from Link import Link
from Rating import Rating
from Tag import Tag

class CsvHandler:
    def getMovies() -> list:
        with open('movies.csv', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            movieList = []
            for row in csv_reader:
                movie = Movie(row[0], row[1], row[2])
                movieList.append(movie)

            return movieList

    def getLinks() -> list:
        with open('links.csv', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            linkList = []
            for row in csv_reader:
                link = Link(row[0], row[1], row[2])
                linkList.append(link)

            return linkList

    def getRatings() -> list:
        with open('ratings.csv', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            ratingList = []
            for row in csv_reader:
                rating = Rating(row[0], row[1], row[2], row[3])
                ratingList.append(rating)

            return ratingList

    def getTags() -> list:
        with open('tags.csv', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            tagList = []
            for row in csv_reader:
                tag = Tag(row[0], row[1], row[2], row[3])
                tagList.append(tag)

            return tagList

    def serialize(type: str) -> list:
        list_with_serialized_objects = []
        if (type == 'Movie'):
            movieList = CsvHandler.getMovies()
            for movie in movieList:
                list_with_serialized_objects.append(json.dumps(movie.__dict__))
        elif (type == 'Link'):
            linkList = CsvHandler.getLinks()
            for link in linkList:
                list_with_serialized_objects.append(json.dumps(link.__dict__))
        elif (type == 'Rating'):
            ratingList = CsvHandler.getRatings()
            for rating in ratingList:
                list_with_serialized_objects.append(json.dumps(rating.__dict__))
        elif (type == 'Tag'):
            tagList = CsvHandler.getTags()
            for tag in tagList:
                list_with_serialized_objects.append(json.dumps(tag.__dict__))

        return list_with_serialized_objects

    def getJson(type: str) -> str:
        return CsvHandler.serialize(type)
        

print(CsvHandler.getJson('Movie'))