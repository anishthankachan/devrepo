=IFERROR(
    LOOKUP(
        2,
        1 / (ISNUMBER(SEARCH(LOWER(A2), LOWER(ABC!B2:B1000)))),
        LET(
            matched_abc_role_full, INDEX(ABC!C2:C1000, MATCH(TRUE, ISNUMBER(SEARCH(LOWER(A2), LOWER(ABC!B2:B1000))), 0)),
            extracted_abc_role, IF(ISNUMBER(FIND(": ", matched_abc_role_full)), MID(matched_abc_role_full, FIND(": ", matched_abc_role_full) + 2, 255), matched_abc_role_full),
            first_5_src_role, LEFT(UPPER(D2), 5),
            first_5_abc_role, LEFT(UPPER(extracted_abc_role), 5),
            IF(
                EXACT(first_5_src_role, first_5_abc_role),
                "Match: " & extracted_abc_role,
                ""
            )
        )
    ),
    "No Match"
)


=IFERROR(
    LOOKUP(
        2,
        1 / (ISNUMBER(SEARCH(LOWER(A2), LOWER(ABC!B2:B1000)))),
        LET(
            matched_abc_role, INDEX(ABC!C2:C1000, MATCH(TRUE, ISNUMBER(SEARCH(LOWER(A2), LOWER(ABC!B2:B1000))), 0)),
            extracted_abc_role, IF(ISNUMBER(FIND(": ", matched_abc_role)), MID(matched_abc_role, FIND(": ", matched_abc_role) + 2, 255), matched_abc_role),
            IF(
                EXACT(LEFT(UPPER(D2), 5), LEFT(UPPER(extracted_abc_role), 5)),
                "Match: " & extracted_abc_role,
                ""
            )
        )
    ),
    "No Match"
)


=IFERROR(INDEX(ABC!C2:C1000, MATCH(TRUE, ISNUMBER(FIND(LOWER(A2), LOWER(ABC!B2:B1000))), 0)), "No Email Match")


=IFERROR(INDEX(ABC!C2:C1000, MATCH(TRUE, ISNUMBER(SEARCH(LOWER(A2), LOWER(ABC!B2:B1000))), 0)), "No Email Match")


=IFERROR(
    LOOKUP(
        2,
        1 / (ISNUMBER(SEARCH(LOWER(A2), LOWER(ABC!B2:B1000)))),
        IF(
            EXACT(
                LEFT(UPPER(D2), 5),
                LEFT(UPPER(MID(INDEX(ABC!C2:C1000, MATCH(TRUE, ISNUMBER(SEARCH(LOWER(A2), LOWER(ABC!B2:B1000))), 0)), FIND(": ", INDEX(ABC!C2:C1000, MATCH(TRUE, ISNUMBER(SEARCH(LOWER(A2), LOWER(ABC!B2:B1000))), 0))) + 2, 255)), 5)
            ),
            "Match: " & MID(INDEX(ABC!C2:C1000, MATCH(TRUE, ISNUMBER(SEARCH(LOWER(A2), LOWER(ABC!B2:B1000))), 0)), FIND(": ", INDEX(ABC!C2:C1000, MATCH(TRUE, ISNUMBER(SEARCH(LOWER(A2), LOWER(ABC!B2:B1000))), 0))) + 2, 255),
            ""
        )
    ),
    "No Match"
)


=IFERROR(
    LOOKUP(
        2,
        1 / (ISNUMBER(SEARCH(LOWER(A2), LOWER(ABC!B2:B1000)))),
        IF(
            EXACT(
                LEFT(UPPER(D2), 5),
                LEFT(UPPER(INDEX(ABC!C2:C1000, MATCH(TRUE, ISNUMBER(SEARCH(LOWER(A2), LOWER(ABC!B2:B1000))), 0))), 5)
            ),
            "Match: " & INDEX(ABC!C2:C1000, MATCH(TRUE, ISNUMBER(SEARCH(LOWER(A2), LOWER(ABC!B2:B1000))), 0)),
            ""
        )
    ),
    "No Match"
)



=IFERROR(
    LOOKUP(
        2,
        1 / (ISNUMBER(SEARCH(LOWER(A1), LOWER(ABC!B:B)))),
        IF(
            EXACT(
                LEFT(UPPER(D1), 5),
                LEFT(UPPER(INDEX(ABC!C:C, ROW(INDEX(ABC!B:B, MATCH(TRUE, ISNUMBER(SEARCH(LOWER(A1), LOWER(ABC!B:B))), 0))))), 5)
            ),
            "Match: " & INDEX(ABC!C:C, ROW(INDEX(ABC!B:B, MATCH(TRUE, ISNUMBER(SEARCH(LOWER(A1), LOWER(ABC!B:B))), 0)))),
            ""
        )
    ),
    "No Match"
)


=IFERROR(
    IF(
        SUMPRODUCT(--ISNUMBER(SEARCH(LOWER(A1), LOWER(ABC!B:B))))>0,
        LET(
            matched_row, MATCH(TRUE, INDEX(ISNUMBER(SEARCH(LOWER(A1), LOWER(ABC!B:B))), 0), 0),
            abc_role, INDEX(ABC!C:C, matched_row),
            IF(
                EXACT(LEFT(UPPER(D1), 5), LEFT(UPPER(abc_role), 5)),
                "Match: "&abc_role,
                "No Match"
            )
        ),
        "No Match"
    ),
    "No Match"
)





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

