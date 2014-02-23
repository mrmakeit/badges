var showLogin = function(){
	var box = document.getElementById('signin-box')
	if(box.classList.contains('show')){
		document.getElementById('signin-box').classList.remove('show')
	}else{
		document.getElementById('signin-box').classList.add('show')
	}
}
