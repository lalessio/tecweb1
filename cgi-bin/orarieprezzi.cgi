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

#my $session = CGI::Session->load() or die $!;
#servirà ancora auth?
#my $auth = $session->param('auth');
my $file1 = "../data/orari.xml";
my $parser1 = XML::LibXML->new();
my $doc1 = $parser1->parse_file($file1);
my $file2 = "../data/prezzi.xml";
my $parser2 = XML::LibXML->new();
my $doc2 = $parser2->parse_file($file2);

print "Content-type:text/html\n\n";
print "
<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\"
        \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">
<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"it\" lang=\"it\">
	<head>
		<title>Orari e Prezzi - Parco Naturale Monte Verde</title>
		<meta name=\"title\" content=\"Orari e Prezzi - Parco Naturale Monte Verde\"/>
		<meta name=\"description\" content=\"Orari e Prezzi - Parco Naturale Monte Verde\"/>
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
				<li><a href=\"../newsattivita.html\"><span lang=\"en\">NEWS</span> E ATTIVITA'</a></li>
				<li class=\"active\">ORARI E PREZZI</a></li>
				<li><a href=\"../infocontatti.html\">INFO E CONTATTI</a></li>
			</ul>
		</div>
		
		<div class=\"nav\">Ti trovi qui: <a href=\"../index.html\"><span lang=\"en\">Home</span></a> &gt;&gt; Orari e Prezzi</div>

		<div class=\"contenuto\">
			<h2 class=\"titolo_testo\">Orari</h2>
			<p>Aggiungere paragrafo introduttivo</p>
			<ul>

";

my @orari = $doc1->findnodes("/orari/giorno");
foreach my $orario (@orari)
{
	my $ora = decode_entities($orario->findvalue('ora'));
    my $id = $orario->getAttribute('id');
	print "<li><strong>$id:</strong><span>$ora</span></li>";
}

print"
	</ul>
	<h2 class=\"titolo_testo\">Prezzi</h21>
	<p>Inserire spiegazione prezzi/periodi dell'anno</p>
	<ul>";
	
my @prezzi = $doc2->findnodes("/prezzi/ingresso");
foreach my $prezzo (@prezzi)
{
	my $pa = decode_entities($prezzo->findvalue('primaveraautunno'));
	my $estate = decode_entities($prezzo->findvalue('estate'));
    my $id = $prezzo->getAttribute('id');
	print "<li>
				<span>$id:</span>
				<ul>
					<li><span>Primavera - Autunno: $pa</span></li>
					<li><span>Estate: $estate</span></li>
				</ul>
			</li>";
}	

print"
	</ul>
</div>			
</div>
	<div class=\"footer\">
		<a href=\"#menu\"><span id=\"up\">TORNA ALL'INIZIO</span></a>
		 <img class=\"valido\" alt=\"css valido\" src=\"../images/css.png\"/>
		 <div class=\"indirizzo\"> Via Nazionale, 22 38085  Bolzano (TN)</div>
		<img class=\"valido\" alt=\"xhtml valido\" src=\"../images/xhtml.png\"/></div>
	</body>
	</html>
";

#Last Update by Luca 25/07/2016
