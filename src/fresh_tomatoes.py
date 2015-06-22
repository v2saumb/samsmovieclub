import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Sam's Movie Club</title>
    <!-- Bootstrap 3 -->
    <link rel="stylesheet"
    href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet"
     href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script
    src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .navbar-inverse {
            background-image: linear-gradient(to bottom, #0CA9FF 0px,
                               #282599 100%);
            background-repeat: repeat-x;
        }
        .navbar-inverse .navbar-brand {
           color: #fff;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        .row-border{
            padding-bottom:5px;
            padding-top:5px;
            border-bottom:1px solid #ccc;
        }
        .content_scroll{
            overflow-y: scroll;
            height: 300px;
            width: 100%;

        }
        .row{
            border-bottom: 0.1em solid #ccc;
            padding-top: 10px;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal',
            function (event) {
        // Remove the src so the player itself gets removed, as this is
        // the only reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId
            + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>",{
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal"
          aria-hidden="true">
          <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Sam's Movie Club</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
  <div id="content">
  <ul id="tabs" class="nav nav-tabs  row" data-tabs="tabs">
            <li class="active">
            <a href="#Movies" data-toggle="tab">Movies</a></li>
            <li><a href="#TVShow" data-toggle="tab">TV Shows</a></li>
       </ul>
        <div id="main_tab_content" class="tab-content ">
            <div class="tab-pane active" id="Movies">
            <div id="content">
                {movie_tiles}
            </div>
            </div>
            <div class="tab-pane" id="TVShow">
              <div id="content">
                {tv_show_tiles}
            </div>
            </div>
        </div>
    <div>
    </div>
  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
   <div id="{media_id}_content" class="row">
   <div class="col-md-5 movie-tile text-center"
   data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal"
   data-target="#trailer">
    <img src="{poster_url}" width="220" height="342" />
    <h3>{movie_title}</h3>
    <h5>{media_pg_rating} | {media_duration} </h5>
</div>
        <ul id="tabs_movie" class="nav nav-tabs  col-md-7" data-tabs="tabs">
            <li class="active"><a href="#{media_id}_story" data-toggle="tab">
            Story Line</a></li>
            <li><a href="#{media_id}_cast" data-toggle="tab">
            Cast and Director</a></li>
            <li><a href="#{media_id}_ratings"
            data-toggle="tab">Reviews & Ratings</a></li>
        </ul>
        <div id="movies-tab-content" class="tab-content col-md-5">
            <div class="tab-pane active" id="{media_id}_story">
                <h3>Story Line</h3>
                <p>{movie_story_Line}</p>
                <h3>Genres</h3>
                <p>{media_genres}</p>
                <h3>Duration</h3>
                <p>{media_duration}</p>
            </div>
            <div class="tab-pane" id="{media_id}_cast">
                <h3>Director</h3>
                <p>{movie_director}</p>
                <h3>Cast</h3>
                <p>{movie_cast}</p>
            </div>
            <div class="tab-pane" id="{media_id}_ratings">
                <p><strong>Average Viewer's Rating:</strong>
                 {media_avg_rating} / 10 </p>
                <p><strong>Total Reviews:</strong>{total_reviews}</p>
                <div class="content_scroll">
                {media_reviews}
                </div>
            </div>
        </div>
        </div>
'''
# A single movie entry html template
shows_tile_content = '''
   <div id="{media_id}_content" class="row">
   <div class="col-md-5 movie-tile text-center"
   data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal"
   data-target="#trailer">
    <img src="{poster_url}" width="220" height="342" />
    <h3>{show_title}</h3>
    <h5>{media_pg_rating} | {media_duration} </h5>
   </div>
        <ul id="tabs_tv" class="nav nav-tabs  col-md-7" data-tabs="tabs">
            <li class="active">
                <a href="#{media_id}_story" data-toggle="tab">Story Line</a>
             </li>
            <li>
                <a href="#{media_id}_cast" data-toggle="tab">
                Cast and Director</a>
            </li>
            <li>
                <a href="#{media_id}_ratings"
                data-toggle="tab">Reviews & Ratings</a>
            </li>
        </ul>
        <div id="shows-tab-content" class="tab-content col-md-5">
            <div class="tab-pane active" id="{media_id}_story">
                <h3>Story Line</h3>
                <p>{show_story_Line}</p>
                <h3>Genres</h3>
                <p>{media_genres}</p>
                <h3>Duration</h3>
                <p>{media_duration}</p>
                <h3>Number of Episodes</h3>
                <p>{show_episodes}</p>
                <h3>No of Seasons</h3>
                <p>{show_nos}</p>
            </div>
            <div class="tab-pane" id="{media_id}_cast">
                <h3>Creators</h3>
                <p>{show_creator}</p>
                <h3>Cast</h3>
                <p>{show_cast}</p>
            </div>
            <div class="tab-pane" id="{media_id}_ratings">
                <p><strong>Average Viewer's Rating:</strong>
                 {media_avg_rating} / 10 </p>
                <p><strong>Total Reviews:</strong>{total_reviews}</p>
                <div class="content_scroll">
                {media_reviews}
                </div>
            </div>
        </div>
        </div>
'''

# A single review entry html template
movie_reviews_content = '''
   <div class="row row-border">
       <div class="col-md-5"><strong>User: </strong>{user_name}</div>
       <div class="col-md-5"><strong>Rating: </strong>{user_rating} / 10</div>
       <div class="col-md-10"><strong>Comments: </strong>{user_review}</div>
   </div>

'''


def create_movie_tiles_content(movies):
    """
    The HTML content for the movies section of the page
    Arguments:
        movies a list of moivies
    Returns:
        Html content for the movies list section
    """

    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_url)
        trailer_youtube_id = youtube_id_match.group(
            0) if youtube_id_match else None

        # Append the details for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title + "(" + movie.releaseYear + ")",
            poster_url=movie.poster_url,
            trailer_youtube_id=trailer_youtube_id,
            movie_story_Line=movie.story_line,
            movie_director=movie.director,
            movie_cast=movie.cast,
            media_id=movie.media_id,
            media_avg_rating=movie.viewer_rating.average_rating,
            media_pg_rating=movie.pg_rating,
            media_duration=movie.duration,
            media_genres=movie.genres.replace("|", ","),
            total_reviews=movie.viewer_rating.total_rating - 1,
            media_reviews=create_movie_reviews_content(movie.viewer_rating)
        )
    return content


def create_shows_tiles_content(tv_shows):
    """
    The HTML content for the movies section of the page
    Arguments:
        movies a list of moivies
    Returns:
        Html content for the movies list section
    """

    content = ''
    for show in tv_shows:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', show.trailer_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', show.trailer_url)
        trailer_youtube_id = youtube_id_match.group(
            0) if youtube_id_match else None

        # Append the details for the movie with its content filled in
        content += shows_tile_content.format(
            show_title=show.title + "(" + str(show.first_aired) + ")",
            poster_url=show.poster_url,
            trailer_youtube_id=trailer_youtube_id,
            show_story_Line=show.story_line,
            show_creator=show.creator,
            show_cast=show.cast,
            media_id=show.media_id,
            media_avg_rating=show.viewer_rating.average_rating,
            media_pg_rating=show.pg_rating,
            media_duration=show.duration,
            media_genres=show.genres.replace("|", ","),
            total_reviews=show.viewer_rating.total_rating - 1,
            media_reviews=create_movie_reviews_content(show.viewer_rating),
            show_nos=show.no_of_seasons,
            show_episodes=show.episodes
        )
    return content


def create_movie_reviews_content(viewers_rating):
    """
    The HTML content for the review section of the page
    Arguments:
        movies a list of moivies
    Returns:
        Html content for the review section
    """
    content = ''
    for review in viewers_rating.current_reviews:
        # Append the reviews and rating with its content filled in
        if len(review.user_review) > 0:  # Pick non blank reviews only
            content += movie_reviews_content.format(
                user_rating=review.user_rating,
                user_review=review.user_review,
                user_name=review.user_name
            )
    return content


def open_movies_page(movies, tv_shows):
    # Create or overwrite the output file
    output_file = open('html/samsMovieClub.html', 'w')

    # Replace the placeholder for the movie tiles with the actual
    # dynamically generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies),
        tv_show_tiles=create_shows_tiles_content(tv_shows))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser
    url = os.path.abspath(output_file.name)
    print "Opening browser..."
    # open in a new tab, if possible
    webbrowser.open('file://' + url, new=2)
