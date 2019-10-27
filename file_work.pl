
#!/usr/bin/perl
use strict;
use warnings;
# use Data::Dumper;

if($ENV{'CONTENT_LENGTH'}){
# Open file for writting, read content from web
open(my $fh, '>', 'file.txt') || die "Couldn't open file file.txt, $!";
read(STDIN, my $buffer, $ENV{'CONTENT_LENGTH'});

my @pairs = split(/&/, $buffer);
foreach my $pair (@pairs) {
  (my $name, my $value) = split(/=/, $pair); # dif key, value
  print $fh "$name: $value\n";
 # print Dumper $pair;
}
print $fh "\n";
close($fh);
}
