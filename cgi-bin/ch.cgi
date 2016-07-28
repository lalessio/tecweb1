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

my $cgi = CGI->new();

my $selected_day = $cgi->param('day');
my $new_orario = $cgi->param('new_hour');

my $file = "../data/orari.xml";
my $parser = XML::LibXML->new();
my $doc = $parser->parse_file($file);

my $b="fallita";

for my $dacambiare ($doc->findnodes("/orari/giorno[id='$selected_day']/ora/text()"))
{
	$dacambiare->setData($new_orario);
	$b="riuscita";
}
print $doc->toString;
print "Content-type:text/html\n\n";
print "<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\"
        \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">
	<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"it\" lang=\"it\">
	<head>
	</head>
	<body>
		<p>hai scelto di modificare il giorno $selected_day con nuovo orario $new_orario e l'operazione è $b</p>
	</body>
	</html>
";
