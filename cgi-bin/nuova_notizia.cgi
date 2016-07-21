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

#my $session = CGI::Session->load() or die $!;
#my $auth = $session->param('auth');
$CGI::POST_MAX = 1024 * 1000; #limite upload 1 MB
my $file_er = \"a-zA-Z0-9_.-";
my $upload_dir = "../images";
my $cgi = CGI->new();
my $filename = $cgi->param('new_image');
my $nuovo_titolo = $cgi->param('new_title');
my $nuovo_contenuto = $cgi->param('new_content');
chomp $filename;
my ($nome, $path, $estensione) = fileparse($filename, '..*');
if (($estensione =~ /.png/i) || ($estensione =~ /.jpg/i) || ($estensione =~ /.jpeg/i) || ($estensione =~ /.gif/i))
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
	
	my $img = XML::LibXML::Element->new('img');
	$img->appendText("$filename");
	$new_node->appendChild($img);

	my $notizie = $doc->findnodes("/news")->get_node(1);
	$notizie->appendChild($new_node);
	open(OUT,">$file") or die;
	print OUT $doc->toString;
	close(OUT);
		
	print "Content-type:text/html\n\n";

	print "
	<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">
	<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"it\" lang=\"it\"> 
	<head>
	</head>
	<body>
	  <p>OK!</p>
	</body>
	</html>
	";		
}
else 
{
	print "
	<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">
	<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"it\" lang=\"it\"> 
	<head>
	</head>
	<body>
	  <p>ERRORE IMMAGINE</p>
	</body>
	</html>
	";		
}
#Last Update by Luca 21/07/2016
