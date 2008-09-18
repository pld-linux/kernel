# A script for building kernel config from multiarch config file.
# It also has some file merging facilities.
#
# usage:
#  awk -v arch=%{_target_base_arch} -f path/to/kernel-config.awk \
#    kernel-multiarch.config kernel-%{arch}.config kernel-%{some_feature}.config \
#     > .config
#
# TODO:
#  - check value correctness, should allow only:
#    y, m, n, -[0-9]+, 0x[0-9A-Fa-f]+, ".*"
#  - smarter arch split, there could be strings with spaces
#    ( kernel-config.py does not suppoty it either )
#  - use as many warnings as possible, we want our configs to be clean
#  - allow more multiarch configs

function warn( msg ) {
	print FILENAME " (" FNR "): " msg > "/dev/stderr"
}

BEGIN {
	if ( ! arch ) {
		warn( "arch= must be specified" )
		exit 1
	}
	firstfile = 1
}

{
	# remember first file name
	if ( ! file )
		file = FILENAME

	else if ( file != FILENAME ) { # second and following files
		if ( match( $0, /CONFIG_[A-Za-z0-9_-]+/ ) ) {
			option = substr( $0, RSTART, RLENGTH )
			if ( $0 ~ "^" option "=.+$" || $0 ~ "^# " option " is not set$" ) {
				if ( option in outputArray )
					warn( option " already defined in: " outputArray[ option ] )
				else {
					print
					outputArray[ option ] = FILENAME " (" FNR ")"
				}
			} else {
				if ( ! /^#/ )
					warn( "Incorrect line: " $0 )
			}
		} else if ( ! /^\s*$/ && ! /^#/ ) {
			warn( "Incorrect line: " $0 )
		}
		next
	}
}

# multiarch file proxessing

/^#/ || /^\s*$/ {
	next
}

/^CONFIG_/ {
	warn( "Options should not start with CONFIG_" )
	gsub( /^CONFIG_/, "" )
}

{
	option = $1
	line = $0
	if ( option ~ /=/ ) {
		warn( $0 " should have explicit ` all='" )
		gsub( /=.*$/, "", option )
		gsub( /^[^=]*=/, "", line )
		line = "all=" line
	} else {
		gsub( "^" option, "", line )
	}
	split( line, archs )

	dest = ""
	for ( inx in archs ) {
		split( archs[inx], opt, "=" );
		if ( opt[1] == "all" )
			dest = opt[2]

		if ( opt[1] == arch ) {
			dest = opt[2]
			break
		}
	}
	if ( length( dest ) ) {
		option = "CONFIG_" option

		if ( dest == "n" )
			out = "# " option " is not set"
		else
			out = option "=" dest
		print out

		outputArray[ option ] = FILENAME " (" FNR ")"
	}
}

END {
}
