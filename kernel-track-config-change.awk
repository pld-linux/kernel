# $Id$

BEGIN {
	if ( ! infile ) {
		print "infile= must be specified" > "/dev/stderr"
		exit 1
	}

	file = ""
	while ( getline < infile ) {
		name = ""
		if ( match( $0, /^# CONFIG_[A-Za-z0-9_]+ is not set$/ ) ) {
			name = $2
			value = "n"
		} else if ( match( $0, /^CONFIG_[A-Za-z0-9_]+=/ ) ) {
			name = value = $1

			sub( /=.*$/, "", name )
			sub( /^[^=]*=/, "", value )
		} else if ( match( $0, /^# file:/ ) ) {
			file = $3
		}
		if ( length( name ) ) {
			optionArray[ name ] = value
			optionFile[ name ] = file
		}
	}

	foundErrors = 0
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
			print "ERROR (" optionFile[ name ] "): option " name " redefined from " orig " to " value
			foundErrors++
		}
	}
}

END {
	if ( foundErrors ) {
		print "There were " foundErrors " errors"
		if ( dieOnError )
			exit 1
	}
}
