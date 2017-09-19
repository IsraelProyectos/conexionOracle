import clr
import System
clr.AddReference("System.Data")

from System.Data import DataSet
from System.Data.OleDb import OleDbConnection, OleDbDataAdapter, OleDbCommand


class class1(object):

    
    #WORK_SKO/WORK_SKO@bvn002b.bbdo.local/PRDBATCH
    conStr = "Provider=MSDAORA.1;Data Source=PRDBATCH;User Id=WORK_SKO;Password=WORK_SKO;"

    con = OleDbConnection(conStr)

    query = "SELECT * FROM EXCEL_SENDER_PARAMETERS"

    adapter = OleDbDataAdapter(query, con)
    ds = DataSet()
    con.Open()

    adapter.Fill(ds, "t1")

    

    for i in range(ds.Tables["t1"].Rows.Count -1):
        uno = ds.Tables["t1"].Rows[i][0]
        dos = ds.Tables["t1"].Rows[i][1]
        tres = ds.Tables["t1"].Rows[i][2]

    def dat(self):
        for registro in ds:
            uno = registro

    def saludo(self):
        return "hola"
        

    con.Close()





