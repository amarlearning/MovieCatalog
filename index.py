import movie
import generate_html

ddlj = movie.Movie("Dilwale Dulhania Le Jayenge",
                   "Love Story of a boy named Raj and girl named simran in europe",
                   1,
                   "img/sh.jpg",
                   "file:///C:/Users/AMAR/Desktop/Freenet/Simranjeet%20Singh%20-%20Vroom%20Vroom%20feat%20Badshah%20_%20Latest%20Punjabi%20Song%202015-ULbgRLSvtHI.mp4")

captain_america = movie.Movie("Captain America: Civil War",
                              "Captain America: Civil War is an upcoming American superhero film featuring the Marvel Comics character Captain America",
                              2,
                              "img/sh.jpg",
                              "file:///C:/Users/AMAR/Desktop/Freenet/Simranjeet%20Singh%20-%20Vroom%20Vroom%20feat%20Badshah%20_%20Latest%20Punjabi%20Song%202015-ULbgRLSvtHI.mp4")


x_men = movie.Movie("X-Men: Apocalypse More words added",
                    "X-Men: Apocalypse is an upcoming 2016 American superhero film based on the X-Men characters that appear in Marvel Comics",                    
                    3,
                    "img/sh.jpg",
                    "file:///C:/Users/AMAR/Desktop/Freenet/Simranjeet%20Singh%20-%20Vroom%20Vroom%20feat%20Badshah%20_%20Latest%20Punjabi%20Song%202015-ULbgRLSvtHI.mp4")

walk_to_remember = movie.Movie("A Walk to Remember",
                   "Landon Carter gets in trouble and has to do community service- including getting involved in the spring play. ",
                   4,
                   "img/sh.jpg",
                   "file:///C:/Users/AMAR/Desktop/Freenet/Simranjeet%20Singh%20-%20Vroom%20Vroom%20feat%20Badshah%20_%20Latest%20Punjabi%20Song%202015-ULbgRLSvtHI.mp4")


Forrest_Gump = movie.Movie("Forrest Gump",
                           "Forrest Gump is a 1994 American epic romantic-comedy-drama film based on the 1986 novel of the same name by Winston Groom.",
                           5,
                           "img/sh.jpg",
                           "file:///C:/Users/AMAR/Desktop/Freenet/Simranjeet%20Singh%20-%20Vroom%20Vroom%20feat%20Badshah%20_%20Latest%20Punjabi%20Song%202015-ULbgRLSvtHI.mp4")


The_Breakfast_Club = movie.Movie("The Breakfast Club",
                    "The Breakfast Club is a 1985 American coming of age comedy-drama film written, produced, and directed by John Hughes",                    
                    1,
                    "img/sh.jpg",
                    "file:///C:/Users/AMAR/Desktop/Freenet/Simranjeet%20Singh%20-%20Vroom%20Vroom%20feat%20Badshah%20_%20Latest%20Punjabi%20Song%202015-ULbgRLSvtHI.mp4")

passlist = [ddlj,captain_america,x_men,walk_to_remember,Forrest_Gump,The_Breakfast_Club]

generate_html.generate_html_page(passlist)
