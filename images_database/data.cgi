#!/usr/bin/perl

use strict;
use DBI;

# writting image

# try to connect to database

my $dbh = DBI->connect("dbi:mysql:dbname=work", "root", "", { RaiseError => 1 },) or die $DBI::errstr;

open IMAGE, "../22.gif" or die $!;

my ($image, $buff);
while (read IMAGE, $buff, 1024) {
  $image .= $buff;
}

# insert image to database

my $stm = $dbh->prepare("INSERT INTO image_table(id, image) VALUES (8, ?)");
$stm->bind_param(1, $image, DBI::SQL_BLOB);
$stm->execute();

close(image_table);
$stm->finish();
$dbh->disconnect();

1;

