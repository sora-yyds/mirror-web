#!/bin/bash
web=/home/sora/mirror-web
disks="/ /home/sora/mirror-web"

while true; do
        python3 /home/sora/mirror-web/geninfo/z-geninfo/genisolist.py 2>/dev/null > $web/static/status/isoinfo.json
        echo -n "[" > $web/static/status/disk.json
        df -B 1k --output="size,used" $disks  | awk '{if (FNR==1) ; else {if (FNR>2) printf ","; printf "{\"total_kb\":%s,\"used_kb\":%s}", $1, $2;}}' >> $web/static/status/disk.json
        echo -n "]" >> $web/static/status/disk.json
        sleep 15s
done