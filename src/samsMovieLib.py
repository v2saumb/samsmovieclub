import webbrowser


# Media Class
class Media():

    """ The class Media contains the Basic Information about the media.
        Information like Title  for the movie or tv series.
        The class also contains the method to show the media trailer.
        Attributes:
            mediaId:   A reference Id,
            mediaType: TV or MOVIE,
            title:     Title of the media,
            duration:  Duration of the movie.
                       In case or TV show the duration of the episodes,
            pgrating:  The pg rating for the the movie or the tv show,
            cast:      The case for this media,
            poster:    The poster image url for the media,
            trailerurl:The youtube trainer url,
            media_storyline:  The story line of the movie or the tv show,
            genres:    The gerenes for the media
            viewer_rating: The rating information about he media
    """

    def __init__(self, md_id, md_type, md_title, md_duration,
                 md_pg_rating, md_cast, poster,
                 md_trailer_url, media_storyline, media_genres):
        """Constructor for class Media
            Attributes:
                md_id:      A reference Id,
                md_type:    TV or MOVIE,
                md_title:   Title of the media,
                md_duration:Duration of the movie. In case of TV show
                            the duration of the episodes,
                md_pg_rating:  The pg rating for the the movie or the tv show,
                md_cast:      The case for this media,
                poster:         The poster image url for the media,
                md_trailer_url:     The youtube trainer url,
                media_storyline:The story line of the movie or the tv show, and
                media_genres:   The gerenes for the media
            """
        self.media_id = md_id
        self.media_type = md_type
        self.title = md_title
        self.duration = md_duration
        self.pg_rating = md_pg_rating
        self.cast = md_cast
        self.poster_url = poster
        self.trailer_url = md_trailer_url
        self.story_line = media_storyline
        self.genres = media_genres
        self.viewer_rating = ViewerRating()

    def show_trailer(self):
        """
        Opens the youtube trailer
        Arguments:
            None
        Returns:
            None
        """
        webbrowser.open(self.trailer)


# Rating class
class Rating():

    """
    Individual rating class that containg the users review and ratings.
    Attribute:
        user_rating: A integer between 1 - 10
        user_review: A string containgin the users review
        user_name
    """

    def __init__(self, usr_review="", usr_rating=0, usr_name=""):
        """
            Constructor for the rating class
            Arguments:
               usr_review: A users review for the media
               usr_rating: A int between 1 - 10 for users rating for the media
               usr_name: A string user name
        """
        self.user_rating = usr_rating
        self.user_review = usr_review
        self.user_name = usr_name


# Viewer Ratings Class
class ViewerRating():

    """
    ViewerRating  the class containg the viewer ratings for any media
    Attributes:
        MAX_RATING:         The maximum any media can be rated.
        current_rating:     The current average rating.
        total_ratings:      The total number of reviews or ratings present.
        current_revies:     An array of te current reviews
        acerage_rating:     The average rating for the media
    """
    MAX_RATING = 10

    def __init__(self):
        temp_rating = Rating()
        self.current_reviews = [temp_rating]
        self.total_rating = len(self.current_reviews) - 1
        self.average_rating = 0
        self.adjust_ratings()

    def add_rating(self, rating, review, username):
        """"
        Adds the review and ratings for a a media
        Args:
            rating a number between 0 - 10
            review a string containing the review comments by the user
            username a string containing the user name who added the review
        Returns:
            The function rturns nothing. Will show error if
            the rating passed is not within
            the range appropreate error will be disaplayed
        """
        # check and throw error if the rating is not in range
        if int(rating) < 0 or int(rating) > 10:
            print("Please Enter Rating Between [0 - 10]")
            return
        else:
            new_rating = Rating(review, rating, username)
            self.current_reviews.insert(0, new_rating)
        self.adjust_ratings()

    def adjust_ratings(self):
        """"
        adjusts the average raiting for this media
        Args:
            none
        Returns:
            nothing
        """
        self.total_rating = len(self.current_reviews)
        if self.total_rating == 0:
            self.average_rating = 0
            return
        rating_sum = 0
        for iReview in self.current_reviews:
            # Continue the loop and add the ratings
            rating_sum = rating_sum + iReview.user_rating
        # calculate and set average rating
        if self.total_rating == 1:
            self.average_rating = rating_sum / self.total_rating
        else:
            self.average_rating = rating_sum / (self.total_rating-1)


# The Movie Class
class Movie(Media):

    """
    The class Movies that inherites Media class and represents
    a media type of movie
    Attributes:
        director: the name of the director of the movie
        releaseTear: the year whne the movie was released
    """

    def __init__(self, md_id=1, media_title="", media_duration="0",
                 media_pgrating="G", media_cast="", media_poster="",
                 media_trailerurl="", media_storyline="", media_genres="",
                 media_director="", media_released=1900):
        Media.__init__(self, md_id, "MOVIE", media_title,
                       media_duration, media_pgrating, media_cast,
                       media_poster, media_trailerurl, media_storyline,
                       media_genres)
        self.director = media_director
        self.releaseYear = media_released

    def addmediarating(self, rating, review, username):
        """
        addmediarating setter method for the parent Media class
        set a rating to the viewer_rating property
        Arguments:
            rating: rating given by te user
            review: review comments by the user
            username: user name of the reviewer
        """
        self.viewer_rating.add_rating(rating, review, username)


# TV Show Class
class TVShow(Media):

    """
    The class TVShow that inherites Media class anf represents a media type
    of TV show.
    Attributes:
        creator:        The name of the director of the movie
        episodes:       The number of episodes that the TV show has.
        no_of_seasons   The number of season for the
    """

    def __init__(self, md_id=1, media_title="", media_duration="0",
                 media_pgrating="G", media_cast="", media_poster="",
                 media_trailerurl="", media_storyline="", media_genres="",
                 media_creator="", media_aired="1990", no_episodes=0,
                 no_seasons=1):
        Media.__init__(self, md_id, "TVSHOW", media_title, media_duration,
                       media_pgrating, media_cast, media_poster,
                       media_trailerurl, media_storyline, media_genres)
        self.first_aired = media_aired
        self.creator = media_creator
        self.episodes = no_episodes
        self.no_of_seasons = no_seasons

    def addmediarating(self, rating, review, username):
        """
        addmediarating setter method for the parent Media class
        set a rating to the viewer_rating property
        Arguments:
            rating: rating given by te user
            review: review comments by the user
            username: user name of the reviewer
        """
        self.viewer_rating.add_rating(rating, review, username)
