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



if($auth ne "checksession")
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
		<meta http-equiv=\"Content-Script-Type\" content=\"text/javascript\"/>
		<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"/>
		<link rel=\"stylesheet\" href=\"../css/style.css\" type=\"text/css\" media=\"screen\"/>
		<link rel=\"stylesheet\" href=\"../css/styleprint.css\" type=\"text/css\" media=\"print\"/>
		<script type=\"text/javascript\" src=\"../js/amministratore.js\"></script>

	</head>
	<body>
<div><a class=\"salta\" href=\"#contenuto\"><span>Salta al contenuto</span></a></div>
		<div><a href=\"../index.html\"><img class=\"logo\" alt=\"logo del parco\" src=\"../images/logo.jpg\"/></a></div> 
		<div class=\"titolo\"><a href=\"../index.html\">Parco Naturale</a></div><div class=\"sottotitolo\"><a href=\"../index.html\">Monte Verde</a></div>
		
		<div id=\"menu\">
			<ul class=\"lista\">
				<li><a href=\"../index.html\"><span lang=\"en\">HOME</span></a></li>
				<li><a href=\"../chisiamo.html\">CHI SIAMO</a></li>
				<li><a href=\"../naturaterritorio.html\">NATURA E TERRITORIO</a></li>
				<li><a href=\"newsattivita.cgi\"><span lang=\"en\">NEWS</span> E ATTIVITA'</a></li>
				<li><a href=\"orarieprezzi.cgi\">ORARI E PREZZI</a></li>
				<li><a href=\"../infocontatti.html\">INFO E CONTATTI</a></li>
			</ul>
		</div>

		<div class=\"nav\">Ti trovi qui: <a href=\"../index.html\"><span lang=\"en\">Home</span></a> &gt; &gt; <span lang=\"en\">Admin</span> amministratore</div>

		<div class=\"contenuto\" id=\"contenuto\">	
            <div class=\"formadmin\">
			<form method=\"post\" onsubmit=\"return login_check()\" action=\"controllologin.cgi\">

			<h1 class=\"blocco1\">Login</h1>
			<fieldset id=\"informazioni\">
			<p id=\"errore\"></p>

					<p><label for=\"user_name\"><span lang=\"en\">Username:</span></label>
					<input type=\"text\" id=\"user_name\" name=\"user_name\" title=\"Inserisci il tuo username qui\"/></p>

				
					<p><label for=\"user_pwd\"><span lang=\"en\">Password:</span></label>
					<input type=\"password\" id=\"user_pwd\" name=\"user_pwd\" title=\"Inserisci la tua password qui\"/></p>
				
			</fieldset>
			<fieldset id=\"conferma\">


					<label for=\"invia\">Invia:</label><input type=\"submit\" name=\"submit\" id=\"invia\" value=\"Invia\" title=\"Invia\"/>

					<label for=\"azzera\">Azzera:</label>
					<input type=\"reset\" id=\"azzera\" value=\"Azzera\" title=\"Azzera\"/>
				
			</fieldset>
			</form>
        </div>
		</div>
		
		<div class=\"footer\">
        <a href=\"../mappasito.html\"><span class=\"up\">MAPPA DEL SITO</span></a>
		<a href=\"#menu\"><span class=\"up\">TORNA ALL'INIZIO</span></a>
		 <img class=\"valido\" alt=\"css valido\" src=\"../images/css.png\"/>

		 <div class=\"indirizzo\"> Via Nazionale, 22 38085  Bolzano (TN)</div>

		<img class=\"valido\" alt=\"xhtml valido\" src=\"../images/xhtml.png\"/></div>

	</body>
</html>
";
}

else {

print "Content-type:text/html\n\n";
print "Location: adminarea.cgi\n\n";
}
<!-- Last Update by Carlo 8/08/16 -->
