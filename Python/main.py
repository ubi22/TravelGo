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
from kivymd.uix.list import OneLineIconListItem
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
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
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty

from kivymd.uix.list import OneLineIconListItem
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
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

with sqlite3.connect('databaseadmin.db') as db:
    cursor = db.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS admin(
        id INTEGER PRIMARY KEY,
        login VARCHAR(15),
        password VARCHAR(20),
        email TEXT,
        name TEXT,
        phone TEXT

)
    """

    cursor.executescript(query)

with sqlite3.connect('database.db') as db:
    cursor = db.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        login VARCHAR(15),
        password VARCHAR(20),
        email TEXT,
        name TEXT

)
    """

    cursor.executescript(query)

with sqlite3.connect('search-base.db') as fut:
    db = fut.cursor()
    table = """
    CREATE TABLE IF NOT EXISTS search(
        name TEXT,
        opis TEXT,
        num TEXT,
        gmail TEXT,
        h1 TEXT,
        h2 TEXT,
        h3 TEXT,
        h4 TEXT,
        h5 TEXT,
        camera TEXT,
        login TEXT,
        sale TEXT
        
)
    """
    db.executescript(table)


class sDrawer(MDFloatLayout):
    pass


v = None
class TravelGO(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=True,
        )

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_file("kivy.kv")

    def screen(self, sed):
        self.root.ids.screen_manager.current = sed

    def file_manager_open(self, file):
        global v
        if file == 0:
            self.file_manager.show('/')
            v = "prou"
        elif file == 1:
            self.file_manager.show('/')
            v = "proa"
        elif file == 2:
            self.file_manager.show('/')
            v = "h1"
        elif file == 3:
            self.file_manager.show('/')
            v = "h2"
        elif file == 4:
            self.file_manager.show('/')
            v = "h3"
        elif file == 5:
            self.file_manager.show('/')
            v = "h4"
        elif file == 6:
            self.file_manager.show('/')
            v = "h5"
        elif file == 7:
            self.file_manager.show('/')
            v = "protravel"
        self.manager_open = True

    def select_path(self, path):
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;
        '''
        global v
        if v == "prou":
            self.root.ids.iconhome.icon = f"{path}"
        elif v == "proa":
            self.root.ids.iconadmin.icon = f"{path}"
        elif v == "h1":
            self.root.ids.h1.source = f"{path}"
        elif v == "h2":
            self.root.ids.h2.source = f"{path}"
        elif v == "h3":
            self.root.ids.h3.source = f"{path}"
        elif v == "h4":
            self.root.ids.h4.source = f"{path}"
        elif v == "h5":
            self.root.ids.h5.source = f"{path}"
        elif v == "protravel":
            self.root.ids.camera.source = f"{path}"
        self.exit_manager()

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True

    def registrationadmin(self):
        login = self.root.ids.logincom.text
        password = self.root.ids.pasecom.text
        name = self.root.ids.namecom.text
        try:
            db = sqlite3.connect("databaseadmin.db")
            cursor = db.cursor()

            db.create_function("md5", 1, md5sum)

            cursor.execute("SELECT login FROM admin WHERE login = ?", [login])

            if cursor.fetchone() is None:
                values = [login, password, name]
                cursor.execute("INSERT INTO admin(login, password, name) VALUES(?,md5(?),?)", values)
                toast("Создали акаунт")
                self.root.ids.screen_manager.current = "enter"
                db.commit()
            else:
                toast("Tакой логин уже есть")

        except sqlite3.Error as e:
            print("Error", e)
        finally:
            cursor.close()
            db.close()

    def registrationuser(self):
        login = self.root.ids.log.text
        password = self.root.ids.pase.text
        email = self.root.ids.email.text
        name = self.root.ids.name.text
        try:
            db = sqlite3.connect("database.db")
            cursor = db.cursor()

            db.create_function("md5", 1, md5sum)

            cursor.execute("SELECT login FROM users WHERE login = ?", [login])

            if cursor.fetchone() is None:
                values = [login, password, email, name]
                cursor.execute("INSERT INTO users(login, password, email, name) VALUES(?,md5(?),?,?)", values)
                toast("Создали акаунт")
                self.root.ids.screen_manager.current = "enter"
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

        try:
            db = sqlite3.connect("database.db")
            cursor = db.cursor()
            db.create_function("md5", 1, md5sum)
            cursor.execute("SELECT login FROM users WHERE login = ?", [login])
            if cursor.fetchone() is None:
                ss = sqlite3.connect("databaseadmin.db")
                cur = ss.cursor()
                ss.create_function("md5", 1, md5sum)
                cur.execute("SELECT login FROM admin WHERE login = ?", [login])
                if cur.fetchone() is None:
                    toast("Такого логина не существует")
                else:
                    cur.execute("SELECT login FROM admin WHERE login = ? AND password = md5(?)", [login, password])
                    if cur.fetchone() is None:
                        toast("Пороль не верный")
                    else:
                        toast("Вы вошли")
                        self.root.ids.screen_manager.current = "admin"
                        self.tyr()
            else:
                cursor.execute("SELECT login FROM users WHERE login = ? AND password = md5(?)", [login, password])
                if cursor.fetchone() is None:
                    toast("Пороль не верный")
                else:
                    toast("Вы вошли")
                    self.root.ids.screen_manager.current = "home"
        finally:
            cursor.close()
            db.close()

    def create(self):
        name = self.root.ids.namet.text
        opis = self.root.ids.op.text
        h1 = self.root.ids.h1.source
        h2 = self.root.ids.h2.source
        h3 = self.root.ids.h3.source
        h4 = self.root.ids.h4.source
        h5 = self.root.ids.h5.source
        num = self.root.ids.phonea.text
        gmaila = self.root.ids.emaila.text
        camera = self.root.ids.camera.source
        login = self.root.ids.login.text
        sale = self.root.ids.sele.text
        try:
            fut = sqlite3.connect("search-base.db")
            searchs = fut.cursor()
            values = [name, opis, num, gmaila, h1, h2, h3, h4, h5, camera, login, sale]
            searchs.execute("INSERT INTO search(name, opis, num, gmail, h1, h2, h3, h4, h5, camera, login, sale) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",values)
            print(values)
            fut.commit()
            self.root.ids.screen_manager.current = "admin"
        except sqlite3.Error as e:
            print("Error", e)
    def tyr(self):
        try:
            poisk = self.root.ids.login.text
            fut = sqlite3.connect("search-base.db")
            searchs = fut.cursor()
            searchs.execute(f'''SELECT * FROM search WHERE login LIKE '%{poisk}%';''')
            three_results = searchs.fetchall()
            if len(three_results) == 0:
                toast('Такого преподователя нет')
            else:
                s = len(three_results)
                for i in range(s):
                    # conten = sDrawer()
                    # a = self.root.ids.fer.text
                    # f = self.root.ids.hy.text
                    # d = self.root.ids.ger.text
                    # if self.fyx == 0:
                        # conten.add_widget(FitImage(source=self.pomi, size_hint={0.25, 0.85}))
                        # conten.add_widget(ThreeLineListItem(text=f'{f}', secondary_text=f"{a} {d}"))
                        # self.root.ids.md_list.add_widget(conten)
                    pass

        except sqlite3.Error as e:
                print("Error", e)

TravelGO().run()