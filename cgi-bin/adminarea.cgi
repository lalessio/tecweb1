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

#e l'auth?

print "Content-type:text/html\n\n";
print "
<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">
<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"it\" lang=\"it\">
	<head>
		<title>Area amministratore - Parco Naturale Monte Verde</title>
		<meta name=\"title\" content=\"area amministratore - Parco Naturale Monte Verde\"/>
		<meta name=\"description\" content=\"area amministratore - Parco Naturale Monte Verde\"/>
		<meta name=\"keywords\" content=\"parco naturale, animali, flora,fauna\"/>
		<meta name=\"language\" content=\"italian it\"/>
		<meta name=\"author\" content=\"Carlo Sindico , Luca Alessio\"/>
		<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/>
		<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"/>
		 <link rel=\"stylesheet\" href=\"../css/styleprova.css\" type=\"text/css\" media=\"screen\"/>
	</head>
	<body>
		<div><a href=\"../index.html\"><img class=\"logo\" alt=\"logo\" src=\"../images/logo.jpg\"/></a></div> 
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

		<div class=\"nav\">Ti trovi qui: <a href=\"../index.html\"><span lang=\"en\">Home</span></a> &gt; &gt;<a href=\"adminlogin.cgi\">Admin amministratore</a> &gt; &gt; Area amministratore</div>

		<div class=\"contenuto\">
		
		<form id=\"form\" method=\"post\" action=\"change_prezzo.cgi\">
				<h1 class=\"blocco1\">Modifica prezzo</h1>
				<p>Inserire un prezzo non negativo intero</p>
				<fieldset id=\"informazioni\">
					<p><label>Seleziona tipo prezzo:</label>
						  <select  name=\"price\" title=\"price\">	
						  <option value=\"intero\">intero</option> 
						  <option value=\"ridotto ragazzi (sotto 12 anni)\">ridotto ragazzi (sotto 12 anni)</option>
						  <option value=\"ridotto anziani (sopra 65 anni)\">ridotto anziani (sopra 65 anni)</option>
					</select></p>

					<p><label>Modifica Prezzo (Primavera/Autunno):</label>
					<input type=\"text\" id=\"new_pricePA\" name=\"new_pricePA\"/></p>
					
					<p><label>Modifica Prezzo (Estate):</label>
					<input type=\"text\" id=\"new_priceE\" name=\"new_priceE\"/></p>
				
				</fieldset>
				<fieldset id=\"conferma\">
				
					<label for=\"modifica\"></label>
					<input type=\"submit\" id=\"modifica\" value=\"Modifica\">
										
				</fieldset>
				
			</form>
		
			
			<form id=\"form\" method=\"post\" action=\"change_orario.cgi\">
				<h1 class=\"blocco1\">Modifica orario</h1>
				<p>Inserire un  orario nel formato  XX:YY-ZZ:KK</p>
				<fieldset id=\"informazioni\">
					<p><label>Seleziona giorno:</label>
						  <select  name=\"day\" title=\"day\">	
						  <option value=\"Lunedi\">Lunedi'</option> 
						  <option value=\"Martedi\">Martedi'</option>
						  <option value=\"Mercoledi\">Mercoledi'</option>
						  <option value=\"Giovedi\">Giovedi'</option>
						  <option value=\"Venerdi\">Venerdi'</option>
						  <option value=\"Sabato\">Sabato</option>
						  <option value=\"Domenica\">Domenica</option>
						  <option value=\"Festivi\">Festivi</option>
					</select></p>

					<p><label>Modifica Orario:</label>
					<input type=\"text\" id=\"new_hour\" name=\"new_hour\"/></p>
				
				</fieldset>
				<fieldset id=\"conferma\">
				
					<label for=\"modifica\"></label>
					<input type=\"submit\" id=\"modifica\" value=\"Modifica\">
					
				</fieldset>
				
			</form>

		<form id=\"form\" method=\"post\" action=\"nuova_notizia.cgi\" enctype=\"multipart/form-data\">

			<h1 class=\"blocco1\">Inserisci nuova notizia</h1>
			<p>Inserire una immagine che abbia una dimensione non superiore a 1Mega<span lang=\"eng\">byte</span></p>
			<p>non vi e' la possibilita' di inserire una notizia senza testo o titolo. <span>Tutti i campi devono essere compilati</span></p>
			<fieldset id=\"informazioni\">
			<p id=\"\"></p>

					<p><label for=\"new_title\">Titolo:</label>
					<input type=\"text\" id=\"new_title\" name=\"new_title\"/></p>
				
					<p><label for=\"new_content\">Testo:</label>
					<textarea rows=\"20\" cols=\"60\" name=\"new_content\" id=\"new_content\"></textarea></p>

					<p><label for=\"new_image\">Carica un'immagine:</label>
					<input type=\"file\" id=\"new_image\" name=\"new_image\"/></p>
		
			</fieldset>
			<fieldset id=\"conferma\">

					<label for=\"invia\"></label><input type=\"submit\" name=\"submit\" id=\"invia\" value=\"Invia\"/>

					<label for=\"azzera\"></label>
					<input type=\"reset\" id=\"azzera\" value=\"Azzera\"/>
				
			</fieldset>
			</form>
					
		<div class=\"footer\">
		<a href=\"#menu\"><span id=\"up\">TORNA ALL'INIZIO</span></a>
		 <img class=\"valido\" alt=\"css valido\" src=\"../images/css.png\"/>
		  <a href=\"logout.cgi\"><button type=\"submit\" name=\"delete\"><span xml:lang=\"en\">Logout</span></button></a>
		 <div class=\"indirizzo\"> Via Nazionale, 22 38085  Bolzano (TN)</div>

		<img class=\"valido\" alt=\"xhtml valido\" src=\"../images/xhtml.png\"/></div>

	</body>
</html>
";

#Last Update by Luca 01/08/16
