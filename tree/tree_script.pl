#!/usr/bin/perl -w
use strict;
use warnings;
use File::Find;
use Data::Dumper;

# print "Content-Type: text/html\n\n";

my $buffer;
my $dir_token;
my @files;
my @dirs;
my @pairs;
my $pair;
my $name;
my $value;
my $file;
read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
@pairs = split(/&/, $buffer);

foreach $pair (@pairs) {
  ($name, $value) = split(/=/, $pair);
  $dir_token = $value;
}

sub printDir {
  my ($dir_name) = @_;
  print Dumper $dir_name;
  opendir(my $dir, $dir_name);

  (@files) = readdir($dir_name);
  foreach $file (@files) {
    if (-f $file) {
      print $file . "\n";

      if (-d $file && $file ne "." && $file ne "..") {
        push(@dirs, $file);
      }
    }

  }
  closedir($dir_name);
}


