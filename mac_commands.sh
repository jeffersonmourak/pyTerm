f() {
	local IFS=:
	local foo
	set -f # Disable glob expansion
	foo=( $@ ) # Deliberately unquoted 
	set +f
	n=${#foo[@]}

	for ((j=0; j < n; j++)); do

		for i in ${foo[j]}/*; do
			if [[ -x "$i" && -f "$i" ]]; then     
				k="$(echo $i | rev | cut -d/ -f1 | rev)"
				printf '%s ' $k
			fi
		done

	done
}

f $PATH