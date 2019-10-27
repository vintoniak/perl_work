
#!/usr/bin/perl
print "Conten-Type: text/html\n\n";

use strict;
use warnings;

# Open file for writting
open(my $fh, '>', 'file.txt') || die "Couldn't open file file.txt, $!";
# read content from web
read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});

@pairs = split(/&/, $buffer);
foreach $pair (@pairs) {
  ($name, $value) = split(/=/, $pair);
  print $fh "$name: $value\n";
}
print $fh "\n";
