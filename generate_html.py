import os
import webbrowser

header = """<!DOCTYPE html>
<html>
<head>
	<title>OctoMovieCatalog</title>
	<link rel="stylesheet" type="text/css" href="css/style.css">
</head>
"""

body_part_one = """<body>
<header>
		<h2>Octo Movie Catalog</h2>
	</header>
	<section class="section">
		<section class="inside">
			{publish_article}
		</section>
	</section>"""

body_part_two = """
	<section class="pull-out">
		{show_full_content}
	</section>
<script type="text/javascript" src="js/jquery-1.9.1.min.js"></script>
<script type="text/javascript" src="js/script.js"></script>
</body>
"""

footer = """</html>"""

generate_full_content = """
<div class="movie" id="{i}yt">
			<div class="cross" id="{i}"></div>
			<div class="upper-part">
				<div class="image-part">
					<img src="{poster_url}">
				</div>
				<div class="content-part">
					<h2>{title_name}</h2>
					<h3>Rating : &nbsp; {rating}/5</h3> 
					<p> <b>Storyline : </b>
						{storyline}
					</p>
				</div>
			</div>

			<!-- will work on this later -->
			<div class="lower-part">
				<video id="{i}pauseit" src="{youtube_trailer_link}" controls></video>
			</div>
		</div>
"""

need_to_publish_articles = """<article id="{i}">
	<img src="{image_link}">	
	<div class="title-name">{title_name}</div>
</article>"""


def create_article(movies) :
	generated_article = ""
	cnt = 1
	for movie in movies :
		generated_article += need_to_publish_articles.format(
			i = cnt,
			title_name = movie.title,
			image_link = movie.poster_image_url
			)
		cnt+=1
	return generated_article

def create_full_content(movies) :
	generated_content = ""
	cnt = 1
	for movie in movies :
		generated_content += generate_full_content.format(
			i = cnt,
			poster_url = movie.poster_image_url,
			title_name = movie.title,
			rating = movie.rating,
			storyline = movie.storyline,
			youtube_trailer_link = movie.trailer_youtube_url
			)
		cnt+=1
	return generated_content

def generate_html_page(movies) :
	#open the file which is to modify or if not present create one
	file_open = open("index.html",'w')

	body_part_one_clone = body_part_one.format(publish_article = create_article(movies))

	#
	#create body part two clone, so as to generate html
	body_part_two_clone = body_part_two.format(show_full_content = create_full_content(movies))
	#
	#

	#copy the content in the index file using defined "write()" function
	file_open.write(header + body_part_one_clone + body_part_two_clone + footer)

	#In the end close the file, using the defined "close()" function
	file_open.close()

	#Try opening the file using "webbrowser" module
	url = os.path.abspath(file_open.name)
	webbrowser.open("file://"+ url)
