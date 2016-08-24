 function manage_footer()
{
    var exist = document.cookie.indexOf("autorizzazione=checksession");
	if(exist == -1)
	{
		document.getElementById("dinamico").innerHTML = "<a href=\"cgi-bin/adminlogin.cgi\">Area Amministratore</a>";
	}
	else
	{
		document.getElementById("dinamico").innerHTML = "<a href=\"cgi-bin/logout.cgi\"><button type=\"submit\" name=\"delete\"><span xml:lang=\"en\">Logout</span></button></a> <a href=\"cgi-bin/adminarea.cgi\">Area Amministratore</a>";
	}	
} 

//Last Update by Luca 24/08/16
