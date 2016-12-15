from bottle import route, run, template, static_file, request


def get_movies_from_file():
    try:
        my_file = open("storage/movies.txt", "r")
    except:
        my_file = open("storage/movies.txt", "w").close()
        my_file = open("storage/movies.txt", "r")

    movies = []

    for movie in my_file.read().split("\n"):
        movies.append(movie)

    my_file.close()
    return movies

    
@route("/")
def index():
    return template("index", movies=get_movies_from_file())

@route("/add_movie")
def add_movie():
    return template("add_movie")

@route("/save_movie", method="POST")
def save_movie():
    title = request.forms.get("title")
    my_file = open("storage/movies.txt", "a")
    my_file.write("\n" + title)
    my_file.close()

    return template("index", movies=get_movies_from_file())

@route("/contact")
def contact():
    return "<h1>Här kommer snart en kontaktsida att visas</h1>"

@route("/static/<filename>")
def static_files(filename):
    return static_file(filename, root="static")
    

run(host="127.0.0.1", port=8080)
