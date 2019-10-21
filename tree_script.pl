 #!/usr/bin/perl -w
use strict;
use warnings;
use File::Find;

printDir(".");
sub printDir{
opendir(DIR, $_[0]);
my @files;
my @dirs;
 (@files) = readdir(DIR);
 foreach $file (@files) {
    if (-f $file) {
      print $file .pl "\n";
    }
    if (-d $file && $file ne "." && $file ne "..") {
      push(@dirs, $file);
    }
 } 
 foreach $dir (@dirs) {
   print "\n";
   print $dir . "\n";
   printDir($dir);
 }
 closedir(DIR);
}
