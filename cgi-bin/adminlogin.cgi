#!/usr/bin/perl -w

use strict;
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use CGI::Cookie;
use XML::LibXML;
use File::Copy;
use File::Basename;
use CGI::Pretty qw(:html3);
use POSIX;
use URI;
use utf8;


my $session = CGI::Session->load() or die $!;


my $auth = $session->param('auth');



if($auth ne "amministratoreautenticato")
	{
print "Content-type:text/html\n\n";
print "

<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">
<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"it\" lang=\"it\">
	<head>
		<title>Admin login - Parco Naturale Monte Verde</title>
		<meta name=\"title\" content=\"Admin login - Parco Naturale Monte Verde\"/>
		<meta name=\"description\" content=\"Admin login - Parco Naturale Monte Verde\"/>
		<meta name=\"keywords\" content=\"parco naturale, animali, flora,fauna\"/>
		<meta name=\"language\" content=\"italian it\"/>
		<meta name=\"author\" content=\"Carlo Sindico , Luca Alessio\"/>
		<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/>
		<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"/>
		<link rel=\"stylesheet\" href=\"../css/styleprova.css\" type=\"text/css\" media=\"screen\"/>
		<script type=\"text/javascript\" src=\"../js/amministratore.js\"></script>

	</head>
	<body>
		<div><a href=\"index.html\"><img class=\"logo\" alt=\"logo\" src=\"../images/logo.jpg\"/></a></div> 
		<div class=\"titolo\"><a href=\"../index.html\">Parco Naturale</a></div><div class=\"sottotitolo\"><a href=\"../index.html\">Monte Verde</a></div>
		<div id=\"menu\">
			<ul class=\"lista\">
				<li><a href=\"../index.html\"><span lang=\"en\">HOME</span></a></li>
				<li><a href=\"../chisiamo.html\">CHI SIAMO</a></li>
				<li><a href=\"../naturaterritorio.html\">NATURA E TERRITORIO</a></li>
				<li><a href=\"newsattivita.cgi\"><span lang=\"en\">NEWS</span> E ATTIVITÀ</a></li>
				<li><a href=\"orarieprezzi.cgi\">ORARI E PREZZI</a></li>
				<li><a href=\"../infocontatti.html\">INFO E CONTATTI</a></li>
			</ul>
		</div>

		<div class=\"nav\">Ti trovi qui: <a href=\"../index.html\"><span lang=\"en\">Home</span></a> &gt; &gt; Admin amministratore</div>

		<div class=\"contenuto\">	

			<form id=\"form\" method=\"post\" onsubmit=\"return login_check()\" action=\"controllologin.cgi\">

			<h1>Login</h1>
			<fieldset id=\"informazioni\">
			<p id=\"errore\"></p>

					<p><label for=\"user_name\"><span lang=\"en\">Username:</span></label>
					<input type=\"text\" id=\"user_name\" name=\"user_name\"/></p>

				
					<p><label for=\"user_pwd\"><span lang=\"en\">Password:</span></label>
					<input type=\"password\" id=\"user_pwd\" name=\"user_pwd\"/></p>
				
			</fieldset>
			<fieldset id=\"conferma\">


					<label for=\"invia\"></label><input type=\"submit\" name=\"submit\" id=\"invia\" value=\"Invia\"/>

					<label for=\"azzera\"></label>
					<input type=\"reset\" id=\"azzera\" value=\"Azzera\"/>
				
			</fieldset>
			</form>
		</div>
		
		<div class=\"footer\">
		<a href=\"#menu\"><span id=\"up\">TORNA ALL'INIZIO</span></a>
		 <img class=\"valido\" alt=\"css valido\" src=\"../images/css.png\"/>

		 <div class=\"indirizzo\"> Via Nazionale, 22 38085  Bolzano (TN)</div>

		<img class=\"valido\" alt=\"xhtml valido\" src=\"../images/xhtml.png\"/></div>

	</body>
</html>
";
}

else {
	print "Content-type:text/html\n\n";
			print "<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">
			<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"it\" lang=\"it\"> 
			<head>
			<title>Controllo login</title>
			<meta name=\"title\" content=\"Redirect\"/>
			<meta http-equiv=\"refresh\"
			content=\"0; url=adminarea.cgi\"/>
			</head>
			<body>
			</body>
			</html>"; 
}

# Last Update by Carlo 01/08/16
