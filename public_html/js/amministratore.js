function login_check()
{

	var username = document.getElementById("user_name").value;	
        var password=document.getElementById("user_pwd").value;
        
        if (!username.replace(/^\s+/g, '').length)
        {
           document.getElementById("errore").innerHTML = "il campo username è obligatorio*";
           document.getElementById("user_name").focus();
           return false;
	}
	else 
		if( !password.replace(/^\s+/g, '').length){

			document.getElementById("errore").innerHTML = "il campo password è obligatorio*";
			document.getElementById("user_pwd").focus();
           return false;
		}
		else

	return true;
}
