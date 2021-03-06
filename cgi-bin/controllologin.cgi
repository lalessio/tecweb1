#!/usr/bin/perl -w


use strict;
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use CGI::Cookie;
use XML::LibXML;
use File::Copy;
use URI;

my $cgi = CGI->new();

my $username = $cgi->param('user_name');

my $password = $cgi->param('user_pwd');

my $auth="checksession";
my $file = "../data/amministratore.xml";

# creazione oggetto parser
my $parser = XML::LibXML->new();

# apertura file e lettura input
my $doc = $parser->parse_file($file);

# estrazione radice
my $root = $doc->getDocumentElement;


	my $pwd = $doc->findvalue("/amministratore/password");
	my $user = $doc->findvalue("/amministratore/username");
	
	# confronto le password
	if ($pwd ne $password || $user ne $username)
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
		<meta http-equiv=\"Content-Script-Type\" content=\"text/javascript\"/>
		<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
		<link rel="stylesheet" href="../css/style.css" type="text/css" media="screen"/>
		<link rel=\"stylesheet\" href=\"../css/styleprint.css\" type=\"text/css\" media=\"print\"/>

	</head>
	<body>
<div><a class=\"salta\" href=\"#contenuto\"><span>Salta al contenuto</span></a></div>
		<div><a href="../index.html"><img class="logo" alt="logo del parco" src="../images/logo.jpg"/></a></div> 
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

		<div class="nav">Ti trovi qui: <a href="../index.html"><span lang="en">Home</span></a> &gt; &gt;<a href="adminlogin.cgi"><span lang="en">Admin</span> amministratore</a> &gt; &gt; Errore</div>

		<div class="contenuto" id=\"contenuto\">	
		<h1 class="blocco1">Errore</h1>
		<p><span lang="en">Login</span> sbagliato, riprova di nuovo <a href="adminlogin.cgi"><span lang="en">Login</span></a></p> 
		</div>
		
		<div class="footer">
        <a href="../mappasito.html"><span class="up">MAPPA DEL SITO</span></a>
		<a href="#menu"><span class="up">TORNA ALL'INIZIO</span></a>
		 <img class="valido" alt="css valido" src="../images/css.png"/>

		 <div class="indirizzo"> Via Nazionale, 22 38085  Bolzano (TN)</div>

		<img class="valido" alt="xhtml valido" src="../images/xhtml.png"/></div>

	</body>
</html>
EOF
exit;
}
	if ($pwd eq $password){
		# controllo se la sessione esiste gia
		my $session = CGI::Session->load() or die $!;

		if($session->is_expired || $session->is_empty){
			# sessione non esiste quindi la creo
			my $session = new CGI::Session(undef, undef, {Directory=>'/tmp'});
			# aggiungo i parametri utente alla sessione
			$session->param("username", $username);
			$session->param("auth", $auth);

			# creo il cookie
			my $cookie1 = CGI::Cookie->new(-name => $session->name, -value => $session->id);
			my $cookie2 = CGI::Cookie->new(-name => "user", -value => $username);
                        my $cookie3 = CGI::Cookie->new(-name => "autorizzazione", -value => $auth);
			print header(-cookie => [$cookie1,$cookie2,$cookie3]);
			
			print "Content-type:text/html\n\n";
			print "<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">
			<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"it\" lang=\"it\"> 
			<head>
			<title>Controllo login</title>
			<meta name=\"title\" content=\"Redirect\"/>
			<meta http-equiv=\"refresh\"
			content=\"0; url=adminarea.cgi\"/>
			</head>
			<body>
			</body>
			</html>";
		

		}
		else{
			# la sessione esiste
			# controllo l'esistenza del cookie
			my %cookie = CGI::Cookie->fetch;
			my $cook = $cookie{'autorizzazione'};
			my $cook2 = $cookie{'user'};
			# se i 2 cookie fondamentali non sono presenti lo ricreo
			if(!defined $cook){
				# ricreo il cookie se mancante
				my $cookie3 = CGI::Cookie->new(-name => "autorizzazione", -value => $auth);
				print header(-cookie => $cookie3);				
			}
			if(!defined $cook2){
                        # ricreo il cookie se mancante
			my $cookie2 = CGI::Cookie->new(-name => "user", -value => $username);
				print header(-cookie => $cookie2);				
			}

			print "Content-type:text/html\n\n";
			print "<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">
			<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"it\" lang=\"it\"> 
			<head>
			<title>Controllo login</title>
			<meta name=\"title\" content=\"Redirect\"/>
			<meta http-equiv=\"refresh\"
			content=\"0; url=adminarea.cgi\"/>
			</head>
			<body>
			</body>
			</html>";
		
		}
	}
