from kivy.app import App
from kivy.uix.gridlayout import GridLayout

from kivy.lang import Builder



class Calculator_Grid(GridLayout,Screen):
    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"





kv = Builder.load_file("calculator.kv")

class Calculator_App(App):
    def build(self):
        return Calculator_Grid()
if __name__ =="__main__":
    Calculator_App().run()