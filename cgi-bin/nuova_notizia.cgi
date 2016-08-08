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
use HTML::Parser;
use HTML::Entities;

my $session = CGI::Session->load() or die $!;
my $auth = $session->param('auth');
$CGI::POST_MAX = 1024 * 1000; #limite upload 1 MB
my $file_er = \"a-zA-Z0-9_.-";
my $upload_dir = "../images";
my $cgi = CGI->new();
my $filename = $cgi->param('new_image');
encode_entities($filename);
my $nuovo_titolo = $cgi->param('new_title');
encode_entities($nuovo_titolo);
my $nuovo_contenuto = $cgi->param('new_content');
encode_entities($nuovo_contenuto);

if($filename eq "" or $nuovo_contenuto eq "")
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
	<div><a class="salta" href="#contenuto"><span>Salta al contenuto</span></a></div>
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

		<div class="nav">Ti trovi qui: <a href="../index.html"><span lang="en">Home</span></a> &gt; &gt;<a href="adminlogin.cgi"><span lang="en">Admin</span> amministratore</a> &gt; &gt;<a href="adminarea.cgi"><span lang="en">Admin</span>area</a> &gt; &gt; Errore</div>

		<div class="contenuto" id="contenuto">	
		<h1 class="blocco1">Errore</h1>
		<p>Uno o piu' campi sono vuoti, riprova di nuovo <a href="adminarea.cgi"><span lang="en">Admin</span>area</a></p> 
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

chomp $filename;
my ($nome, $path, $estensione) = fileparse($filename, '..*');
if (($estensione =~ /.png/i) || ($estensione =~ /.jpg/i) || ($estensione =~ /.jpeg/i) || ($estensione =~ /.gif/i) )
{
	
	
	$filename = $nome . $estensione;
	$filename =~ tr/ /_/;

	my $file_up = $cgi->upload("new_image");
	
	open (UPLOADFILE, ">../public_html/images/$filename") or die "$!";
	binmode UPLOADFILE;

	while( <$file_up> ){
		print UPLOADFILE;
	}
	close UPLOADFILE;
	


	my $file = "../data/newsparco.xml";
	
	my $parser = XML::LibXML->new();
	
	my $doc = $parser->parse_file($file);
	
	my $root = $doc->getDocumentElement;
	
	my $new_node = XML::LibXML::Element->new('notizia');
 
    my $id;
	my $path = $doc->findnodes("/news/notizia[last()]")->get_node(1);
	if ($path){
		$id = $path->getAttribute('ID');
	}
	else{
		$id=0;
	}
	$new_node->setAttribute("ID", $id+1); 

	my $titolo = XML::LibXML::Element->new('titolo');
	$titolo->appendText($nuovo_titolo);
	$new_node->appendChild($titolo);
	
	my $contenuto = XML::LibXML::Element->new('contenuto');
	$contenuto->appendText($nuovo_contenuto);
	$new_node->appendChild($contenuto);
	
	my $datacorrente = XML::LibXML::Element->new('data');
	my $ymd = strftime "%Y/%m/%d", localtime;
	$datacorrente->appendText($ymd);
	$new_node->appendChild($datacorrente);
	
	my $img = XML::LibXML::Element->new('img');
	$img->appendText("$filename");
	$new_node->appendChild($img);

	my $notizie = $doc->findnodes("/news")->get_node(1);
	$notizie->appendChild($new_node);
	open(OUT,">$file") or die;
	print OUT $doc->toString;
	close(OUT);
	
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
		<div><a class="salta" href="#contenuto"><span>Salta al contenuto</span></a></div>
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

		<div class="nav">Ti trovi qui: <a href="../index.html"><span lang="en">Home</span></a> &gt; &gt;<a href="adminlogin.cgi"><span lang="en">Admin</span> amministratore</a> &gt; &gt;<a href="adminarea.cgi"><span lang="en">Admin</span>area</a> &gt; &gt; Inserimento avvenuto</div>

		<div class="contenuto" id="contenuto">	
		<h1 class="blocco1">Informazioni</h1>
		<p>Inserimento avvenuto con successo! Puoi visualizzare le notizie più recenti in <a href="../newsattivita.html"><span lang="en">News</span> e attivita'</a></p> 
		<p>Ritorna all' <a href="adminarea.cgi">Area Amministratore</a></p>
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
else 
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
		<div><a class="salta" href="#contenuto"><span>Salta al contenuto</span></a></div>
		<div><a href="index.html"><img class="logo" alt="logo" src="../images/logo.jpg"/></a></div> 
		<div class="titolo"><a href="../index.html">Parco Naturale</a></div><div class="sottotitolo"><a href="../index.html">Monte Verde</a></div>
		<div id="menu">
			<ul class="lista">
				<li><a href="../index.html"><span lang="en">HOME</span></a></li>
				<li><a href="../chisiamo.html">CHI SIAMO</a></li>
				<li><a href="../naturaterritorio.html">NATURA E TERRITORIO</a></li>
				<li><a href="newsattivita.cgi"><span lang="en">NEWS</span> E ATTIVITÀ</a></li>
				<li><a href="orarieprezzi.cgi">ORARI E PREZZI</a></li>
				<li><a href="../infocontatti.html">INFO E CONTATTI</a></li>
			</ul>
		</div>

		<div class="nav">Ti trovi qui: <a href="../index.html"><span lang="en">Home</span></a> &gt; &gt;<a href="../adminlogin.cgi"><span lang="en">Admin</span> amministratore</a> &gt; &gt;<a href="adminarea.cgi"><span lang="en">Admin</span>area</a> &gt; &gt; Errore</div>

		<div class="contenuto" id="contenuto">	
		<h1 class="blocco1">Errore</h1>
		<p>Formato immagine non supportato, riprova di nuovo <a href="adminarea.cgi"><span lang="en">Admin</span>area</a></p> 
		</div>
		
		<div class="footer">
		<a href="#menu"><span id="up">TORNA ALL'INIZIO</span></a>
		 <img class="valido" alt="css valido" src="images/css.png"/>

		 <div class="indirizzo"> Via Nazionale, 22 38085  Bolzano (TN)</div>

		<img class="valido" alt="xhtml valido" src="images/xhtml.png"/></div>

	</body>
</html>
EOF
}

#Last Update by Luca 08/08/2016
