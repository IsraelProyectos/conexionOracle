import wpf
import clr
import OracleConnection
clr.AddReference("System.Drawing")
clr.AddReference("System.Windows.Forms")
from System.Windows.Forms import Application, Button, Form, Label
from System.Windows import Application, Window


class MyWindow(Window):
    def __init__(self):
        
        wpf.LoadComponent(self, 'conexionOracle.xaml')
        oc = OracleConnection.class1()
        self.label1.Content = "Hola"

        
if __name__ == '__main__':
    Application().Run(MyWindow())
