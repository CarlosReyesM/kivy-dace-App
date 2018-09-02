from kivy.lang import Builder
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.scatter import Scatter
from kivy.uix.gridlayout import GridLayout

Builder.load_string('''
#: import random random  
<dadosScreen>:
	GridLayout:
		cols:1
        GridLayout:
        	cols:2
        	size_hint_y: 0.6
            Label:
                id: my_label
                text: "Tira un dado!"
                font_size: 60
                center:(90,500)
                color:(0.5,0.7,0.8,1)
            Image:
                id: my_image
                source: "Dices.jpg"
        GridLayout:
        	cols: 2
            Button:
                text: "1D100"
                color:(1,0.2,1,1)
                font_size: 60
                on_press: 
                    my_image.source = "1D100.png"
                    my_label.color = (1,0.2,1,1)
                    my_label.text = "Resultado "+ str(random.randint(1,100))
            Button:
                text: "1D10"
                color:(0.5,0.2,0.4,1)
                font_size: 60
                on_press: 
                    my_label.text = "Resultado "+str(random.randint(1,10))
                    my_image.source = "1D10.jpg"
                    my_label.color = (0.5,0.2,0.4,1)
            Button:
                text: "1D20"
                color:(0.8,0.7,1,1)
                font_size: 60
                on_press: 
                    my_label.text = "Resultado "+str(random.randint(1,20))
                    my_image.source = "1D20-2.jpg"
                    my_label.color = (0.8,0.7,1,1)
            Button:
                text: "1D12"
                color:(0,0.7,0.6,1)
                font_size: 60
                on_press: 
                    my_label.text = "Resultado "+str(random.randint(1,12))
                    my_image.source = "1D12.jpg"
                    my_label.color = (0,0.7,0.6,1)
            Button:
                text: "1D8"
                color:(1,0.2,0.2,1)
                font_size: 60
                on_press:
                    my_label.text = "Resultado "+str(random.randint(1,8))
                    my_image.source = "1D8.jpg"
                    my_label.color = (1,0.2,0.2,1)    
            Button:
                text: "1D6"
                color:(0.3,0.8,0.4,1)
                font_size: 60
                on_press: 
                    my_label.text = "Resultado "+str(random.randint(1,6))
                    my_image.source = "1D6.jpg"
                    my_label.color = (0.3,0.8,0.4,1)
            Button:
                text: "1D4"
                color:(0.2,1,0.2,1)
                font_size: 60
                on_press: 
                    my_label.text = "Resultado "+str(random.randint(1,4))
                    my_image.source = "1D4.jpg" 
                    my_label.color = (0.2,1,0.2,1)  
            Button:
                text: "Quit"
                color:(0.2,0.8,0.2,1)
                font_size: 60
                on_press: 
                    app.stop()
''')

class dadosScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(dadosScreen(name= "dados1"))

class misDadosApp(App):

    def build(self):
        return sm

if __name__ == "__main__":
    misDadosApp().run()