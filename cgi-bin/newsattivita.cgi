#!/usr/bin/perl -w

use strict;
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use XML::LibXML;
use File::Copy;
use utf8;
use URI;
use HTML::Parser;
use HTML::Entities;

my $session = CGI::Session->load() or die $!;

my $auth = $session->param('auth');
my $file = "../data/newsparco.xml";
my $parser = XML::LibXML->new();
my $doc = $parser->parse_file($file);

print "Content-type:text/html\n\n";
print <<EOF;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
		<title>News e Attivita' - Parco Naturale Monte Verde</title>
		<meta name="title" content="News e Attività - Parco Naturale Monte Verde"/>
		<meta name="description" content="News e Attività - Parco Naturale Monte Verde"/>
		<meta name="keywords" content="parco naturale, animali, flora,fauna"/>
		<meta name="language" content="italian it"/>
		<meta name="author" content="Carlo Sindico , Luca Alessio"/>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
		<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
		 <link rel="stylesheet" href="../css/styleprova.css" type="text/css" media="screen"/>
	</head>
	<body>
<div><a class=\"salta\" href=\"#contenuto\"><span>Salta al contenuto</span></a></div>
		<div><a href="../index.html"><img class="logo" alt="logo" src="../images/logo.jpg"/></a></div> 
		<div class="titolo"><a href="../index.html">Parco Naturale</a></div><div class="sottotitolo"><a href="index.html">Monte Verde</a></div>
	
		<div id="menu">
			<ul class="lista">
				<li><a href="../index.html"><span lang="en">HOME</span></a></li>
				<li><a href="../chisiamo.html">CHI SIAMO</a></li>
				<li><a href="../naturaterritorio.html">NATURA E TERRITORIO</a></li>
				<li class="active"><span lang="en">NEWS</span> E ATTIVITA'</li>
				<li><a href="orarieprezzi.cgi">ORARI E PREZZI</a></li>
				<li><a href="../infocontatti.html">INFO E CONTATTI</a></li>
			</ul>
		</div>
		
		<div class="nav">Ti trovi qui: <a href="../index.html"><span lang="en">Home</span></a> &gt;&gt; <span lang="en">News</span> e Attivita'</div>

		<div class="contenuto" id=\"contenuto\">
			
			<!-- testo contenuto preso da http://www.pnab.it/footer/mappa-del-sito.html-->

			<h1 class="titolo_testo">Attivita'</h1>
			<p>Tra le numerose iniziative, proposte e attività del Parco Naturale Monte Verde vi sono gli ingredienti per una vacanza 				di emozioni, godendo delle peculiarità naturalistiche, della preziosa flora e dell’unicità delle specie animali che, 				grazie all’integrità di questo territorio, hanno trovato l’habitat ideale. 
			Rilassanti passeggiate ed itinerari tra vette innevate, la suggestione autunnale del bramito dei cervi, la quiete e la 				magia dell’inverno nelle escursioni con le ciaspole. Queste sono solamente alcune delle attività proposte dal parco.
			</p><p><a href="../attivita.html">Scopri di più</a></p>

			<h1 class="titolo_testo"><span lang="en">News</span></h1>
			<div class="blocconews">
EOF

for (my $i=0; $i<3; $i=$i+1)
{
	my @notizie = $doc->findnodes("/news/notizia[last()-$i]");
	my $notizia = $notizie[0];
	my $title = $notizia->findvalue('titolo');
	decode_entities($title);
	my $date = $notizia->findvalue('data');	
	my $text = $notizia->findvalue('contenuto');
	decode_entities($text);
	$text = substr($text,0,100);
	my $image = $notizia->findvalue('img');
    my $id = $notizia->getAttribute('ID');
	print "
			<div class=\"bloccosingolonew\">
				<p><strong>$title</strong></p>
				<p>$date</p>
				<img class=\"fotonews\" src=\"../images/$image\" alt=\"$title\"/> 
				<p>$text...</p>
				<a href=\"notizia.cgi?request=$id\">Continua a leggere</a>	
			</div>";
}
if($auth eq "checksession")
{print <<EOF;
		</div><p><a href="news.cgi">Visualizza l'Archivio completo delle News</a></p>
		</div>
		<div class="footer">
		<a href="#menu"><span id="up">TORNA ALL'INIZIO</span></a>
		 <img class="valido" alt="css valido" src="../images/css.png"/>
		 <div class="indirizzo"> Via Nazionale, 22 38085  Bolzano (TN)</div>
		 <div class=\"indirizzo\"><a href=\"logout.cgi\"><button type=\"submit\" name=\"delete\"><span xml:lang=\"en\">Logout</span></button></a></div>
		 <div class=\"indirizzo\"><a href=\"adminarea.cgi\">TORNA AD ADMIN AREA</a></div>
		<img class="valido" alt="xhtml valido" src="../images/xhtml.png"/></div>

	</body>
	</html>
EOF
}
else {
print <<EOF;
		</div><p><a href="news.cgi">Visualizza l'Archivio completo delle News</a></p>
		</div>
		<div class="footer">
		<a href="#menu"><span id="up">TORNA ALL'INIZIO</span></a>
		 <img class="valido" alt="css valido" src="../images/css.png"/>
		 <div class="indirizzo"> Via Nazionale, 22 38085  Bolzano (TN)</div>
		<div class=\"indirizzo\"><a href=\"adminlogin.cgi\">AREA AMMINISTRATORE</a></div>
		<img class="valido" alt="xhtml valido" src="../images/xhtml.png"/></div>

	</body>
	</html>
EOF

}
#Last Update by Carlo 28/07/16
