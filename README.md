
Run it on the old server

$WAS_HOME/bin/wsadmin.sh -username wasadmin -password password -f /tmp/export_full_config.py

Copy the exported files to the new server

scp -r /tmp/ws_config_export new_host:/tmp/

$WAS_HOME/bin/wsadmin.sh -username wasadmin -password password -f /tmp/import_full_config.py

Run it on the new server

$WAS_HOME/bin/wsadmin.sh -username wasadmin -password password -f /tmp/import_full_config.py


---

Step 3: Verify Migration

After import, restart WebSphere:

$WAS_HOME/bin/stopServer.sh server1 -username wasadmin -password password
$WAS_HOME/bin/startServer.sh server1

Check logs for errors:

tail -f $WAS_HOME/profiles/AppSrv01/logs/server1/SystemOut.log

