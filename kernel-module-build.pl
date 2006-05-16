#!/usr/bin/perl

open( F, $ARGV[0]) or die("cannot open file: $ARGV[0]\n" );
@lines = <F>;
close( F );

foreach (@lines)
{
	@pe = split( '/', $_ );
	my $tmp;
	for my $p (0 .. $#pe - 1)
	{
		$tmp = $tmp . '/' . $pe[$p];
		print( "%dir $ARGV[1]$tmp\n" );
	}
	my $file = join( '/', @pe );
	print( "$ARGV[1]/$file" );
}
