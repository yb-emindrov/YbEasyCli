#TODO sysprocs need many more test cases
#   for regular user test cases the sysview procedures need to be installed
map_out=[{ 'regex' : re.compile(r'\d+'), 'sub' : 'X' }
         , { 'regex' : re.compile(r' +'), 'sub' : ' ' }
         , { 'regex' : re.compile(r'-+'), 'sub' : '-' }]

test_cases = [
    test_case(
        cmd="""yb_sysprocs_column.py @{argsdir}/db1_su --database_in {db1} {db2} --table_like '%C%'"""
        , exit_code=0
        , stdout="""db         rel  rel     schema    rel       col  col     col     nullable    encrypted
name        id  type    name      name       id  name    type
-------  -----  ------  --------  ------  -----  ------  ------  ----------  -----------
{db1}  61452  table   Prod      C1_t        1  Col1    int4    t
{db1}  61470  view    Prod      C1_v        1  Col1    int4    t
{db2}  61543  table   Prod      C1_t        1  Col1    int4    t
{db2}  61561  view    Prod      C1_v        1  Col1    int4    t"""
        , stderr="", map_out=map_out)
]