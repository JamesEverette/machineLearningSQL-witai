import pypyodbc as pyodbc

connection_string = 'Driver={ODBC Driver 13 for SQL Server};Server=localhost;Database=policyDatabase;UID=user1;PWD=testPassword123!;'#trusted_connection=yes;')
db = pyodbc.connect(connection_string)
cursor = db.cursor()

def query(select, where, table):

	query = select + ' FROM [policyDatabase].[dbo].[policyTable] ' + where
	print(query)

	cursor.execute(query + ';')

	return cursor.fetchone()