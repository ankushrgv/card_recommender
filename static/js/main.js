$(document).on('ready', function(){

	$('img').each(function(){
		card_id = $(this).data("card-id");
		img_url = "{% static " + "'images/" + card_id + ".jpg' %}";
		console.log(img_url);
		// $(this).attr('src',img_url);
	})

});