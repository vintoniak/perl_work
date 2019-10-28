#!/usr/bin/perl

use strict;
use DBI;

#reading image from database 

# try to connect to database

my $dbh = DBI->connect("dbi:mysql:dbname=work", "root", "", { RaiseError => 1 },) or die $DBI::errstr;

# taking image from database

my $stm = $dbh->prepare("SELECT image FROM image_table WHERE Id=1");
$stm->execute();
my $image = $stm->fetch();

open IMAGE, "1.jpg" or die $!;
print IMAGE @$image;
close(IMAGE);

$stm->finish();
$dbh->disconnect();
