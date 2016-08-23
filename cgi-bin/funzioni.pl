#!/usr/bin/perl -w

use HTML::Parser;
use HTML::Entities;
use utf8;
sub  rimuovi{ my $s = shift; $s =~ s/^\s+|\s+$//g; return $s };

sub string() {
	my $string = shift;
  	$string = encode_entities($string, '<>&"');
	$string = encode_entities($string);
	return $string;
}




1;
