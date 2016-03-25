import movie
import moviecatalog

ddlj = movie.Movie("Dilwale Dulhania Le Jayenge",
                   "Dilwale Dulhania Le Jayenge (English: The Big-Hearted Will Take Away the Bride)," 
                   "also known by the initialism DDLJ, is an Indian romance film written and directed"
                   " by Aditya Chopra and produced by Yash Chopra. Released on 20 October 1995, the film "
                   "stars Shah Rukh Khan and Kajol.",
                   "Shah Rukh Khan, Kajol",
                   "4.3",
                   "https://upload.wikimedia.org/wikipedia/en/thumb/8/80/Dilwale"
                   "_Dulhania_Le_Jayenge_poster.jpg/220px-Dilwale_Dulhania_Le_Jayenge_poster.jpg",
                   "https://www.youtube.com/watch?v=EIKZ7amRGwk")



captain_america = movie.Movie("Captain America: Civil War",
                              "Captain America: Civil War is an upcoming American superhero film featuring the "
                              "Marvel Comics character Captain America, produced by Marvel Studios and distributed "
                              "by Walt Disney Studios Motion Pictures. It is intended to be the sequel to 2011's "
                              "Captain America: The First Avenger and 2014's Captain America: The Winter Soldier, "
                              "and the thirteenth film of the Marvel Cinematic Universe (MCU).",
                              "Chris Evans, Robert Downey, Jr., Scarlett Johansson",
                              "4.5",
                              "https://upload.wikimedia.org/wikipedia/en/thumb/5/53/Captain_"
                              "America_Civil_War_poster.jpg/220px-Captain_America_Civil_War_poster.jpg",
                              "https://www.youtube.com/watch?v=QGfhS1hfTWw")




x_men = movie.Movie("X-Men: Apocalypse",
                    "X-Men: Apocalypse is an upcoming 2016 American superhero film based on the X-Men "
                    "characters that appear in Marvel Comics. It is intended to be the sequel to 2014's "
                    "X-Men: Days of Future Past and the ninth installment in the X-Men film series. "
                    "Directed by Bryan Singer", 
                    "James McAvoy, Michael Fassbender, Jennifer Lawrence",                   
                    "3.9",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/0/04/X-Men"
                    "_-_Apocalypse.jpg/220px-X-Men_-_Apocalypse.jpg",
                    "https://www.youtube.com/watch?v=N0io2w_6vT8")



walk_to_remember = movie.Movie("A Walk to Remember",
                   "A Walk to Remember is a 2002 American coming-of-age romantic drama film directed by "
                   "Adam Shankman and written by Karen Janszen, based on Nicholas Sparks' 1999 novel of "
                   "the same name. The film stars Shane West, Mandy Moore, Peter Coyote, and Daryl Hannah, "
                   "and was produced by Denise Di Novi and Hunt Lowry for Warner Bros.",
                   "Shane West, Mandy Moore, Peter Coyote, Daryl Hannah",
                   "4.9",
                   "https://upload.wikimedia.org/wikipedia/en/thumb/d/dc/A_Walk_to_Remember_"
                   "Poster.jpg/220px-A_Walk_to_Remember_Poster.jpg",
                   "https://www.youtube.com/watch?v=i72wRvPw_ik")




Forrest_Gump = movie.Movie("Forrest Gump",
                           "The story depicts several decades in the life of Forrest Gump, a slow-witted and naive, "
                           "but good-hearted and athletically prodigious man from Alabama who witnesses, and in some "
                           "cases influences, some of the defining events of the latter half of the 20th century in "
                           "the United States; more specifically, the period between Forrest's birth in 1944 and 1982.",
                           "Tom Hanks, Robin Wright, Gary Sinise",
                           "5.0",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/6/67/Forrest_"
                           "Gump_poster.jpg/220px-Forrest_Gump_poster.jpg",
                           "https://www.youtube.com/watch?v=eYSnxZKTZzU")





The_Breakfast_Club = movie.Movie("The Breakfast Club",
                    " The storyline follows five teenagers, each a member of a different high school clique, "
                    "who spend a Saturday in detention together and come to realize that they are all more than "
                    "their respective stereotypes, while facing a strict disciplinarian principal.",                    
                    "Emilio Estevez, Paul Gleason, Anthony Michael Hall",
                    "5.0",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/5/50/The_Breakfast_"
                    "Club.jpg/220px-The_Breakfast_Club.jpg",
                    "https://www.youtube.com/watch?v=BSXBvor47Zs")




passlist = [ddlj,captain_america,x_men,walk_to_remember,Forrest_Gump,The_Breakfast_Club]




moviecatalog.generate_html_page(passlist)
