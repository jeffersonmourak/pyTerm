COMMANDS=`echo -n $PATH | xargs -d : -I {} find {} -maxdepth 1 \
        -executable -type f -printf '%P '`
    ALIASES=`alias | cut -d '=' -f 1`
    echo "$COMMANDS"$'\n'"$ALIASES" | sort -u