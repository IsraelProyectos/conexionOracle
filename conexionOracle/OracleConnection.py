import clr
import System
clr.AddReference("System.Data")

from System.Data import DataSet
from System.Data.OleDb import OleDbConnection, OleDbDataAdapter, OleDbCommand


class class1(object):

    def crearLista(self):
            #WORK_SKO/WORK_SKO@bvn002b.bbdo.local/PRDBATCH
            conStr = "Provider=MSDAORA.1;Data Source=PRDBATCH;User Id=WORK_SKO;Password=WORK_SKO;"

            con = OleDbConnection(conStr)

            query = "SELECT * FROM EXCEL_SENDER_PARAMETERS"

            adapter = OleDbDataAdapter(query, con)
            ds = DataSet()
            con.Open()

            adapter.Fill(ds, "t1")

            lista = [ ]
            
            for i in range(ds.Tables["t1"].Rows.Count):
                
                registro = [ ]
                registro.append(ds.Tables["t1"].Rows[i][0])
                registro.append(ds.Tables["t1"].Rows[i][4])
                registro.append(ds.Tables["t1"].Rows[i][6])
                lista.append(registro)
            

                
            return lista

            con.Close()





