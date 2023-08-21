from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.utils.fitimage import FitImage
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDSeparator
from kivymd.uix.button import MDIconButton
from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
<StarButton@MDIconButton>
    icon: "star"
    on_release: self.icon = "star-outline" if self.icon == "star" else "star"


MDScreen:

    MDCard:
        orientation: "vertical"
        size_hint: .5, None
        height: box_top.height + box_bottom.height
        focus_behavior: True
        ripple_behavior: True
        pos_hint: {"center_x": .5, "center_y": .5}

        MDBoxLayout:
            id: box_top
            spacing: "20dp"
            adaptive_height: True

            FitImage:
                source: "/Users/macbookair/album.jpeg"
                size_hint: .3, None
                height: text_box.height

            MDBoxLayout:
                id: text_box
                orientation: "vertical"
                adaptive_height: True
                spacing: "10dp"
                padding: 0, "10dp", "10dp", "10dp"

                MDLabel:
                    text: "Байкал"
                    theme_text_color: "Primary"
                    font_style: "H5"
                    bold: True
                    size_hint_y: None
                    height: self.texture_size[1]

                MDLabel:
                    id: gr
                    text: "Акция! На заезд 20.08.2023 - 24.08.2023 действует скидка. Стоимость тура — 55 200 руб./чел.В одном туре вы посетите территории курортов Архыза, Домбая, Теберды и региона Кубани. Увидите красивейшие места Архыза, Домбая, Теберды, Верхней Мары и Гумбаши и сделаете эксклюзивные фото. Отдохнете на берегу реликтового высокогорного озера и искупаться в его живой воде. Совместите автопробеги с горным треккингом и содержательными экскурсиями."
                    size_hint_y: None
                    height: self.texture_size[1]
                    theme_text_color: "Primary"
                MDLabel:
                    text: "54600R"
                    size_hint_y: None
                    theme_text_color: "Primary" 

        MDSeparator:

        MDBoxLayout:
            id: box_bottom
            adaptive_height: True
            padding: "10dp", 0, 0, 0

            MDLabel:
                text: "Rate this album"
                size_hint_y: None
                height: self.texture_size[1]
                pos_hint: {"center_y": .5}
                theme_text_color: "Primary"

            StarButton:
                on_press:
                    app.higer()
'''


class Test(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return(




Test().run()