# Input of movie data (definition of instances of the class Movie)

# (code partially taken from Udacity Nanodegree 'Intro to Programming' Stage 3 lessons,
# https://www.udacity.com/course/intro-to-programming-nanodegree--nd000)

# Movie information extracted from website: http://www.imdb.com

from class_def import Movie
import fresh_tomatoes

toy_story = Movie("Toy Story",
                    "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.",
                    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                    "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                    "Animation, Adventure, Comedy",
                    1995,
                    "Tom Hanks, Tim Allen, Don Rickles")

avatar = Movie("Avatar",
                    "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
                    "http://cdn.traileraddict.com/content/20th-century-fox/avatar-6.jpg",
                    "https://www.youtube.com/watch?v=cRdxXPV9GNQ",
                    "Action, Adventure, Fantasy",
                    2009,
                    "Sam Worthington, Zoe Saldana, Sigourney Weaver")

invictus = Movie("Invictus",
                    "Nelson Mandela, in his first term as the South African President, initiates a unique venture to unite the apartheid-torn land: enlist the national rugby team on a mission to win the 1995 Rugby World Cup.",
                    "https://upload.wikimedia.org/wikipedia/en/0/05/Invictus-poster.png",
                    "https://www.youtube.com/watch?v=RZY8c_a_dlQ",
                    "Biography, Drama, History",
                    2009,
                    "Morgan Freeman, Matt Damon, Tony Kgoroge")

the_judge = Movie("The Judge",
                    "Big-city lawyer Hank Palmer returns to his childhood home where his father, the town's judge, is suspected of murder. Hank sets out to discover the truth and, along the way, reconnects with his estranged family.",
                    "http://www.lawpracticeadvisor.com/wp-content/uploads/2014/10/The-judge-movie.jpg",
                    "https://www.youtube.com/watch?v=PBmD5emE21c",
                    "Crime, Drama",
                    2014,
                    "Robert Downey Jr., Robert Duvall, Vera Farmiga")

mrs_doubtfire = Movie("Mrs Doubtfire",
                    "After a bitter divorce, an actor disguises himself as a female housekeeper to spend time with his children held in custody by his former wife.",
                    "http://trinityhospice.org.uk/sites/default/files/Mrs-Doubtfire.jpg",
                    "https://www.youtube.com/watch?v=RzZsdL-EGwg",
                    "Comedy, Drama, Family",
                    1993,
                    "Robin Williams, Sally Field, Pierce Brosnan")

the_dinner_Game = Movie("The Dinner Game",
                    "To amuse themselves at a weekly dinner, a few well-heeled folk each bring a dimwit along who is to talk about his pastime.",
                    "https://www.bathstudent.com/pageassets/socs/societies/frenchsoc/activits/Filmnights/diner-de-cons.jpg",
                    "https://www.youtube.com/watch?v=4FANGIUNbiA",
                    "Comedy",
                    1998,
                    "Thierry Lhermitte, Jacques Villeret, Francis Huster")


movies = [toy_story, avatar, invictus, the_judge, mrs_doubtfire, the_dinner_Game]
fresh_tomatoes.open_movies_page(movies)


