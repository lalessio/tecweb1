 function manage_footer()
{
    var exist = document.cookie.indexOf("autorizzazione=checksession");
	if(exist == -1)
	{
		document.getElementById("dinamico").innerHTML = "<div class=\"indirizzo\"><a href=\"cgi-bin/adminlogin.cgi\"> Area amministratore</a></div>";
	}
	else
	{
		document.getElementById("dinamico").innerHTML = "<div class=\"indirizzo\"><a href=\"cgi-bin/logout.cgi\"><button type=\"submit\" name=\"delete\"><span xml:lang=\"en\">Logout</span></button></a></div><div class=\"indirizzo\"><a href=\"cgi-bin/adminarea.cgi\">TORNA AD <span lang=\"en\">ADMIN</span>AREA</a></div>";
	}	
} 

//Last Update by Luca 04/08/16