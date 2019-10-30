#!/usr/bin/perl -w
use CGI::Carp qw(fatalsToBrowser);

# режим вывода - gif картинки
print "Content-type: image/gif\n\n";

use strict;
use DBI;

#reading image from database

# try to connect to database

my $dbh = DBI->connect("dbi:mysql:dbname=work", "root", "", { RaiseError => 1 },) or die $DBI::errstr;

# taking image from database

my $stm = $dbh->prepare("SELECT image FROM image_table WHERE id=7");
$stm->execute();
my $image = $stm->fetch();

open IMAGE, ">22.gif" or die $!;
print IMAGE @$image;
close(IMAGE);

$stm->finish();
$dbh->disconnect();
