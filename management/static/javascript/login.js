function loginvalidation(){
	var email=document.getElementById("email");
	var pwd=document.getElementById("pwd");
	if(email.value.trim()==""){
		email.style.border="solid 1px red"; 	
		document.getElementById("lblemail").style.visibility="visible";
	}
	if(pwd.value.trim()==""){
		pwd.style.border="solid 1px red";
		document.getElementById("lblpwd").style.visibility="visible";
		return false;
	}
	else if (pwd.value.trim().length<5){
		pwd.style.border="soild 1px red";
		document.getElementById("lblpwd	").style.visibility="visible";
		return false;
	}
	return false;
}
	
	