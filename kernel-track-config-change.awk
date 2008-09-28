# $Id$

BEGIN {
	if ( ! infile ) {
		print "infile= must be specified" > "/dev/stderr"
		exit 1
	}

	while ( getline < infile ) {
		if ( match( $0, /^# CONFIG_[A-Za-z0-9_]+ is not set$/ ) ) {
			optionArray[ $2 ] = "n";
		} else if ( match( $0, /^CONFIG_[A-Za-z0-9_]+=/ ) ) {
			name = value = $1

			sub( /=.*$/, "", name )
			sub( /^[^=]*=/, "", value )

			optionArray[ name ] = value;
			continue
		}
	}
}


{
	name = ""
}

/^# CONFIG_[A-Za-z0-9_]+ is not set$/ {
	name = $2
	value = "n"
}

/^CONFIG_[A-Za-z0-9_]+=/ {
	name = value = $1

	sub( /=.*$/, "", name )
	sub( /^[^=]*=/, "", value )
}

{
	if ( ! length( name ) )
		next;

	orig = optionArray[ name ]
	if ( ! orig ) {
		#print "Warning: new option " name " with value " value
	} else {
		if ( value != orig ) {
			print "ERROR: option " name " redefined from " orig " to " value
		}
	}
}

END {
	exit 0
}
