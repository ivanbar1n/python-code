from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.fitimage import FitImage
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
class MyApp(MDApp):
    def build(self):
        self.counter = 0
        self.label =  Label(
                   text="",font_size='30sp'
        )
        return(
            MDScreen(
                FitImage(
                    source="newyear.png"
                ),
               self.label,
                Button(
                    text = "нажми на меня",
                    size_hint = (None,0.1) ,
                    size = (300,40),
                    pos = (250,200),
                    on_press=self.on_button_press
                ),

            )

        )

    def on_button_press(self, instance):
        self.counter += 1
        self.label.text = f"C новым годом,Алёна!"

if __name__ == "__main__":
    MyApp().run()