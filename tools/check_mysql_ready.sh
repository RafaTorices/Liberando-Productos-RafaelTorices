while true; do
    if pgrep -x mysqld >/dev/null; then
        echo "MySQL is running."
        break
    else
        echo "MySQL is not running, waiting 10 seconds to retry..."
        sleep 10
    fi
done
