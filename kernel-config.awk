# $Id$
# A script for building kernel config from multiarch config file.
# It also has some file merging facilities.
#
# usage:
#  awk -v arch=%{_target_base_arch} -f path/to/kernel-config.awk \
#    kernel-important.config kernel-multiarch.config \
#    kernel-%{arch}.config kernel-%{some_feature}.config \
#     > .config
#
# Authors:
# - Przemysław Iskra <sparky@pld-linux.org>
# parts based on kernel-config.py, by:
# - arekm@pld-linux.org
# - glen@pld-linux.org
# 
# TODO:
#  - smarter arch split, there could be strings with spaces
#    ( kernel-config.py does not suppoty it either )
#  - use as many warnings as possible, we want our configs to be clean

# no:
# CONFIG_SOMETHING=n
# SOMETHING=n
# CONFIG_SOMETHING all=n
# SOMETHING all=n
# # CONFIG_SOMETHING is not set -- special case

# yes/module/other
# CONFIG_SOMETHING=y
# SOMETHING=y
# CONFIG_SOMETHING all=y
# SOMETHING all=y


# return actual file name (without path) and line number
function fileLine() {
	f = FILENAME
	sub( /^.*\//, "", f ) # strip path

	return f " (" FNR ")"
}

function warn( msg ) {
	print fileLine() ": " msg > "/dev/stderr"
}

BEGIN {
	if ( ! arch ) {
		print "arch= must be specified" > "/dev/stderr"
		exit 1
	}
	shouldDie = 0
}

function dieLater( code ) {
	if ( shouldDie < code )
		shouldDie = code
}

# convert special case:
# # CONFIG_SOMETHING it not set
# to:
# SOMETHING all=n
/^# CONFIG_[A-Za-z0-9_]+ is not set$/ {
	match( $0, /CONFIG_[A-Za-z0-9_]+/ )
	option = substr( $0, RSTART, RLENGTH)
	$0 = option " all=n"
}

# ignore all the comments and empty lines
/^#/ || /^\s*$/ {
	next
}

!/^CONFIG_/ {
	$0 = "CONFIG_" $0
}

{
	option = $1
	line = $0
	value = ""
	if ( option ~ /=/ ) {
		sub( /=.*$/, "", option )
		sub( /^[^=]*=/, "", line )
		value = line
	} else {
		sub( "^" option, "", line )
		sub( /^[ \t]*/, "", line )

		if ( line ~ /"/ ) {
			# there can be white spaces
			i = 0
			while ( match( line, /^[^=]+="[^"]*"/ ) ) {
				archs[ (++i) ] = substr( line, RSTART, RLENGTH )
				line = substr( line, RSTART + RLENGTH )
				sub( /^[ \t]*/, "", line )
			}
		} else {
			split( line, archs )
		}
		for ( i in archs ) {
			split( archs[i], opt, "=" );
			if ( opt[1] == "all" )
				value = opt[2]

			if ( opt[1] == arch ) {
				# found best match, don't look further
				value = opt[2]
				break
			}
		}
	}

	# completely ignore lines with no value
	if ( length( value ) == 0 )
		next

	fileOption = FILENAME "/" option
	if ( fileOption in outputByFile ) {
		warn( "ERROR: " option " already defined in this file at line " outputByFile[ fileOption ] )
		dieLater( 2 )
		next
	} else
		outputByFile[ fileOption ] = FNR

	if ( option in outputArray ) {
		warn( "Warning: " option " already defined in: " outputArray[ option ] )
		next
	} else
		outputArray[ option ] = fileLine()

	if ( value == "n" )
		out = "# " option " is not set"
	else {
		out = option "=" value

		if ( value == "y" || value == "m" )
			; # OK
		else if ( value ~ /^"[^"]*"$/ )
			; # OK
		else if ( value ~ /^-?[0-9]+$/ || value ~ /^0x[0-9A-Fa-f]+$/ )
			; # OK
		else {
			warn( "ERROR: Incorrect value: " $0 )
			dieLater( 1 )
		}
	}
	
	print out
}

END {
	exit shouldDie
}
