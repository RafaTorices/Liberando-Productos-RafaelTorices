while true; do
    if pgrep -x mysqld >/dev/null; then
        echo "MySQL is running."
        sleep 30
        break
    else
        echo "MySQL is not running, waiting 30 seconds to retry..."
        sleep 30
    fi
done
