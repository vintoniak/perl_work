#!/usr/bin/perl
use strict;
use warnings;
use DBI;

my $dbh = DBI->connect("dbi:mysql:dbname=work", "root", "", { RaiseError => 1 },) or die $DBI::errstr;

#запис картики в бд
open (my $file, "22.gif");
my ($image, $buff);
while(read $file, $buff, 1024) {
  $image .= $buff;
}
my $query = $dbh->prepare("INSERT INTO image_table(id,image) VALUES (7,?)");
$query->bind_param(1, $image, DBI::SQL_BLOB);
$query->execute;

close($file);
$query->finish();

#зчитування даних і конвертація
$query = $dbh->prepare("SELECT image FROM image_table");
$query->execute;

$image = $query->fetch();

print "Content-Type: image/gif\n\n";
print @$image;

$query->finish();
$dbh->disconnect();
