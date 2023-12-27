while true; do
    if pgrep -x mysqld >/dev/null; then
        echo "MySQL is running."
        sleep 30
        break
    else
        echo "MySQL is not running, waiting 10 seconds to retry..."
        sleep 10
    fi
done
