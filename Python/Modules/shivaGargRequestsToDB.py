# Thank you Shiva!!https://repl.it/@shgargir/UPRM-Python-Workshop
import requests

# Replace "YOUR_API_KEY" with your own API key.
# Api key can be obtained from http://www.omdbapi.com/
# We are pulling info from the IMDB database, but there
# are thousands of public APIs. E.g. see https://any-api.com
API_KEY = "YOUR_API_KEY"

def getMovieDetails(title):
    """Queries IMDB to fetch movie information.

  Args:
    title: A string representing the title of the movie
    to search.

  Returns:
    A json dictionary containing movie information such
    as the title, plot actors etc.
  """
  # build the api endpoint to call.
  # for e.g. to call the api to get information for
  # the movie jumanji, the url should look like
  # http://www.omdbapi.com/?t=jumanji&apikey=YOUR_API_KEY
  url = ""
  if url != "":
      # make the request and save the response
    response = requests.get(url)
    # extract data in json format 
    data = response.json() 
    return data

def printRecommendation(score):
    """Prints a recommendation to watch or skip a movie.

  Args:
    score: A float representing the Rotten Tomatoes
    rating for a movie (e.g. 92.0, representing 92 out of 100).
  """
  print("Not enough data to make a recommendation.")

def getRottenTomatoesRating(ratings):
    """Return the rotten tomato score of the movie.

  Args:
    ratings: A list of dictionaries encapsulating ratings from
    different bodies such as imdb, rotten tomatoes etc.
  """
  return -1

def critique(movieDetails):
    """Parses movie details and displays a recommendation
     on whether to watch the movie that was searched
     for.

  Args:
    movieDetails: Dictionary containing details about
    the movie.
  """
  if movieDetails is None:
      print("Movie details could not be retrieved. Is your code hooked up correctly?")
    return

title = movieDetails.get('Title')
  if title is None:
      print('Movie not found.')
  else:
      # Extract information to print
    # extract year
    # extract director
    # extract actors
    # extract plot
    # extract ratings and pass it as
    # the argument to getRottenTomatoesRating
    # to get the score
    ratings = None
    score = getRottenTomatoesRating(ratings)
    # format and print the details
    printRecommendation(score)

def main():
    print("Welcome to Mayaguez Movie Critic")
  movieTitle = input("What movie do you want a recommendation for? [Q to quit] ")
  while movieTitle != 'Q' and movieTitle != 'q':
      movieDetails = getMovieDetails(movieTitle)
      critique(movieDetails)
      movieTitle = input("What movie do you want a recommendation for? [Q to quit] ")

main()mport requests
https://repl.it/repls/GroundedCloseNasm

dir(requests)
