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
use XML::LibXML::NodeList;
use HTML::Parser;
use HTML::Entities;

require ('funzioni.pl');

my $session = CGI::Session->load() or die $!;

my $auth = $session->param('auth');

my $cgi = CGI->new();

my $selected_day = $cgi->param('day');

$selected_day = rimuovi(string($selected_day));

my $new_orario = $cgi->param('new_hour');

$new_orario = rimuovi(string($new_orario));




my $file = "../data/orari.xml";
my $parser = XML::LibXML->new();
my $doc = $parser->parse_file($file);

my $b="fallita";

if($new_orario eq '')
{
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
		<link rel="stylesheet" href="../css/styleprova.css" type="text/css" media="screen"/>

	</head>
	<body>
<div><a class=\"salta\" href=\"#contenuto\"><span>Salta al contenuto</span></a></div>
		<div><a href="index.html"><img class="logo" alt="logo" src="../images/logo.jpg"/></a></div> 
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

		<div class="nav">Ti trovi qui: <a href="../index.html"><span lang="en">Home</span></a> &gt; &gt;<a href="adminarea.cgi"><span lang="en">Admin</span>area</a> &gt; &gt; Errore</div>

		<div class="contenuto" id=\"contenuto\">	
		<h1 class="blocco1">Errore</h1>
		<p>Il campo Modifica Orario non puo' essere vuoto, riprova di nuovo <a href="adminarea.cgi"><span lang="en">Admin</span>area</a></p> 
		</div>
		
		<div class="footer">
		<a href="#menu"><span id="up">TORNA ALL'INIZIO</span></a>
		 <img class="valido" alt="css valido" src="../images/css.png"/>
		 <a href=\"logout.cgi\"><button type=\"submit\" name=\"delete\"><span xml:lang=\"en\">Logout</span></button></a>
		 <a href=\"adminarea.cgi\">TORNA AD ADMIN AREA</a>
		 <div class="indirizzo"> Via Nazionale, 22 38085  Bolzano (TN)</div>

		<img class="valido" alt="xhtml valido" src="../images/xhtml.png"/></div>

	</body>
</html>
EOF
exit;

}


 for my $dacambiare ($doc->findnodes("/orari/giorno[\@\id='$selected_day']/ora/text()"))
	{
		
		$dacambiare->setData($new_orario);
		open(OUT,">$file") or die;
		print OUT $doc->toString;
		close(OUT);	
		$b="buon fine";}



print "Content-type:text/html\n\n";
print <<EOF;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
		<title>Inserimento avvenuto con successo - Parco Naturale Monte Verde</title>
		<meta name="title" content="Inserimento avvenuto con successo - Parco Naturale Monte Verde"/>
		<meta name="description" content="Inserimento avvenuto con successo - Parco Naturale Monte Verde"/>
		<meta name="keywords" content="parco naturale, animali, flora,fauna"/>
		<meta name="language" content="italian it"/>
		<meta name="author" content="Carlo Sindico , Luca Alessio"/>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
		<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
		<link rel="stylesheet" href="../css/styleprova.css" type="text/css" media="screen"/>

	</head>
	<body>
		<div><a href="index.html"><img class="logo" alt="logo" src="../images/logo.jpg"/></a></div> 
		<div class="titolo"><a href="../index.html">Parco Naturale</a></div><div class="sottotitolo"><a href="../index.html">Monte Verde</a></div>
	<div><a class=\"salta\" href=\"#contenuto\"><span>Salta al contenuto</span></a></div>
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

		<div class="nav">Ti trovi qui: <a href="../index.html"><span lang="en">Home</span></a> &gt; &gt;<a href="adminarea.cgi"><span lang="en">Admin</span>area</a> &gt; &gt; Inserimento avvenuto</div>

		<div class="contenuto" id=\"contenuto\">	
		<h1 class="blocco1">Informazioni</h1>
		<p>Inserimento avvenuto con successo,per visualizzare gli orari <a href="orarieprezzi.cgi">Orari e prezzi</a></p> 
		<p>oppure torna indietro <a href="adminarea.cgi"><span lang="en">Admin</span>area</a></p>
		</div>
		
		<div class="footer">
		<a href="#menu"><span id="up">TORNA ALL'INIZIO</span></a>
		 <img class="valido" alt="css valido" src="../images/css.png"/>
		 <a href=\"logout.cgi\"><button type=\"submit\" name=\"delete\"><span xml:lang=\"en\">Logout</span></button></a>
		 <a href=\"adminarea.cgi\">TORNA AD ADMIN AREA</a>
		 <div class="indirizzo"> Via Nazionale, 22 38085  Bolzano (TN)</div>

		<img class="valido" alt="xhtml valido" src="../images/xhtml.png"/></div>

	</body>
</html>
EOF
exit;
		
	
	



