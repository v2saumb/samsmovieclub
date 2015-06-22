# Introduction
This a demo project for a small movie reviews website. called "Sam's Movie Club". 
This program demonstrates the different aspects of Python programming. 
The reviews and other informatin the site contains is total fiction and is
ment for demonstrations only


**Table of Contents**

1. [How To Run](#how-to-run)   
2. [Assumptions](#assumptions)
3. [Directory Structure](#dir-structure)
    - [Html](#html-page)
    - [Media db](#mediadb)
        - [Media Details](#media-details)
        - [Media Reviews](#media-reviews)
    - [Src](#src-folder)
        - [Sams Movie Club Lib](#sams-lib)
            - [Media](#media)                    
            - [Rating](#rating)
            - [ViewerRating](#viewer-rating)
            - [Movie](#movie)
            - [TVShow](#tv-show)
        - [Sams Movie Club](#sams-club)
            - [Program Flow](#program-flow)    
        - [Fresh Tomatoes](#fresh-tomatoes)    

<a name="how-to-run"></a>
### How To Run

** Prerequsites **
1. Python v2.7 or greater should be installed.
2. PYTHON environment variable should be correctly set with the path to python executable.
3. PYTHONPATH environment variable should be set with the python root folder

**Using Windows Explorer**

1. Navigate to the samsmovieclub folder on the drive.
2. Double click on the **movieclub.bat** file to run **samsmovieclub.py** file.
3. The default browser should open with the **samsMovieClub.html** page.

**Using Command Prompt**
1. Navigate to the samsmovieclub folder on the drive.
2. Execute the **movieclub.bat** file to run **samsmovieclub.py** file.
3. The default browser should open with the **samsMovieClub.html** page.


<a name="assumptions"></a>
### Assumptions

1. All data used is for demonstration only and completely fictitious.
2. All user names used and rating are for demonstration only.
3. In this version of the code the only way to add media and media reviews is through the csv files mentioned in this document.
4. Data is validated before hand ehen entring it in csv files. 


<a name="dir-structure"></a>
# Directory Structure
The following section represents the directory structure.
```
samsmobieclub
|
+-- html
|   +-- samsMovieClub.html
+-- mediadb
|   +-- mediadetails.csv
|   +-- mediareviews.csv
+-- src
|   +--fresh tomatoes.py
|   +--samsmovieclub.py
|   +--samsMovieLib.py
+-- readme.txt
+-- readme.md
+-- mediaclub.bat
```
  
<a name="html-page"></a>
## HTML 
The html folder is the output folder contains the output file **samsMovieClub.html**.
Once the program executes sucessfully the above file is created and then using
the browser module rendered in the default browser. 


<a name="mediadb"></a>
## Media db
  This folder in the project contains two **.csv** files containing media details and media reviews. 

<a name="media-details"></a>
### Media Details

The **mediadetails.csv** file contains the basic information about the movies and tv shows. The file was generated using Microsoft Excel but you can ues any text editor. The secquence of fields has to be excatly the same as shown below. If the sequence does not match incorect data will be displayed on the Html page.

**Media Detials File Structure: **

| id  | type  | title  | duration  | pg_rating  | cast  | poster_url  | trailer_url  | story_line  |  genres | director  | year  |  episodes | seasons  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |

**Property Details: **

| Property  | Details  |
|---|---|
| id  |  A unique int id for the the movie or tv show. |
| type  |  MOVIE or TVSHOW depending on the type of record being entered |
| title  | The title of the movie or the tv show.   |
| duration  | The duration of the movie or the tv show. |
| pg_rating  | The PG rating for the movie or the tv show.  |
| cast  | The cast of the movie or the tv show.  |
| poster_url  | The poster image url for the movie or the tv show.  |
| trailer_url  | The youtube trailer url for the movie or the tv show.  |
| story_line  |  The storyline of the movie or the tv show. |
| genres  | The Generes that the movie or the tv show belongs to.  |
| director  | The director / creatror of the movie or the tv show.   |
| year  | The year in when the move or the tv show was released.  |
| episodes  | The number of episodes currently availabe. This property is ued only for tv shows, when entering details for a movie this field can be left blank  |
| seasons  |  The number of seasons already aired for the tv show. This property is ued only for tv shows, when entering details for a movie this field can be left blank |


<a name="media-reviews"></a>
### Media Reviews

The **mediareviews.csv** file contains the review information about the movies and tv shows. The file was generated using Microsoft Excel but you can ues any text editor. The secquence of fields has to be excatly the same as shown below. If the sequence does not match incorect data will be displayed on the Html page.

**Media Reviews File Structure: **

| media_id  | user_name  | review  | rating  | 
|---|---|---|---|
|   |   |   |   |

**Property Details: **

| Property  | Details  |
|---|---|
| media_id  |  A int id matching one of the entries in the media details csv for the the movie or tv show. |
| user_name  | The user name of the person entering the review. |
| review  | The review commente by the user |
| rating  | The integer between 1 - 10 depecting the rating by the user 10 being the highest |

<a name="src-folder"></a>
### Src Folder
The src folder contains the **.py** files required to generate the "Sam's Movie Club" html page.There are three files in the folder.

* samsMovieLib.py
* samsmovieclub.py
* fresh_tomatoes.py

<a name="sams-lib"></a>
#### samsMovieLib.py

The **samsMovieLib.py** file contains all the custom python classes used in this project. 

* Media
* Rating
* ViewerRating
* Movie
* TVShow

<a name="media"></a>
#### Media 

The class Media contains the Basic Information about the media.
Information like Title  for the movie or tv series.
The class also contains the method to show the media trailer.
        
**Attributes:**

|Attribute  | Details |
| --- | --- |
|mediaId |    A reference Id |
|mediaType |  TV or MOVIE |
|title |      Title of the media |
|duration |   Duration of the movie.In case or TV show the duration of the episodes|
|pgrating |   The pg rating for the the movie or the tv show|
|cast |       The case for this media|
|poster |     The poster image url for the media|
|trailerurl | The youtube trainer url|
|media_storyline |   The story line of the movie or the tv show|
|genres |     The gerenes for the media|
|viewer_rating |  The rating information about he media|

<a name="rating"></a>
#### Rating

 Individual rating class that containg the users review and ratings.

** Attributes: **

|Attribute  | Details |
| --- | --- |
| user_rating | A integer between 1 - 10 |
| user_review | A string containgin the users review user_name |

<a name="viewer-rating"></a>
#### ViewerRating

ViewerRating  the class containg the viewer ratings for any media


** Attributes: **

|Attribute  | Details |
| --- | --- |
| MAX_RATING | The maximum any media can be rated. |
| current_rating | The current average rating. |
| total_ratings | The total number of reviews or ratings present. |
| current_revies | An array of te current reviews |
| acerage_rating | The average rating for the media |


<a name="movie"></a>
#### Movie
The class Movies that inherites Media class and represents a media type of movie

** Additional Attributes: **

|Attribute  | Details |
| --- | --- |
| director | the name of the director of the movie |
| releaseTear | the year whne the movie was released |


<a name="tv-show"></a>
#### TVShow

 The class TVShow that inherites Media class and represents a media type of TV show.

** Additional Attributes: **

|Attribute  | Details |
| --- | --- |
| creator | The name of the director of the movie |
| episodes |       The number of episodes that the TV show has. |
| no_of_seasons |   The number of season for the |

<a name="sams-club"></a>
### samsmovieclub.py

The **samsmovieclub.py** has code to read the csv files located in the mediadb folder and then calls the fresh_tomatoes.py to generate the html page for sams movie club. The detailed documentaiton is contained in the class.

<a name="program-flow"></a>
#### Program FLow

1. The code first reads the **mediareviews.csv** and loads all the reviews in a list **all_reviews**. 
2. The code then parses the **mediadetails.csv** and for each row decides if it is a movie or a TV show. A appropreate instance of Movie or the TVShow class is created. 
3. The code reads the **all_reviews** and gets and adds all the reviews for the current media.
4. The instance is then added to the movie_list or the shows_list as per media_type.
5. Once all the rows are read the fresh_tomatoes is called to parse and create the list


<a name="fresh-tomatoes"></a>
### fresh_tomatoes.py

This is the sane file contained and ued during the training course. The file contains code that parses the movie_list and the shows list and writes the **samsMovieClub.html** in the html folder. Minor changes have been made to in corporate the TV shows, reviews  and a few other style changes.


