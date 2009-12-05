#!/usr/bin/perl
#
use strict;
use warnings;
use File::Find qw(find);

my $rpmdir = shift @ARGV or die;
my $fileoutdir = shift @ARGV or die;

# files which match: */include/*/Kbuild
my @modulebuild_in_include;
# files which match: */Kbuild */Kconfig except include
my @modulebuild;
# parent dirs of Kconfig files which match */include*
my @dirs_in_include;
# parent dirs of Kconfig files except include
my @dirs;

sub push_dirs
{
	my $list = shift;
	my $dir = shift;
	my $subdir = "";
	foreach my $sub ( split( '/', $dir )) {
		$subdir .= "/" . $sub;
		push @$list, "\%dir $rpmdir$subdir\n";
	}
}

sub wanted
{
	return unless -f;
	return unless /^Kconfig/ or /^Makefile/ or /^Kbuild/;
	#return if /\.orig$/;
	return if $File::Find::name =~ /(Documentation|scripts)/;
	(my $file = $File::Find::name) =~ s#^\./##;
	$file =~ m#^(.*)/#;
	my $dir = $1 || "";
	if ( $dir =~ m{^(.*/)?include(/.*?)?$} ) {
		push @modulebuild_in_include, "$rpmdir/$file\n";
		push_dirs( \@dirs_in_include, $dir );
	} else {
		push @modulebuild, "$rpmdir/$file\n";
		push_dirs( \@dirs, $dir );
	}
}

find(\&wanted, ".");

sub uniq
{
	my %hash = map { $_, 1 } @_;
	return sort keys %hash;
}

sub remove
{
	my $from = shift;
	my $what = shift;
	my %hash = map { $_, 1 } @$from;
	foreach ( @$what ) {
		delete $hash{ $_ };
	}
	return sort keys %hash;
}

# to module-build add all Kconfig, Makefile and Kbuild files
# also add all their parent dirs if they aren't parents of some include directory
open F_OUT, "> $fileoutdir/files.mb_include_modulebuild_and_dirs"
	or die "Can't create files.mb_include_modulebuild_and_dirs: $!\n";
print F_OUT remove( \@dirs, \@dirs_in_include );
print F_OUT uniq( @modulebuild_in_include, @modulebuild );
close F_OUT and print "files.mb_include_modulebuild_and_dirs created\n";

# from source remove all files Kconfig, Makefile and Kbuild files
# also remove all their parent dirs
open F_OUT, "> $fileoutdir/files.source_exclude_modulebuild_and_dirs"
	or die "Can't create files.source_exclude_modulebuild_and_dirs: $!\n";
print F_OUT map {"\%exclude $_"} uniq( @modulebuild_in_include, @modulebuild,
	@dirs_in_include, @dirs );
close F_OUT and print "files.source_exclude_modulebuild_and_dirs created\n";

# from headers remove all Kconfig, Makefile and Kbuild files that are
# part of include directory
open F_OUT, "> $fileoutdir/files.headers_exclude_kbuild"
	or die "Can't create files.headers_exclude_kbuild: $!\n";
print F_OUT map {"\%exclude $_"} uniq( @modulebuild_in_include );
close F_OUT and print "files.headers_exclude_kbuild created\n";
