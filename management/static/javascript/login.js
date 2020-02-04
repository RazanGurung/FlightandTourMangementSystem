function loginvalidation() {
	var email = document.getElementById("email");
	var pwd = document.getElementById("pwd");
	if(email.value.trim()==""){
		email.style.border="solid 1px red"; 	
		document.getElementById("emaillbl").style.visibility="visible";
	}
	if(pwd.value.trim()==""){
		pwd.style.border="solid 1px red";
		document.getElementById("pwdlbl").style.visibility="visible";
		return false;
	}
	else if (pwd.value.trim().length<5){
		pwd.style.border="solid 1px red";
		document.getElementById("pwdlbl").style.visibility="visible";
        return false;
	}
	return false;
}
	
	