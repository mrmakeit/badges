var getCode = function(){
	var code = document.getElementById('badge_code')
	var url = '/badges/claim/'+code.value
	document.location = url
}
