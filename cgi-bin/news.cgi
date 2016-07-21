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
#servirà ancora auth?
#my $auth = $session->param('auth');
my $file = "../data/newsparco.xml";
my $parser = XML::LibXML->new();
my $doc = $parser->parse_file($file);

print "Content-type:text/html\n\n";
print "
<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\"
        \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">
<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"it\" lang=\"it\">
	<head>
		<title>Archivio News - Parco Naturale Monte Verde</title>
		<meta name=\"title\" content=\"Archivio News - Parco Naturale Monte Verde\"/>
		<meta name=\"description\" content=\"Archivio News - Parco Naturale Monte Verde\"/>
		<meta name=\"keywords\" content=\"parco naturale, animali, flora,fauna\"/>
		<meta name=\"language\" content=\"italian it\"/>
		<meta name=\"author\" content=\"Carlo Sindico , Luca Alessio\"/>
		<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/>
		<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"/>
		 <link rel=\"stylesheet\" href=\"css/styleprova.css\" type=\"text/css\" media=\"screen\"/>
	</head>
	<body>
		<div><a href=\"home.html\"><img class=\"logo\" alt=\"logo\" src=\"images/logo.jpg\"/></a></div> 
		<div class=\"titolo\"><a href=\"index.html\">Parco Naturale</a></div><div class=\"sottotitolo\"><a href=\"index.html\">Monte Verde</a></div>
		<div id=\"menu\">
			<ul class=\"lista\">
				<li><a href=\"index.html\"><span lang=\"en\">HOME</span></a></li>
				<li><a href=\"chisiamo.html\">CHI SIAMO</a></li>
				<li><a href=\"naturaterritorio.html\">NATURA E TERRITORIO</a></li>
				<li><a href=\"newsattivita.html\"><span lang=\"en\">NEWS</span> E ATTIVITÀ</a></li>
				<li><a href=\"orariprezzi.html\">ORARI E PREZZI</a></li>
				<li><a href=\"infocontatti.html\">INFO E CONTATTI</a></li>
			</ul>
		</div>
		
		<div class=\"nav\">Ti trovi qui: <a href=\"index.html\"><span lang=\"en\">Home</span></a> &gt;&gt; <a href=\"newsattivita.html\"><span lang=\"en\">News</span> e Attività</a> &gt;&gt; Archivio News</div>

		<div class=\"contenuto\">
			<h1 class=\"titolo_testo\">Archivio <span lang=\"en\">News</span></h1>
";
#attenzione che per adesso estraggo e mostro tutte quante le notizie in una sola pagina (sarà da inserire un limite es. 10 e poi mostrarle in una nuova pagina)

my @notizie = $doc->findnodes("/news/notizia");
foreach my $notizia (@notizie)
{
	my $title = decode_entities($notizia->findvalue('titolo'));
	my $date = $notizia->findvalue('data');
	my $text = decode_entities($notizia->findvalue('contenuto'));
	$text = substr($text,0,100);
	my $image = decode_entities($notizia->findvalue('img'));
    my $id = $notizia->getAttribute('ID');
	#il motivo per cui estraggo ID è perchè magari in questa pagina mostriamo solo una anteprima di x caratteri del testo e poi ci mettiamo
	#un continua a leggere che porta a un page_template per le new in cui l'utente può leggere tutto il testo (di questa cosa ne parleremo)
	print "
			<div>	<!-- div box notizia o qualcosa del genere per separarle meglio -->
				<span><strong>$title</strong></span>
				<span >$date</span>
				<img src=\"../$image\" alt=\"immagine pertinente alla notizia\"/> <!-- questa va messa dentro un div -->
				<p>$text...</p>
				<a href=\"notizia.cgi?request=$id\">Continua a leggere</a>	
			</div>";
}

print"</div>
	<div class=\"footer\">
		<a href=\"#menu\"><span id=\"up\">TORNA ALL'INIZIO</span></a>
		 <img class=\"valido\" alt=\"css valido\" src=\"images/css.png\"/>
		 <div class=\"indirizzo\"> Via Nazionale, 22 38085  Bolzano (TN)</div>
		<img class=\"valido\" alt=\"xhtml valido\" src=\"images/xhtml.png\"/></div>
	</body>
	</html>
";

#Last update by Luca 21/07/2016
