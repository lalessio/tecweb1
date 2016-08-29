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

if($auth eq "checksession")
{
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
		 <link rel=\"stylesheet\" href=\"../css/style.css\" type=\"text/css\" media=\"screen\"/>
		 <link rel=\"stylesheet\" href=\"../css/styleprint.css\" type=\"text/css\" media=\"print\"/>
		<script type=\"text/javascript\" src=\"../js/form.js\"></script>
		<script type=\"text/javascript\" src=\"../js/form2.js\"></script>
		<script type=\"text/javascript\" src=\"../js/form3.js\"></script>
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

		<div class=\"nav\">Ti trovi qui: <a href=\"../index.html\"><span lang=\"en\">Home</span></a> &gt; &gt; Area amministratore</div>

		<div class=\"contenuto\" id=\"contenuto\">
		
		<div id=\"form123\">
		<h1 class=\"titolo_testo\">Per eliminare una notizia bisogna accedere alla pagina  <a href=\"news.cgi\">Archivio News</a>  e premere il pulsante \"elimina\" accanto ad ogni notizia</h1>
		<div class=\"form12\">
		<div class=\"form1\">
		<form  method=\"post\" action=\"change_prezzo.cgi\" onsubmit=\"return price_check()\">
				<h1 class=\"blocco1\">Modifica prezzo</h1>
				<p>Inserire un prezzo compreso tra € 5 ed € 30</p>
				<fieldset class=\"informazioni\">
					<p><label>Seleziona tipo prezzo:</label>
						  <select  name=\"price\" title=\"price\">	
						  <option value=\"intero\">intero</option> 
						  <option value=\"ridotto ragazzi (sotto 12 anni)\">ridotto ragazzi (sotto 12 anni)</option>
						  <option value=\"ridotto anziani (sopra 65 anni)\">ridotto anziani (sopra 65 anni)</option>
					</select></p>

				<p><label>Seleziona periodo:</label>
						  <select  name=\"period\" title=\"period\">	
						  <option value=\"primaveraautunno\">Primavera - Autunno</option> 
						  <option value=\"estate\">Estate</option>
					</select></p>


					<p><label>Modifica Prezzo: <span id=\"errore_prezzo2\"></span></label>
					<input type=\"text\" id=\"new_price\" name=\"new_price\" title=\"Modifica prezzo\"/></p>
				
				</fieldset>
				<fieldset class=\"conferma\">
				
					<label for=\"Modificaprezzo\">Modifica:</label>
					<input type=\"submit\" id=\"Modificaprezzo\" value=\"Modifica\" title=\"Modifica prezzo\"/>
					
					<label for=\"Azzeraprezzo\">Azzera:</label>
					<input type=\"reset\" id=\"Azzeraprezzo\" value=\"Azzera\" title=\"Azzera campi\"/>
					
				</fieldset>
				
			</form>
			</div>
		
			<div class=\"form2\">
			<form method=\"post\" action=\"change_orario.cgi\" onsubmit=\"return orario_check()\">
				<h1 class=\"blocco1\">Modifica orario</h1>
				<p>Inserire un  orario nel formato  XX:YY-ZZ:KK</p>
				<fieldset class=\"informazioni\">
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

					<p><label>Modifica Orario: <span id=\"errore_orario\"></span></label>
					<input type=\"text\" id=\"new_hour\" name=\"new_hour\" title=\"Modifica orario\"/></p>
				
				</fieldset>
				<fieldset class=\"conferma\">
				
					<label for=\"Modificaorario\">Modifica:</label>
					<input type=\"submit\" id=\"Modificaorario\" value=\"Modifica\" title=\"Modifica orario\"/>
					
					<label for=\"Azzeraorario\">Azzera:</label>
					<input type=\"reset\" id=\"Azzeraorario\" value=\"Azzera\" title=\"Azzera orario\"/>
					
				</fieldset>
				
			</form>
			</div>
			</div>
		<div  class=\"form3\">
		<form method=\"post\" action=\"nuova_notizia.cgi\" enctype=\"multipart/form-data\" onsubmit=\"return notizia_check()\">

			<h1 class=\"blocco1\">Inserisci nuova notizia</h1>
			<p>Inserire una immagine che abbia una dimensione non superiore a 1Mega<span lang=\"eng\">byte</span></p>
			<p>non vi e' la possibilita' di inserire una notizia senza testo o titolo. <span>Tutti i campi devono essere compilati</span></p>
			<fieldset class=\"informazioni\">

					<p><label for=\"new_title\">Titolo: <span id=\"errore_notizia1\"></span></label>
					<input type=\"text\" id=\"new_title\" name=\"new_title\" title=\"Titolo notizia\"/></p>

				
					<p><label for=\"new_content\">Testo: <span id=\"errore_notizia2\"></span></label>
					<textarea  rows=\"20\" cols=\"60\" id=\"new_content\" name=\"new_content\" title=\"Testo notizias\"></textarea></p>


					<p><label for=\"new_image\">Carica un'immagine:</label>
					<input type=\"file\" id=\"new_image\" name=\"new_image\" title=\"Carica immagine\"/></p>
		

			</fieldset>
			<fieldset class=\"conferma\">


					<label for=\"Invianotizia\">Invia:</label><input type=\"submit\" name=\"submit\" id=\"Invianotizia\" value=\"Invia\" title=\"Invia notizia\"/>

					<label for=\"Azzeranotizia\">Azzera:</label>
					<input type=\"reset\" id=\"Azzeranotizia\" value=\"Azzera\" title=\"Azzera notizia\"/>
				
			</fieldset>
			</form>
			</div>
			</div>



		</div>
		<div class=\"footer\">
		<a href=\"#menu\"><span id=\"up\">TORNA ALL'INIZIO</span></a>
		 <img class=\"valido\" alt=\"css valido\" src=\"../images/css.png\"/>
		 <div class=\"indirizzo\"> Via Nazionale, 22 38085  Bolzano (TN)</div>
		 <a href=\"logout.cgi\"><button type=\"submit\" name=\"delete\"><span xml:lang=\"en\">Logout</span></button></a>
		<img class=\"valido\" alt=\"xhtml valido\" src=\"../images/xhtml.png\"/></div>

	</body>
</html>
";
}else{

print "Content-type:text/html\n\n";

print <<EOF;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
		<title>Errore - Parco Naturale Monte Verde</title>
		<meta name="title" content="Errore - Parco Naturale Monte Verde"/>
		<meta name="description" content="Errore - Parco Naturale Monte Verde"/>
		<meta name="keywords" content="parco naturale, animali, flora,fauna"/>
		<meta name="language" content="italian it"/>
		<meta name="author" content="Carlo Sindico , Luca Alessio"/>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
		<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
		<link rel="stylesheet" href="../css/style.css" type="text/css" media="screen"/>
        <link rel="stylesheet" href="../css/styleprint.css" type="text/css" media="print"/>

	</head>
	<body>
<div><a class=\"salta\" href=\"#contenuto\"><span>Salta al contenuto</span></a></div>
		<div><a href="../index.html"><img class="logo" alt="logo del parco" src="../images/logo.jpg"/></a></div> 
		<div class="titolo"><a href="../index.html">Parco Naturale</a></div><div class="sottotitolo"><a href="../index.html">Monte Verde</a></div>
	
		<div id="menu">
			<ul class="lista">
				<li><a href="../index.html"><span lang="en">HOME</span></a></li>
				<li><a href="../chisiamo.html">CHI SIAMO</a></li>
				<li><a href="../naturaterritorio.html">NATURA E TERRITORIO</a></li>
				<li><a href="newsattivita.cgi"><span lang="en">NEWS</span> E ATTIVITA'</a></li>
				<li><a href="orarieprezzi.cgi">ORARI E PREZZI</a></li>
				<li><a href="../infocontatti.html">INFO E CONTATTI</a></li>
			</ul>
		</div>

		<div class="nav">Ti trovi qui: <a href="../index.html"><span lang="en">Home</span></a> &gt; &gt; Errore</div>

		<div class="contenuto" id=\"contenuto\">	
		<h1 class="blocco1">Errore</h1>
		<p><span lang="en">Login</span> non avvenuto, devi eseguire il login prima di accedere all'area amministratore <a href="adminlogin.cgi"><span lang="en">Login</span></a></p> 
		</div>
		
		<div class="footer">
		<a href="#menu"><span id="up">TORNA ALL'INIZIO</span></a>
		 <img class="valido" alt="css valido" src="../images/css.png"/>

		 <div class="indirizzo"> Via Nazionale, 22 38085  Bolzano (TN)</div>

		<img class="valido" alt="xhtml valido" src="../images/xhtml.png"/></div>

	</body>
</html>
EOF
exit;

}

<!-- Last Update by Carlo 4/08/16 -->