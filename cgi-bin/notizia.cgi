#!/usr/bin/perl -w

use strict;
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use XML::LibXML;
use File::Copy;
use HTML::Entities;
use utf8;
use URI;

my $cgi = new CGI;
my $request = $cgi->param('request');
my $session = CGI::Session->load() or die $!;
my $auth = $session->param('auth');

my $file ="../data/newsparco.xml";
my $parser = XML::LibXML->new();
my $doc = $parser->parse_file($file);

my $notizia = $doc->findnodes("/news/notizia[\@\ID = $request]")->get_node(1);
my $title = decode_entities($notizia->findvalue('titolo'));
my $date = $notizia->findvalue('data');
my $text = decode_entities($notizia->findvalue('contenuto'));
my $image = decode_entities($notizia->findvalue('img'));
my $id = $notizia->getAttribute('ID');

print "Content-Type: text/html\n\n";

print "
<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\"
        \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">
<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"it\" lang=\"it\">
	<head>
		<title>$title - Parco Naturale Monte Verde</title>
		<meta name=\"title\" content=\"$title - Parco Naturale Monte Verde\"/>
		<meta name=\"description\" content=\"$title - Parco Naturale Monte Verde\"/>
		<meta name=\"keywords\" content=\"parco naturale, animali, flora,fauna\"/>
		<meta name=\"language\" content=\"italian it\"/>
		<meta name=\"author\" content=\"Carlo Sindico , Luca Alessio\"/>
		<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/>
		<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"/>
		 <link rel=\"stylesheet\" href=\"../css/styleprova.css\" type=\"text/css\" media=\"screen\"/>
	</head>
	<body>
		<div><a href=\"../home.html\"><img class=\"logo\" alt=\"logo\" src=\"../images/logo.jpg\"/></a></div> 
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
		
		<div class=\"nav\">Ti trovi qui: <a href=\"../index.html\"><span lang=\"en\">Home</span></a> &gt;&gt; <a href=\"../newsattivita.html\"><span lang=\"en\">News</span> e Attività</a> &gt;&gt; <a href=\"news.cgi\">Archivio News</a> &gt;&gt; $title</div>

		<div class=\"contenuto\">
			<h1 class=\"titolo_testo\">$title</h1>";
			
			if($auth eq "amministratoreautenticato")
			{
				print "<a href=\"delete_notizia.cgi?to_delete=$id\"><input type=\"submit\" value=\"ELIMINA\"></input></a>";
			}
	
			print "
			<p>$date</p>
			<img src=\"../images/$image\" alt=\"$title\"/> 
			<p>$text</p>
		</div>
		
		<div class=\"footer\">
		<a href=\"#menu\"><span id=\"up\">TORNA ALL'INIZIO</span></a>
		 <img class=\"valido\" alt=\"css valido\" src=\"../images/css.png\"/>
		 <div class=\"indirizzo\"> Via Nazionale, 22 38085  Bolzano (TN)</div>
		<img class=\"valido\" alt=\"xhtml valido\" src=\"../images/xhtml.png\"/></div>
	</body>
	</html>
";

#Last Update by Luca 28/07/2016
