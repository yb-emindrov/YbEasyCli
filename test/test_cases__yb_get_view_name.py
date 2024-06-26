test_cases = [
    test_case(
        cmd='yb_get_view_name.py @{argsdir}/db1 --schema dev --view a1_v'
        , exit_code=0
        , stdout='a1_v'
        , stderr='')

    , test_case(
        cmd=(
            'yb_get_view_name.py @{argsdir}/db1 --current_schema dev --schema '
            """'Prod' --view b1_v""")
        , exit_code=0
        , stdout='b1_v'
        , stderr=''),

    test_case(
        cmd=(
            "yb_get_view_name.py @{argsdir}/db1 --current_schema dev "
            """--schema Prod --view C1_v --database {db2} """)
        , exit_code=0
        , stdout='"C1_v"'
        , stderr=''),

    test_case(
        cmd=(
            "yb_get_view_name.py @{argsdir}/db1 --current_schema dev "
            """--schema Prod --view c1_v --database {db2} extra_pos_arg""")
        , exit_code=(0 if Common.is_windows else 1)
        , stdout=""
        , stderr="""yb_get_view_name.py: error: unrecognized arguments: extra_pos_arg
for complete help, execute: yb_get_view_name.py --help""")
]