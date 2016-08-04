#!/usr/bin/perl -w

use strict;
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use CGI::Cookie;
use XML::LibXML;
use File::Copy;
use URI;

my $session = CGI::Session->load() or die $!;
my %cookie = CGI::Cookie->fetch;
$cookie{'autorizzazione'}->value("nope");
$cookie{'autorizzazione'}->bake;
$session->delete();
print "Content-type:text/html\n\n";
			print "<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">
			<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"it\" lang=\"it\"> 
			<head>
			<title>Logout...</title>
			<meta name=\"title\" content=\"Redirect\"/>
			<meta http-equiv=\"refresh\" content=\"0; url=../index.html\"/>
			</head>
			<body>
			</body>
			</html>";
#Last Update by Carlo 26/07/2016
