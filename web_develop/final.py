from bottle import Bottle, post, get, HTTPResponse, request, response, template, route, redirect, delete, error
import bottle
import os
import sys
import psycopg2 as pg
import logging
import argparse
import re


#The logging level to control what messages are shown (skipping debug)
logging.basicConfig(level=logging.INFO)

#Our bottle app, using the default. We can store variables in app
app = bottle.default_app()

#Hello World
@get("/hello")
def hello():
    '''
    show hello world page
    '''
    # Use a template to get the HTML to return. This template needs variables page_name (also for header.tpl) and  body 
    return template('main', page_name='Hello, World', body='This is the body of hello world')


@get("/")
@get("/homepage")
def homepage():
    '''
    show the homepage or movie search page
    '''
    cur = app.db_connection.cursor()
    cur.execute("SELECT DISTINCT language FROM movie")
    lans = cur.fetchall()
    return template('home_page', page_name='Homepage', lans=lans)


@get("/movies")
def results():
    '''
    show the movie searching result page
    '''
    params = {}
    if request.GET.get('Title') != None:
        params['title'] = ('LIKE','%' + request.GET.get('Title').title() + '%')
        params['after'] = ('>=', request.GET.get('Released After'))
        params['by'] = ('<=', request.GET.get('Released By'))
        params['language'] = ('=', request.GET.get('Language'))
        params['movie_id'] = ('=', str(request.GET.get("ID")))

    # create the query
    if not [v[1] for v in params.values() if v[1].strip("%")]:
        exp = "SELECT * FROM movie"
    else:
        exp = "SELECT * FROM movie WHERE"
        i = 0
        for key, t in params.items():
            if t[1] and t[1] != '%%':
                if key == 'by' or key == 'after':
                    if i  == 0:
                        exp += (" release_date " + t[0] + " '" + t[1] + "'")
                    else:
                        exp += (" AND release_date " + t[0] + " '" + t[1] + "'")
                elif key == "ID":
                    if i == 0:
                        exp += (" " + key + " " + t[0] + " " + t[1])
                    else:
                        exp += (" AND " + key + " " + t[0] + " " + t[1])
                else:
                    if i == 0:
                        exp += (" " + key + " " + t[0] + " '" + t[1] + "'")
                    else:
                        exp += (" AND " + key + " " + t[0] + " '" + t[1] + "'")
                i += 1

    exp += " ORDER BY release_date LIMIT 20"
    cur = app.db_connection.cursor()
    cur.execute(exp)
    ms = cur.fetchall()
    return template('results', page_name='Result', data=ms)


@get("/movies/<movie_id:int>")
def view_movie(movie_id):
    '''
    show the view/edit movie page 
    '''
    cur = app.db_connection.cursor()
    cur.execute("SELECT * FROM movie WHERE movie_id = %s", (movie_id,))
    movie = cur.fetchone()
    return template('edit', page_name="Edit", data=movie, err=None)


@post("/movies/<movie_id:int>")
def update_movie(movie_id):
    '''
    upload the movie updating information to our database
    '''
    m_id = request.POST.get('ID')
    film = request.POST.get('name')
    date = request.POST.get('release_date')
    box_office = request.POST.get('box_office')
    budget = request.POST.get('budget')
    language = request.POST.get('language')
    length = request.POST.get('length')
    erorr_msg = None

    cur = app.db_connection.cursor()

    len_r = re.compile('\d{1,2}:[0-5][0-9]:{0,1}\d{0,2}')
    if not len_r.match(length):
    	erorr_msg = "Error: your length input is of incorrect format."
    	cur.execute("SELECT * FROM movie WHERE movie_id = %s", (m_id,))
    	movie = cur.fetchone()
    	return template('edit', page_name='Edit', data=movie, err = erorr_msg)


    lan_r = re.compile('[a-zA-Z]+')
    if not lan_r.match(language):
    	erorr_msg = "Error: your language input is of incorrect format."
    	cur.execute("SELECT * FROM movie WHERE movie_id = %s", (m_id,))
    	movie = cur.fetchone()
    	return template('edit', page_name='Edit', data=movie, err = erorr_msg) 

    
    cur.execute("UPDATE movie SET title = %s, release_date = %s, language = %s, length = %s, box_office = %s, budget = %s WHERE movie_id = %s", (film, date, language, length, box_office, budget, m_id))
    app.db_connection.commit()

    cur.execute("SELECT * FROM movie WHERE movie_id = %s", (m_id,))
    movie = cur.fetchone()

    return template('edit', page_name='Edit', data = movie, err = erorr_msg)


@delete("/del/<movie_id:int>", method="GET")
def delete_movie(movie_id):
    '''
    delete the chosen movie from out database
    '''
    cur = app.db_connection.cursor()
    cur.execute("DELETE FROM movie WHERE movie_id = %s", (movie_id,))
    app.db_connection.commit()

    return redirect('/movies')


@get("/participants/<movie_id:int>")
def get_participants(movie_id):
    '''
    get the page to list all the reviews for a given movie
    '''
    cur = app.db_connection.cursor()
    cur.execute("SELECT title FROM movie WHERE movie_id = %s", (movie_id,))
    film = cur.fetchone()

    cur.execute("SELECT movie_professional.professional_id, name, gender, date_birth, country, occupation FROM movie\
    			 NATURAL JOIN works_in NATURAL JOIN movie_professional WHERE movie.movie_id = %s", (movie_id,))
    professionals = cur.fetchall()

    # cur.execute("SELECT user_id, rev_text, score, submit_time FROM movie NATURAL JOIN reviews WHERE movie.movie_id = %s", (movie_id,))
    # revs = cur.fetchall()

    return template('participants', page_name="Participants", data=professionals, film=film)


@get("/participants/<movie_id:int>/add")
def add_participants(movie_id):
    '''
    show the web page to add the movie review
    '''
    cur = app.db_connection.cursor()
    cur.execute("SELECT title FROM movie WHERE movie_id = %s", (movie_id,))
    film = cur.fetchone()

    # cur.execute("SELECT DISTINCT rev_text FROM reviews;")
    # reviews = [t[0] for t in cur.fetchall()]

    
    cur.execute("SELECT professional_id, name FROM movie_professional\
    			 WHERE professional_id NOT IN (SELECT professional_id FROM works_in WHERE movie_id = %s)", (movie_id,))
    profs = cur.fetchall()

    erorr_msg = None
    vals = [None] * 6

    return template('add_participants', page_name="Add Participants", film=film, movie_id=movie_id, profs=profs, vals=vals, err=erorr_msg)


@post("/participants/<movie_id:int>")
def upload_participants(movie_id):
    '''
    upload the review for a given movie to our database
    '''
    prof_id = request.POST.get("prof_id")
    name = request.POST.get("name")
    gender = request.POST.get("gender")
    date = request.POST.get("time")
    country = request.POST.get("country")
    occupation = request.POST.get("occupation")
    ex_prof_id = request.POST.get("ex_prof")

    erorr_msg = None
    vals = [prof_id, name, gender, date, country, occupation]

    new = request.POST.get("add_new")
    exist = request.POST.get("add_exist")

    cur = app.db_connection.cursor()
    cur.execute("SELECT title FROM movie WHERE movie_id = %s", (movie_id,))
    film = cur.fetchone()

    cur.execute("SELECT professional_id, name FROM movie_professional\
    			 WHERE professional_id NOT IN (SELECT professional_id FROM works_in WHERE movie_id = %s)", (movie_id,))
    profs = cur.fetchall()

    if new:
    	# empty error
    	if prof_id == "" or name == "" or gender == "" or date == "" or country == "" or occupation == "":
    		erorr_msg = "Error: some fileds are left empty."
    		return template('add_participants', page_name="Add Participants", film=film, movie_id=movie_id, profs=profs, vals=vals, err=erorr_msg)

    	# professional ID error
    	cur.execute("SELECT professional_id FROM movie_professional;")
    	prof_ids = [t[0] for t in cur.fetchall()]
    	
    	if int(prof_id) in prof_ids:
    		erorr_msg = "Error: Professional ID already exists."
    		return template('add_participants', page_name="Add Participants", film=film, movie_id=movie_id, profs=profs, vals=vals, err=erorr_msg)

    	# country and occupation illegal input
    	mode = re.compile('[a-zA-Z]+')
    	if (not mode.match(country)) or (not mode.match(occupation)):
    		erorr_msg = "Error: Country or Occupation is of inccorrect format (must be string of characters)."
    		return template('add_participants', page_name="Add Participants", film=film, movie_id=movie_id, profs=profs, vals=vals, err=erorr_msg)

    	cur.execute("INSERT INTO movie_professional (professional_id, name, gender, date_birth, country, occupation)\
    				 VALUES (%s, %s, %s, %s, %s, %s)", (prof_id, name.title(), gender, date, country.title(), occupation))
    	cur.execute("INSERT INTO works_in (professional_id, movie_id)\
    				 VALUES (%s, %s)", (prof_id, movie_id))
    	app.db_connection.commit()

    if exist:

    	if ex_prof_id == "":
    		erorr_msg = "Error: you haven't chosen an existing movie professional."
    		return template('add_participants', page_name="Add Participants", film=film, movie_id=movie_id, profs=profs, vals=vals, err=erorr_msg)

    	cur.execute("INSERT INTO works_in (professional_id, movie_id)\
    				 VALUES (%s, %s)", (ex_prof_id, movie_id))
    	app.db_connection.commit()


    cur.execute("SELECT movie_professional.professional_id, name, gender, date_birth, country, occupation FROM movie\
    			 NATURAL JOIN works_in NATURAL JOIN movie_professional WHERE movie.movie_id = %s", (movie_id,))
    professionals = cur.fetchall()

    return template('participants', page_name="Participants", data=professionals, film=film)

@get("/movies/add")
def add_movies():
    '''
    show the web page to add new movies
    '''
    erorr_msg = None
    vals = [None] * 6

    return template('add_movies', page_name='Add A New Movie', vals=vals, err=erorr_msg)

@post("/movies")
def upload_movies():
    '''
    upload the new movie to our database
    '''
    title = request.POST.get("title").title()
    date = request.POST.get("release_date")
    length = request.POST.get("length")
    lan = request.POST.get("language")
    budget = request.POST.get("budget")
    box_office = request.POST.get("box_office")

    erorr_msg = None
    vals = [title, date, length, lan, budget, box_office]

    len_r = re.compile('\d{1,2}:[0-5][0-9]:{0,1}\d{0,2}')
    if not len_r.match(length):
    	erorr_msg = "Error: length input is of incorrect format."
    	return template('add_movies', page_name='Add A New Movie', vals=vals, err=erorr_msg)

    lan_r = re.compile('[a-zA-Z]+')
    if not lan_r.match(lan):
    	erorr_msg = "Error: language input is of incorrect format."
    	return template('add_movies', page_name='Add A New Movie', vals=vals, err=erorr_msg)

    cur = app.db_connection.cursor()
    cur.execute("INSERT INTO movie (title, release_date, length, language, budget, box_office) \
                VALUES (%s, %s, %s, %s, %s, %s)", (title, date, length, lan, budget, box_office))
    app.db_connection.commit()

    cur.execute("SELECT * FROM movie WHERE title = %s AND release_date = %s AND language = %s and length = %s", (title, date, lan, length))
    movie = cur.fetchone()

    return template('results', page_name='Result', data=[movie])

@error(404)
def error404(error):
    '''
    show 404 error message
    '''
    return template('./error_views/err404', page_name="Error") 

@error(500)
def error500(error):
    '''
    show 500 error message
    '''
    return template('./error_views/err500', page_name="Error") 


#The main function to start the server
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c","--config",
        help="The path to the .conf configuration file.",
        default="server.conf"
    )
    parser.add_argument(
        "--host",
        help="Server hostname (default localhost)",
        default="localhost"
    )
    parser.add_argument(
        "-p","--port",
        help="Server port (default 53001)",
        default=53001,
        type=int
    )
    parser.add_argument(
        "--nodb",
        help="Disable DB connection on startup",
        action="store_true"
    )

    #Get the arguments
    args = parser.parse_args()
    if not os.path.isfile(args.config):
        logging.error("The file \"{}\" does not exist!".format(args.config))
        sys.exit(1)

    app.config.load_config(args.config)

    # Below is how to connect to a database. We put a connection in the default bottle application, app
    if not args.nodb:
        try:
            app.db_connection = pg.connect(
                dbname = app.config['db.dbname'],
                user = app.config['db.user'],
                password = app.config.get('db.password'),
                host = app.config['db.host'],
                port = app.config['db.port']
            )
        except KeyError as e:
            logging.error("Is your configuration file ({})".format(args.config) +
                        " missing options?")
            raise

    try:
        logging.info("Starting Bottle Web Server")
        app.run(host=args.host, port=args.port, debug=True, reloader=True)
    finally:
        #Ensure that the connection opened is closed 
        if not args.nodb:
            app.db_connection.close()
