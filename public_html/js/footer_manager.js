function manage_footer()
{
    var exist = document.cookie.indexOf("autorizzazione=checksession");
	if(exist == -1)
	{
		document.getElementById("dinamico").innerHTML = "<a href=\"cgi-bin/adminlogin.cgi\"> Area amministratore</a>";
	}
	else
	{
		document.getElementById("dinamico").innerHTML = "<a href=\"cgi-bin/logout.cgi\"><button type=\"submit\" name=\"delete\"><span xml:lang=\"en\">Logout</span></button></a>";
	}	
} 

//Last Update by Luca 11/08/16
