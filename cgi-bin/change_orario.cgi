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

for my $dacambiare ($doc->findnodes("/orari/giorno[id='$selected_day']/ora/text()"))
{
	$dacambiare->setData($new_orario);
}

print "Location: http://www.google.com/\n\n";
