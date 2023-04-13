import sqlite3
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.metrics import dp
from kivymd.uix.tab import MDTabsBase
from kivymd.app import MDApp
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.icon_definitions import md_icons
from kivy.properties import StringProperty
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList
from kivymd.uix.button import MDRaisedButton
from kivymd.font_definitions import fonts
from kivymd.icon_definitions import md_icons
from kivymd.uix.card import MDCardSwipe
import datetime
from kivymd.uix.screen import MDScreen
from kivymd.uix.chip import MDChip
from kivy.animation import Animation
from kivy.factory import Factory
from kivymd.uix.menu import MDDropdownMenu
from kivy.clock import Clock
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineListItem
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.list import ThreeLineListItem
from kivymd.uix.button import MDFlatButton
import webbrowser
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.button import MDRaisedButton
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivy.core.window import Window
from kivy.core.window import Window
import sqlite3
import hashlib
from kivy.uix.modalview import ModalView
from kivy.lang import Builder
from kivymd.uix.list import MDList
from kivymd import images_path
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivymd.toast import toast
from kivy.core.window import Window
from kivymd.utils.fitimage import FitImage
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.theming import ThemeManager
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivymd.uix.bottomsheet import MDGridBottomSheet
from kivy.uix.anchorlayout import AnchorLayout
from kivy.lang.builder import Builder
from kivymd.uix.button import MDTextButton
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.snackbar import Snackbar
from kivy.factory import Factory
from kivymd.uix.button import MDIconButton

Window.size = (480, 800)


class ContentNavigationDrawer(FloatLayout):
    screen_manager = ObjectProperty()



def md5sum(value):
    return hashlib.md5(value.encode()).hexdigest()


with sqlite3.connect('database.db') as db:
    cursor = db.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        login VARCHAR(15),
        password VARCHAR(20),
        name TEXT,
        age TEXT

)
    """

    cursor.executescript(query)

with sqlite3.connect('search-base.db') as fut:
    db = fut.cursor()
    table = """
    CREATE TABLE IF NOT EXISTS search(
        fio TEXT,
        kvant TEXT,
        photo TEXT,
        op TEXT,
        pn1 TEXT,
        pn2 TEXT,
        vt1 TEXT,
        vt2 TEXT,
        cr1 TEXT,
        cr2 TEXT,
        cht1 TEXT,
        cht2 TEXT,
        pt1 TEXT,
        pt2 TEXT,
        cb1 TEXT,
        cb2 TEXT,
        ob TEXT

)
    """
    db.executescript(table)


class sDrawer(MDFloatLayout):
    pass


class TravelGO(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_file("kivy.kv")

    def screen(self, sed):
        self.root.ids.screen_manager.current = sed

    def registration(self):
        login = self.root.ids.log.text
        password = self.root.ids.pase.text
        name = self.root.ids.nameas.text
        age = self.root.ids.age.text
        otch = self.root.ids.otchims.text
        famal = self.root.ids.famalis.text

        fio = f"{age, otch, famal}"
        try:
            db = sqlite3.connect("database.db")
            cursor = db.cursor()

            db.create_function("md5", 1, md5sum)

            cursor.execute("SELECT login FROM users WHERE login = ?", [login])

            if cursor.fetchone() is None:
                values = [login, password, fio, age]
                cursor.execute("INSERT INTO users(login, password, name, age) VALUES(?,md5(?),?,?)", values)
                toast("Создали акаунт")
                self.root.ids.screen_manager.current = "Enter"
                db.commit()
            else:
                toast("Tакой логин уже есть")

        except sqlite3.Error as e:
            print("Error", e)
        finally:
            cursor.close()
            db.close()

    def log_in(self):
        login = self.root.ids.login.text
        password = self.root.ids.password.text
        if login == 'admin':
            if password == '1234':
                toast("Здраствуйте Admin")
                self.root.ids.screen_manager.current = "admin"
        else:
            try:
                db = sqlite3.connect("database.db")
                cursor = db.cursor()
                db.create_function("md5", 1, md5sum)
                cursor.execute("SELECT login FROM users WHERE login = ?", [login])
                if cursor.fetchone() is None:
                    toast("Такого логина не существует")
                else:
                    cursor.execute("SELECT login FROM users WHERE login = ? AND password = md5(?)", [login, password])
                    if cursor.fetchone() is None:
                        toast("Пороль не верный")
                    else:
                        toast("Вы вошли")
                        self.root.ids.screen_manager.current = "search"
            except sqlite3.Error as e:
                print('Error, e')
            finally:
                cursor.close()
                db.close()


TravelGO().run()