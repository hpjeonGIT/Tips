# Installing oracle odbc connection in Linux
- download and unzip instantclient for Linux of basic, jdbc, odbc, sdk, sqlplus, tool into an install folder
- May need tnsnames.ora and sql.ora at install_location/network/admin
- export TNS_ADMIN=__install_folder__/network/admin
- export ORACLE_HOME=__install_folder__
- Run odbcinst -j and check if odbcinst is for local or central. If central odbcinst is required, install unixODBC at a central location. 
- $PATH must have the central unixODBC/bin in the head. If the local odbcinst is executed prior to the central odbcinst, local driver will be initiated
- Edit unixODBC/etc/odbcinst.ini as:

[OracleDB]

Description=Oracle Unicode driver

Driver=/opt/oracle_instant_client/18.3/libsqora.so.18.1

Driver64=/opt/oracle_instant_client/18.3/libsqora.so.18.1

UsageCount=1

FileUsage=1


# In Python
- Install pyodbc. May need > gcc4.x. gcc8.2 works.
- python3
- import pyodbc
- conn = pyodbc.connect("DRIVER=OracleDB; DBQ=some_name_as_shown_in_tnsnames.ora; UID=***; PWD=***)
- cursor = conn.cursor()
- cursor.execute("SELECT USERNAME FROM ALL_USERS")
- ans = cursor.fetchall()
- print(ans)
- del(cursor)
- conn.close()

# In R
- Install RODBC
- R
- library(RODBC)
- conn <- odbcDriverConnect("Driver=OracleDB; Dbq=some_name_as_shown_in_tnsnames.ora; uid=***; pwd=***)
- listSchema <- sqlQuery(conn, "SELECT USERNAME FROM ALL_USERS")
- print(listSchema)
- odbcClose(conn)
