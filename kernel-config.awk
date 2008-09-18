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
# 
# TODO:
#  - check value correctness, should allow only:
#    y, m, n, -[0-9]+, 0x[0-9A-Fa-f]+, ".*"
#  - smarter arch split, there could be strings with spaces
#    ( kernel-config.py does not suppoty it either )
#  - use as many warnings as possible, we want our configs to be clean

# no:
# CONFIG_SOMETHING=n		-- should warn
# SOMETHING=n			-- should warn
# CONFIG_SOMETHING all=n	-- should warn
# SOMETHING all=n
# # CONFIG_SOMETHING is not set	-- special case

# yes/module/other
# CONFIG_SOMETHING=y
# SOMETHING=y			-- should warn
# CONFIG_SOMETHING all=y	-- should warn
# SOMETHING all=y


# return actual file name (without path) and line number
function fileLine() {
	f = FILENAME
	gsub( /^.*\//, "", f ) # strip path

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
}

# convert special case:
# # CONFIG_SOMETHING it not set
# to:
# SOMETHING all=n
/^# CONFIG_[A-Za-z0-9_-]+ is not set$/ {
	match( $0, /CONFIG_[A-Za-z0-9_-]+/ )
	option = substr( $0, RSTART, RLENGTH)
	$0 = option " all=n"
}

# ignore all the comments
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
		gsub( /=.*$/, "", option )
		gsub( /^[^=]*=/, "", line )
		value = line
	} else {
		gsub( "^" option IFS, "", line )
		split( line, archs )
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

	if ( option in outputArray ) {
		warn( option " already defined in: " outputArray[ option ] )
		next
	}

	if ( length( value ) ) {
		if ( value == "n" )
			out = "# " option " is not set"
		else
			out = option "=" value
	
		print out
		outputArray[ option ] = fileLine()
	}
}

END {
}
