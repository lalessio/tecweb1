#!/usr/bin/perl -w


use strict;
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use CGI::Cookie;
use XML::LibXML;
use XML::LibXSLT;
use File::Copy;
use POSIX;
use URI;

my $cgi = new CGI;
my $file = "../data/newsparco.xml";
my $parser = XML::LibXML->new();
my $doc = $parser->parse_file($file);
my $id = $cgi->param('ID');
my $ric = $doc->findnodes("/news/notizia[\@\ID = $id]")->get_node(1);
my $parent = $ric->parentNode;
$parent->removeChild($ric);
open(OUT,">$file") or die $!;
print OUT $doc->toString;
close(OUT);			
print "Location:news.cgi\n\n";
#Last update 26/07/2016 by Carlo

