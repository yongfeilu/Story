	#Final Project (proj8)

	The project is web application based on a movie database. It can search and display movies that match certain conditions, 
	show reviews for a given movie, add a new movie to the database, add and link a new review to a given movie, and delete
	movies along with the corresponding reviews from our database. 

	final.py: main logic of the web application

	views/: directory that contains all the tpl files to form the view of different routes

	main.tpl: forms the view of hello world page 
			  - corresponding route: '/hello'

	home_page.tpl: forms the view of the search page
				   - corresponding route: '/' or '/homepage'
				   - search attributes: Title* (wild like), ID (number), Released After (date), Released By (date), Language
				   - functionality: search movies that match the conditions

	results.tpl: forms view for the movie searching results, a list of movies matching the conditions
				 - corresponding route:' /movies'
				 - attributes displayed: Film (movie title), Release Date, Language
				 - links to other functionalities: View/Edit, Delete, Show participants, Add a new participant
				 - button: Add a New Movie
				 - empty result: 'There is no movie matching the conditions.' will be displayed

	add_movie.tpl: form the view of the web page to add new movies
				   - corresponding route: '/movies/add'
				   - attribute input(no empty input): Film (string), Release Date (date),
				   	 Language (string of characters), Budget (number >= 0), Box_office (number >= 0)
				   - error handling: if Language or Length is of incorrect format, error message will be displayed

	edit.tpl: forms the view of the web page to view or edit the detailed attributes of a given movie
			  - corresponding route: '/movies/<movie_id:int>'
			  - attribute input (no empty input): Film (string), Release Date (date), Length (format dd:dd:dd),
			  	Language (string of characters),Budget (number >= 0),Box_office (number >= 0),ID (read only)
			  - error handling: if Language or Length is of incorrect format, error message will be displayed

	participants.tpl: forms the view of the web page to list all the participants recorded of the chosen movie
				 - corresponding route: '/participants/<movie_id:int>'
			  	 - attributes displayed: Professional ID, Name, Gender, Date_Birth, Country, Occupation
			  	 - empty result: 'Oops! No participants recorded yet.' will be displayed

	add_participants.tpl: forms the view of the web page to add participants to a given movie
					 - corresponding route: /participants/<movie_id:int>/add
					 - attribute input: Professional ID (number), Name (text), Gender (select options), Date of 
					   Birth(date), Country (text), Occupation (text)
					 - choice to add an existing participant is available
					 - error handling: error message will be displayed (1) if you click the button 'Add An 
					   Existing Person' but haven't chosen an existing movie professional; (2) if you click
					   the button "Add A New Participant" but leave some inputs empty; (3) Country or 
					   Occupation input is of incorrect format
					   
	header.tpl & footer.tpl: tpl files to improve the design of the web pages


	views/error_views: directory that contains all the error message pages

	err404.tpl: error message for 404 error

	err500.tpl: internal server error message


