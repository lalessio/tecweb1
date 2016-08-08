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

my $cgi = CGI->new();
my $i=$cgi->param('i');
my $limit=$i+4; #mostrerò le prime 4

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
		 <link rel=\"stylesheet\" href=\"../css/styleprova.css\" type=\"text/css\" media=\"screen\"/>
	</head>
	<body>
	<div><a class=\"salta\" href=\"#contenuto\"><span>Salta al contenuto</span></a></div>
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
		
		<div class=\"nav\">Ti trovi qui: <a href=\"../index.html\"><span lang=\"en\">Home</span></a> &gt;&gt; <a href=\"newsattivita.cgi\"><span lang=\"en\">News</span> e Attivita'</a> &gt;&gt; Archivio News</div>

		<div class=\"contenuto\" id=\"contenuto\">
			<h1 class=\"titolo_testo\">Archivio <span lang=\"en\">News</span></h1>
";

my @notizie = $doc->findnodes("/news/notizia");
@notizie = reverse(@notizie); #ribalto così mi mostra le notizie dalla più recente
my $arraysize = @notizie;

for (; $i<$limit and $i<$arraysize; $i=$i+1)
{
	my $notizia=$notizie[$i];
	my $title = $notizia->findvalue('titolo');
	my $date = $notizia->findvalue('data');
	my $text = $notizia->findvalue('contenuto');
	$text = substr($text,0,100);
	my $image = $notizia->findvalue('img');
    my $id = $notizia->getAttribute('ID');
    decode_entities($title);
    decode_entities($text);
	print "<div class=\"bloccosingolonew\">
				<p><strong>$title</strong></p>
				<p>$date</p>
				<img id=\"fotonews\" src=\"../images/$image\" alt=\"$title\"/> 
				<p>$text...</p>
				<a href=\"notizia.cgi?request=$id\">Continua a leggere</a>
			";
	if($auth eq "checksession")
	{
		print " <p><a href=\"delete_notizia.cgi?ID=$id\"><input type=\"submit\" value=\"ELIMINA\"></input></a></p>";
	}
	print "</div>";
}

if($limit<$arraysize)
{
	print"<p><a href=\"news.cgi?i=$limit\">Carica altre notizie</a></p>";
}

if($auth ne "checksession")
{
print"</div></div>
	<div class=\"footer\">
		<a href=\"#menu\"><span id=\"up\">TORNA ALL'INIZIO</span></a>
		 <img class=\"valido\" alt=\"css valido\" src=\"../images/css.png\"/>
		 <div class=\"indirizzo\"> Via Nazionale, 22 38085  Bolzano (TN)</div>
		 <a href=\"adminlogin.cgi\"> Area amministratore</a>
		<img class=\"valido\" alt=\"xhtml valido\" src=\"../images/xhtml.png\"/></div>
	</body>
	</html>
";
}else
{
	print"</div></div>
	<div class=\"footer\">
		<a href=\"#menu\"><span id=\"up\">TORNA ALL'INIZIO</span></a>     
		 <img class=\"valido\" alt=\"css valido\" src=\"../images/css.png\"/>
		 <a href=\"logout.cgi\"><button type=\"submit\" name=\"delete\"><span xml:lang=\"en\">Logout</span></button></a>
		 <div class=\"indirizzo\"> Via Nazionale, 22 38085  Bolzano (TN)</div>
		<img class=\"valido\" alt=\"xhtml valido\" src=\"../images/xhtml.png\"/></div>
	</body>
	</html>
";
}

#Last update by Luca 03/08/2016
