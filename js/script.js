$(document).ready(function(){
	var block = $('.pull-out'); 
	var inside = $('.inside');
	$('article').click(function(){
		block.toggleClass('show')
		inside.toggleClass('control');
		var name = this.id;
		name = '#'+name+'yt';
		$(name).toggleClass('hide');
	})
	$('.cross').click(function(){
		block.toggleClass('show')
		inside.toggleClass('control');
  		var videoElem = this.id;
  		videoElem = videoElem + "pauseit";
  		console.log(videoElem);
  		var pauseit = document.getElementById(videoElem);
    	pauseit.pause();
    	$('.movie').removeClass('hide');
	})
});