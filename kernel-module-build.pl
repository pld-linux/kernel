#!/usr/bin/perl
#
use strict;
use warnings;
use File::Find qw(find);

my $rpmdir = shift @ARGV or die;
my $fileoutdir = shift @ARGV or die;
my @tosort;

find(\&wanted, ".");

sub wanted {
	return unless -f;
	return unless /^Kconfig/ or /^Makefile/;
	#return if /\.orig$/;
	return if $File::Find::name =~ /(Documentation|scripts)/;
	(my $file = $File::Find::name) =~ s#^\./##;
	$file =~ m#^(.*)/#;
	my $dir = $1;
	my $subdir = "";
	foreach my $sub ( split( '/', $dir )) {
		$subdir .= "/" . $sub;
		push @tosort, "\%dir $rpmdir$subdir\n";
	}
	push @tosort, "$rpmdir/$file\n";
}

my $last = "";
my @toprint = grep {if ($_ ne $last) { $last = $_; 1} else {0}} sort @tosort;

open F_OUT, "> $fileoutdir/aux_files" or die "Can't create aux_files: $!\n";
print F_OUT @toprint;
close F_OUT and print "aux_files created\n";

open F_OUT, "> $fileoutdir/aux_files_exc" or die "Can't create aux_files_exc: $!\n";
print F_OUT map {"\%exclude $_"} @toprint;
close F_OUT and print "aux_files_exc created\n";
