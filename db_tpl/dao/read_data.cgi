#!/usr/bin/perl
use strict;
use warnings;

use lib '/var/www/work/db_tpl/controller';    # Add path of my module
use Main;                                     # Add my module
use DBI;
use CGI;

my $Cgi = CGI->new;

print $Cgi->header("text/html");

# Add path to view files
my $tpl_main = TPL::load_tpl("view/main_tpl.tpl");
my $tpl_user = TPL::load_tpl("view/user_form.tpl");

# try to connect to database

my $dbh = DBI->connect("dbi:mysql:dbname=abills", "abills", "Vintoniak7______", { RaiseError => 1 },) or die $DBI::errstr;

# select DATA from mysql table

my $stm = $dbh->prepare("SELECT user_id, user_name, user_address, user_email FROM user_inform");
$stm->execute();

my $users_tpl;
while (my @user = $stm->fetchrow_array()) {
  my ($user_id, $user_name, $user_address, $user_email) = @user;

  $users_tpl .= TPL::render_tpl(
    $tpl_user,
    (
      user_id      => $user_id,
      user_name    => $user_name,
      user_address => $user_address,
      user_email   => $user_email
    )
  );
}

# calling a subroutine and to tpl real data ( changes the markers )
print TPL::render_tpl(
  $tpl_main,
  (
    title   => "Users Panel",
    content => $users_tpl
  )
);

$stm->finish;
$dbh->disconnect;
