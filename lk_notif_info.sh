run_segment() {
    count=$(cat ~/.tmux_inform_notifications | wc -l )
    if [ $count -gt 0 ] ; then
      echo "⚑ Notifications : $count"
    else
      echo "☼"
    fi
}

