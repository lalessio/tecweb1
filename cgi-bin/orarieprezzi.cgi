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
		<meta http-equiv=\"Content-Script-Type\" content=\"text/javascript\"/>
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
				<li class=\"active\">ORARI E PREZZI</li>
				<li><a href=\"../infocontatti.html\">INFO E CONTATTI</a></li>
			</ul>
		</div>
		
		<div class=\"nav\">Ti trovi qui: <a href=\"../index.html\"><span lang=\"en\">Home</span></a> &gt;&gt; Orari e Prezzi</div>

		<div class=\"contenuto\" id=\"contenuto\">
			<h1 class=\"titolo_testo\">Orari</h1>
            <img class=\"foto4\" alt=\"orari e prezzi del parco\" src=\"../images/orariprezzi.jpg\"/>
			<p>Il Parco Naturale Monte Verde e' aperto dal 1 Marzo al 31 Novembre.</p> 
			<p>L'orario di apertura al pubblico del parco resta invariato tutto l'anno ed e' il seguente:</p>
			<ul>

";

my @orari = $doc1->findnodes("/orari/giorno");
foreach my $orario (@orari)
{
	my $ora = ($orario->findvalue('ora'));
	
	decode_entities($ora);
	
    my $id = ($orario->getAttribute('id'));
    
    decode_entities($id);
    
	print "<li><strong>$id:</strong><ul><li>$ora</li></ul></li>";
}

print"
	</ul>
	<h1 class=\"titolo_testo\">Prezzi</h1>
	<p>Il prezzo d'ingresso e' scontato per i ragazzi sotto i 12 anni e gli anziani sopra i 65 e inoltre durante il periodo estivo (15 Maggio - 15 Settembre) si risparmia sempre!</p> 
	<ul>";
	
my @prezzi = $doc2->findnodes("/prezzi/ingresso");
foreach my $prezzo (@prezzi)
{
	my $pa = ($prezzo->findvalue('primaveraautunno'));
	
	decode_entities($pa);
	
	my $estate = ($prezzo->findvalue('estate'));
	
	decode_entities($estate);
	
    my $id = $prezzo->getAttribute('id');
    
    decode_entities($id);
    
	print "<li>
				<span>$id:</span>
				<ul>
					<li><span>Primavera - Autunno: $pa €</span></li>
					<li><span>Estate: $estate €</span></li>
				</ul>
			</li>";
}	
if($auth eq "checksession")
{
print"
	</ul>
	<p><strong>Prezzi ed orari possono essere oggetto di variazioni.</strong></p>
</div>						
	<div class=\"footer\">
		<a href=\"../mappasito.html\"><span class=\"up\">MAPPA DEL SITO</span></a>
		<a href=\"#menu\"><span class=\"up\">TORNA ALL'INIZIO</span></a>
		 <img class=\"valido\" alt=\"css valido\" src=\"../images/css.png\"/>
		 <div class=\"indirizzo\"> Via Nazionale, 22 38085  Bolzano (TN)</div>
		 <div class=\"indirizzo\"><a href=\"logout.cgi\"><button type=\"submit\" name=\"delete\"><span xml:lang=\"en\">Logout</span></button></a></div>
		 <div class=\"indirizzo\"><a href=\"adminarea.cgi\">TORNA AD <span lang=\"en\">ADMIN</span> AREA</a></div>
		<img class=\"valido\" alt=\"xhtml valido\" src=\"../images/xhtml.png\"/></div>
	</body>
	</html>
";
}else
{
print"
	</ul>
	<p><strong>Prezzi ed orari possono essere oggetto di variazioni.</strong></p>
</div>			
	<div class=\"footer\">
		<a href=\"../mappasito.html\"><span class=\"up\">MAPPA DEL SITO</span></a>
		<a href=\"#menu\"><span class=\"up\">TORNA ALL'INIZIO</span></a>
		 <img class=\"valido\" alt=\"css valido\" src=\"../images/css.png\"/>
		 <div class=\"indirizzo\"> Via Nazionale, 22 38085  Bolzano (TN)</div>
		 <div class=\"indirizzo\"><a href=\"adminlogin.cgi\">AREA AMMINISTRATORE</a></div>
		<img class=\"valido\" alt=\"xhtml valido\" src=\"../images/xhtml.png\"/></div>
	</body>
	</html>
";
}

#Last Update by Luca 25/07/2016
