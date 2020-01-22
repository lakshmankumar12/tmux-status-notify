run_segment() {
    count=$(cat ~/.tmux_inform_notifications | wc -l )
    if [ $count -gt 0 ] ; then
      notif="!⚑ Notifications : $count"
    else
      notif="✹"
    fi
    load=""
    if [ -f $HOME/.load_summary ] ; then
        load=$(cat $HOME/.load_summary)
    fi
    echo "$notif $load"
}

