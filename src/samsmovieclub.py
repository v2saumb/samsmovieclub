import fresh_tomatoes
import samsMovieLib
import csv
import sys

# file containing the media details
mediadetails = 'mediadb/mediadetails.csv'

# csv file containig reviews for media
media_reviews = 'mediadb/mediareviews.csv'

""" List of fielsd names to be read from the mediadetails csv
     The secquence of the fields in the csv should match the
     sequence of feilds specified below in media_field_names.
     if the sequence does not match it will render incorrect
     data in the html.
"""

media_field_names = ['id', 'type', 'title', 'duration', 'pg_rating',
                     'cast', 'poster_url', 'trailer_url',
                     'story_line', 'genres', 'director', 'year',
                     'episodes', 'seasons']

""" List of fielsd names to be read from the media_reviews csv
     The secquence of the fields in the csv should match the
     sequence of feilds specified below in media_field_names.
     if the sequence does not match it will render incorrect
     data in the html.
"""

media_review_fields = ['media_id', 'user_name', 'review', 'rating']

# initializing containers
movies_list = []  # List of movies
shows_list = []  # List of tv shows
all_reviews = []  # List of all reviews


def read_media_csv():
    """
    read_media_csv() reads the csv file specified in mediadetails
    and for each row read it will call either the createandaddmovie
    or the createandaddshow functions based on the media type. The
    function reads the column names specified media_review_fields
    Arguments:
        None
    Returns:
        None
    """
    print ("Reading media details.")
    with open(mediadetails, 'rb') as media_file:
        media_reader = csv.DictReader(
            media_file, fieldnames=media_field_names, restval="")
        try:
            for row in media_reader:
                print ". "
                if row['type'] == 'MOVIE':  # check if the row is a movie
                    createandaddmovie(row)
                else:
                    createandaddshow(row)
        except csv.Error as e:
            # On Error:- raise error and exit
            sys.exit('file %s, line %d: %s' %
                     (mediadetails, media_reader.line_num, e))
    print "... done reading media details."


def read_reviews_csv():
    """
    read_reviews_csv() reads the csv file specified in media_reviews
    For each row read, create a object and will use the fields
    specified in media_review_fields, and then adds the object to the
    all_reviews.
    Arguments:
        None
    Returns:
        None
    """
    print ("Reading reviews.")
    with open(media_reviews, 'rb') as review_file:
        reader = csv.DictReader(
            review_file, fieldnames=media_review_fields, restval="")
        try:
            for row in reader:
                print ". "
                all_reviews.insert(0, row)
        except csv.Error as e:
            # On Error:- raise error and exit
            sys.exit('file %s, line %d: %s' %
                     (media_reviews, reader.line_num, e))
    print "Done reading reviews."


def createandaddmovie(row):
    """
    createandaddmovie(row) creates a new instance of movie class
    based on the row passed in. it calls the get_media_reviews
    to get and assign the reviews for this media. Once the movie
    instance is ceated and reviews read the instance is added to the
    movies_list.
    Arguments:
        row: a row read from the CSV file
    """
    temp_media = samsMovieLib.Movie(row['id'], row['title'],
                                    row['duration'], row[
                                        'pg_rating'], row['cast'],
                                    row['poster_url'], row[
                                        'trailer_url'], row['story_line'],
                                    row['genres'], row['director'],
                                    row['year'])
    get_media_reviews(temp_media)  # get the reviews for current media
    movies_list.insert(0, temp_media)  # add the object to the movies_list


def createandaddshow(row):
    """
    createandaddshow(row) creates a new instance of TVShow class
    based on the row passed in. it calls the get_media_reviews
    to get and assign the reviews for this media. Once the TVShow
    instance is ceated and reviews read the instance is added to the
    movies_list.
    Arguments:
        row: a row read from the CSV file
    """
    temp_media = samsMovieLib.TVShow(row['id'], row['title'],
                                     row['duration'], row[
                                         'pg_rating'], row['cast'],
                                     row['poster_url'], row[
                                         'trailer_url'], row['story_line'],
                                     row['genres'], row['director'],
                                     row['year'], row['episodes'],
                                     row['seasons'])
    get_media_reviews(temp_media)  # get the reviews for current media
    shows_list.insert(0, temp_media)  # add the object to the movies_list


def get_media_reviews(media):
    """
    get_media_reviews() checks and add the reviews to the media instance
    passed as an argument. The function iterates over the all_reviews List
    and if it finds an review with matching media_id it will add it to the
    media instance using the addmediarating method.
    Arguments:
        media: an instance of TVShow or the Movie class.
    Returns
        Nothing
    """
    for review in all_reviews:
        if review['media_id'] == media.media_id:
            media.addmediarating(
                int(review['rating']), review['review'], review['user_name'])


print "Initializing Sam's Movie Club"
read_reviews_csv()
read_media_csv()
print "Creating HTML View"
fresh_tomatoes.open_movies_page(movies_list, shows_list)
print "All Done"
