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
my $title =$notizia->findvalue('titolo');
my $date = $notizia->findvalue('data');
my $text = $notizia->findvalue('contenuto');
my $image = $notizia->findvalue('img');
 my $id = $notizia->getAttribute('ID');


decode_entities($title);
decode_entities($text);

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
		 <link rel=\"stylesheet\" href=\"../css/style.css\" type=\"text/css\" media=\"screen\"/>
		 <link rel=\"stylesheet\" href=\"../css/styleprint.css\" type=\"text/css\" media=\"print\"/>
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
		
		<div class=\"nav\">Ti trovi qui: <a href=\"../index.html\"><span lang=\"en\">Home</span></a> &gt;&gt; <a href=\"newsattivita.cgi\"><span lang=\"en\">News</span> e Attivita'</a> &gt;&gt; <a href=\"news.cgi\">Archivio News</a> &gt;&gt; $title</div>


		<div class=\"contenuto\" id=\"contenuto\">
			<div class=\"blocconews\">
			<h1 class=\"titolo_testo\">$title</h1>";
			if($auth eq "checksession"){
		
                         print "<a href=\"delete_notizia.cgi?ID=$id\"><input type=\"submit\" value=\"ELIMINA\"></input></a>";
				}
			print "<p>$date</p>
			<img class=\"fotonews\" src=\"../images/$image\" alt=\"$title\"/> 
			<p>$text</p>";
				
	if($auth eq "checksession")
	{	print"	</div>
		</div> 	
<div class=\"footer\">
		<a href=\"#menu\"><span id=\"up\">TORNA ALL'INIZIO</span></a>
		 <img class=\"valido\" alt=\"css valido\" src=\"../images/css.png\"/>
		 <div class=\"indirizzo\"> Via Nazionale, 22 38085  Bolzano (TN)</div>
		 <div class=\"indirizzo\"><a href=\"logout.cgi\"><button type=\"submit\" name=\"delete\"><span xml:lang=\"en\">Logout</span></button></a></div>
		 <div class=\"indirizzo\"><a href=\"adminarea.cgi\">TORNA AD ADMIN AREA</a></div>
		<img class=\"valido\" alt=\"xhtml valido\" src=\"../images/xhtml.png\"/></div>
	</body>
	</html>
";
} else
{
	print"	</div>
		</div> 	
<div class=\"footer\">
		<a href=\"#menu\"><span id=\"up\">TORNA ALL'INIZIO</span></a> 
		 <img class=\"valido\" alt=\"css valido\" src=\"../images/css.png\"/>
		<div class=\"indirizzo\"> Via Nazionale, 22 38085  Bolzano (TN)</div>
		  <div class=\"indirizzo\"><a href=\"adminlogin.cgi\">AREA AMMINISTRATORE</a></div>
		<img class=\"valido\" alt=\"xhtml valido\" src=\"../images/xhtml.png\"/></div>
	</body>
	</html>
";
}

#Last Update by Carlo 22/07/2016