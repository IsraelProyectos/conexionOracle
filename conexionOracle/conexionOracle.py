import wpf
import clr
import OracleConnection
clr.AddReference("System.Drawing")
clr.AddReference("System.Windows.Forms")
from System.Windows.Forms import Application, Button, Form, Label, DataGrid
from System.Windows import Application, Window


class MyWindow(Window):
    def __init__(self):
        
        wpf.LoadComponent(self, 'conexionOracle.xaml')
        oc = OracleConnection.class1()
        lista = oc.crearLista()
        
        
        
        for registro in lista:
            for dato in registro:
               DataGrid.datagrid1.CurrentCell

        
if __name__ == '__main__':
    Application().Run(MyWindow())
