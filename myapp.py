from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, RoundedRectangle
from kivy.core.window import Window
from kivy.metrics import dp


Window.size = (390, 700)
Window.clearcolor = (1, 0.78, 0.88, 1)


class CuteButton(Button):

    def __init__(self, bg_color, **kwargs):
        super().__init__(**kwargs)

        self.background_normal = ""
        self.background_color = (0, 0, 0, 0)

        with self.canvas.before:
            Color(*bg_color)

            self.shape = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[dp(20)]
            )

        self.bind(
            pos=self.update_shape,
            size=self.update_shape
        )

    def update_shape(self, *args):
        self.shape.pos = self.pos
        self.shape.size = self.size


class CuteCalculator(App):

    def build(self):

        main = BoxLayout(
            orientation="vertical",
            padding=dp(18),
            spacing=dp(12)
        )

        title = Label(
            text="♡ CUTE CALCULATOR ♡",
            font_size=25,
            bold=True,
            color=(0.55, 0.08, 0.25, 1),
            size_hint_y=0.10
        )

        main.add_widget(title)

        display = Label(
            text="0",
            font_size=42,
            bold=True,
            halign="right",
            valign="middle",
            color=(0.45, 0.05, 0.20, 1),
            size_hint_y=0.20
        )

        main.add_widget(display)

        buttons = GridLayout(
            cols=4,
            spacing=dp(9)
        )

        keys = [
            "C", "⌫", "%", "÷",
            "7", "8", "9", "×",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "♡", "0", ".", "="
        ]

        for key in keys:

            if key == "=":
                color = (1, 0.25, 0.55, 1)
            elif key in ["C", "⌫", "%", "÷", "×", "-", "+"]:
                color = (1, 0.45, 0.68, 1)
            else:
                color = (1, 0.62, 0.78, 1)

            button = CuteButton(
                bg_color=color,
                text=key,
                font_size=27,
                bold=True,
                color=(1, 1, 1, 1)
            )

            button.bind(
                on_press=lambda instance:
                self.press(instance.text, display)
            )

            buttons.add_widget(button)

        main.add_widget(buttons)

        footer = Label(
            text="✦ made with love ✦",
            font_size=16,
            bold=True,
            color=(0.65, 0.12, 0.35, 1),
            size_hint_y=0.08
        )

        main.add_widget(footer)

        return main

    def press(self, key, display):

        if key == "C":
            display.text = "0"

        elif key == "⌫":
            display.text = display.text[:-1] or "0"

        elif key == "=":

            try:
                expression = display.text
                expression = expression.replace("×", "*")
                expression = expression.replace("÷", "/")

                result = eval(expression)

                if isinstance(result, float) and result.is_integer():
                    result = int(result)

                display.text = str(result)

            except:
                display.text = "Oops ♡"

        elif key == "%":

            try:
                display.text = str(float(display.text) / 100)
            except:
                display.text = "Oops ♡"

        else:

            if display.text in ["0", "Oops ♡"]:
                display.text = key
            else:
                display.text += key


CuteCalculator().run()