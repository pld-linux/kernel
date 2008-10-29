#!/usr/bin/perl
#
# Script used to sort kernel-*.config files.
# Usage:
#  ./kernel-config-sort.pl ../BUILD/linux-2.6.*/ kernel-multiarch.config
#
#  ./kernel-config-sort.pl ../BUILD/linux-2.6.*/ -a x86 kernel-x86_84.config
#
use strict;
use warnings;

my $dir = ( shift @ARGV ) || ".";
my $arch;
if ( $ARGV[0] eq "-a" ) {
	shift @ARGV;
	$arch = shift @ARGV;
}
my $old_dir = $ENV{PWD};
chdir $dir;

my @Kconfig_list;
my @Kconfig_arch;

sub look_in
{
	my $parent = shift;
	my @files = glob $parent."*";
	foreach ( @files ) {
		if ( -d ) {
			if ( $_ eq "Documentation" or $_ eq "build-done" ) {
				warn "Skipping $_\n";
				next;
			}
			look_in( $_ . '/' );
			next;
		}
		if ( m#^.*/Kconfig# ) {
			if ( m#^arch/# ) {
				push @Kconfig_arch, $_;
			} else {
				push @Kconfig_list, $_;
			}
		}
	}
}

if ( $arch ) {
	push @Kconfig_list, "arch/$arch/Kconfig";
} else {
	look_in("");
	push @Kconfig_list, @Kconfig_arch;
}

my %byFile;
my %byName;

sub add_Kconfig
{
	my $file = shift;

	my @maybe_add_source;
	my @config_list;

	unless ( -r $file ) {
		warn "FILE $file does not exist\n";
		return;
	}

	open my $f_in, '<', $file;
	while ( <$f_in> ) {
		if ( /^\s?(?:menu)?config\s+(.*?)`?\s*$/ ) {
			if ( $byName{ $1 } ) {
				warn "Warning: $file: $1 already defined in $byName{ $1 }\n";
				next;
			}
			push @config_list, [ 'o', $1 ];
			next;
		}
		if ( /^\s?comment\s+"(.*?)"\s*$/ ) {
			push @config_list, [ 'c', $1 ];
			next;
		}
		if ( /^\s*source\s+"(\S+?)"\s*$/ or /^\s*source\s+(\S+?)\s*$/) {
			push @maybe_add_source, $1;
			push @config_list, [ 's', $1 ];
			next;
		}
	}
	close $f_in;

	$byFile{ $file } = \@config_list;
	
	{
		my %add;
		@add{ @maybe_add_source } = ();
		foreach ( @Kconfig_list ) {
			delete $add{ $_ } if exists $add{ $_ };
		}
		if ( keys %add ) {
			#warn "Adding more source files: " . ( join ", ", sort keys %add ) ."\n";
			push @Kconfig_list, sort keys %add;
		}
	}
}

{
	my $i;
	for ( $i = 0; $i < scalar @Kconfig_list; $i++ ) {
		my $file = $Kconfig_list[ $i ];
		add_Kconfig( $file );
	}
}

my $arch_specific;
unless ( $arch ) {
	my @arch_specific;

	foreach my $f ( sort keys %byFile ) {
		next unless $f =~ /^arch/;
		foreach my $line ( @{ $byFile{ $f } } ) {
			push @arch_specific, $line->[1]
				if $line->[0] eq 'o';
		}
		delete $byFile{ $f };
	}

	my @as = map { [ 'o', $_ ] } sort @arch_specific;
	$arch_specific = \@as;
}

chdir $old_dir;

my $out_file = $ARGV[ $#ARGV ];

my %setOptions;

my $allowed_name = qr/[A-Za-z0-9_]+/;
my $comment = "";
while ( <> ) {
	if ( /^#\*/ ) {
		$comment .= $_;
		next;
	}
	my $opt;
	if ( /^# CONFIG_($allowed_name) is not set$/ ) {
		$opt = $1;
	}
	if ( /^(?:CONFIG_)?($allowed_name)[=\s]/ ) {
		$opt = $1;
	}
	unless ( $opt ) {
		if ( /\S/ and !/^#-/ ) {
			warn "Ignored line: $_";
		}
		next;
	}

	if ( exists $setOptions{ $opt } ) {
		die "OPTION $opt REDEFINED";
	}
	chomp;
	$setOptions{ $opt } = $comment . $_;
	$comment = "";
}

sub file_out
{
	my $file = shift;
	my $any_out = 0;
	my @out;
	push @out, "#-", "#- *** FILE: $file ***", "#-";
	my $file_lines = $byFile{ $file };

	foreach my $line ( @{$file_lines} ) {
		my ($type, $data) = @$line;
		if ( $type eq 'o' ) {
			if ( exists $setOptions{ $data } ) {
				push @out, $setOptions{ $data };
				delete $setOptions{ $data };
				$any_out = 1;
			}
		} elsif ( $type eq 'c' ) {
			push @out, "#- $data";
		} elsif ( $type eq 's' ) {
			push @out, "#- file $data goes here";
		}
	}
	if ( $any_out ) {
		return "\n" . ( join "\n", @out ) . "\n";
	}
	return "";
}

*FILE_OUT = \*STDOUT;
if ( $out_file ) {
	open FILE_OUT, '>', $out_file;
}
unless ( $arch ) {
	my @out;
	foreach my $f ( sort keys %byFile ) {
		push @out, file_out( $f );
	}

	my $as_name = "arch/* - ARCH SPECIFIC OPTIONS";
	$byFile{ $as_name } = $arch_specific;
	unshift @out, file_out( $as_name );

	print FILE_OUT @out;
} else {
	foreach my $f ( sort keys %byFile ) {
		print FILE_OUT file_out( $f );
	}
}

if ( keys %setOptions ) {
	print FILE_OUT "\n#-\n#- *** PROBABLY REMOVED OPTIONS ***\n#-\n";
	foreach my $k ( sort keys %setOptions ) {
		print FILE_OUT $setOptions{ $k } . "\n";
	}
}
