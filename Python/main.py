import sqlite3
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.metrics import dp
import requests
import json
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
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from kivymd.icon_definitions import md_icons
from kivymd.uix.list import OneLineListItem
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.list import ThreeLineIconListItem
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
from kivy.animation import Animation
from kivy.core.window import Window
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
from kivymd.utils.fitimage import FitImage
from kivymd.uix.screen import MDScreen
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
from bs4 import BeautifulSoup
import requests
import sqlite3
import time
Window.size = (480, 800)
API = '6c39b074-59ea-4ce3-8924-c1b26f5e9137'


class ContentNavigationDrawer(FloatLayout):
    screen_manager = ObjectProperty()


def md5sum(value):
    return hashlib.md5(value.encode()).hexdigest()


with sqlite3.connect('DBBrowser/databaseadmin.db') as db:
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

with sqlite3.connect('DBBrowser/comment.db') as db:
    cursor = db.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS admin(
        id INTEGER PRIMARY KEY,
        user TEXT,
        text TEXT
    

)
    """

    cursor.executescript(query)

with sqlite3.connect('DBBrowser/mydb.db') as db:
    cursor = db.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS search(
        id INTEGER,
        name TEXT,
        price TEXT,
        description TEXT,
        img TEXT,
        PRIMARY KEY(ID)
)
    """

with sqlite3.connect('DBBrowser/housebase.db') as db:
    cursor = db.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        name TEXT
)
    """

    cursor.executescript(query)

with sqlite3.connect('DBBrowser/cafebase.db') as db:
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

with sqlite3.connect('DBBrowser/merpb.db') as fut:
    db = fut.cursor()
    table = """
    CREATE TABLE IF NOT EXISTS search(
        name TEXT,
        kyda TEXT,
        budget TEXT,
        user TEXT

)
    """
    db.executescript(table)

with sqlite3.connect('DBBrowser/database.db') as fut:
    db = fut.cursor()
    table = """
    CREATE TABLE IF NOT EXISTS users(
        login TEXT, 
        password TEXT,
        email TEXT,
        name TEXT

)
    """
    db.executescript(table)

with sqlite3.connect('DBBrowser/search-base.db') as fut:
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


class sDrawer(BoxLayout):
    btn = ObjectProperty(None)
    def save_user_name(self):
        self.remove_widget(self.btn)
class CustomOneLineIconListItem(OneLineIconListItem):
    icon = StringProperty()
class msdDrawer(BoxLayout):
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
        self.se = []
        self.conten = sDrawer()


    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_file("kivy.kv")

    def screen(self, sed):
        self.root.ids.screen_manager.current = sed
    def eventsname(self):
        search = self.root.ids.login.text
        fut = sqlite3.connect("DBBrowser/merpb.db")
        searchs = fut.cursor()
        searchs.execute(f'''SELECT * FROM search WHERE user LIKE '%{search}%';''')
        three_results = searchs.fetchall()
        s = len(three_results)
        print(s)
        for i in range(s):
            conten = sDrawer()
            self.se.append(
                conten.add_widget(
                    ThreeLineIconListItem(
                        text=f'{three_results[i][0]}',
                        secondary_text=f"{three_results[i][1]}",
                        tertiary_text=f"{three_results[i][2]}",
                        on_press=lambda x: self.events_search(x)
                    )
                )
            )
            self.root.ids.ms.add_widget(conten)


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
            db = sqlite3.connect("DBBrowser/databaseadmin.db")
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
            db = sqlite3.connect("DBBrowser/database.db")
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
            db = sqlite3.connect("DBBrowser/database.db")
            cursor = db.cursor()
            db.create_function("md5", 1, md5sum)
            cursor.execute("SELECT login FROM users WHERE login = ?", [login])
            if cursor.fetchone() is None:
                ss = sqlite3.connect("DBBrowser/databaseadmin.db")
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
                    self.eventsname()
                    self.root.ids.screen_manager.current = "events"
        finally:
            cursor.close()
            db.close()
    def eventscreate(self):
        name = self.root.ids.nameevents.text
        go = self.root.ids.eventsgo.text
        budget = self.root.ids.eventsmany.text
        user = self.root.ids.login.text
        mif = self.root.ids.eventsgo.text
        mydb = sqlite3.connect("DBBrowser/mydb.db")
        mydbs = mydb.cursor()
        fut = sqlite3.connect("DBBrowser/merpb.db")
        searchs = fut.cursor()
        values = [name, go, budget, user]
        searchs.execute("INSERT INTO search(name, kyda, budget, user) VALUES(?,?,?,?)", values)
        self.root.ids.screen_manager.current = "home"
        mydbs.execute(f'''SELECT * FROM search WHERE name LIKE '%{mif}%';''')
        three_results = mydbs.fetchall()
        self.root.ids.rv.clear_widgets()
        if len(three_results) == 0:
            toast('Такого преподователя нет')
        else:
            s = len(three_results)
            if s >= 30:
                s = 30
            print(s)
            for i in range(s):
                conten = sDrawer()
                conten.add_widget(
                    FitImage(
                        source=f"{three_results[i][4]}",
                        size_hint={0.4, 0.77}
                    )
                )
                self.se.append(
                    conten.add_widget(
                        ThreeLineIconListItem(
                            text=f'{three_results[i][1]}',
                            secondary_text=f"{three_results[i][3]}",
                            tertiary_text=f"{three_results[i][2]}",
                            on_press=lambda x: self.screen_travel(x)
                        )
                    )
                )
                self.root.ids.rv.add_widget(conten)
        fut.commit()
    def events_search(self, x):
        fut = sqlite3.connect("DBBrowser/mydb.db")
        searchs = fut.cursor()
        self.root.ids.screen_manager.current = 'home'
        searchs.execute(f'''SELECT * FROM search WHERE name LIKE '%{x.secondary_text}%';''')
        three_results = searchs.fetchall()
        self.root.ids.rv.clear_widgets()
        if len(three_results) == 0:
            toast('Такого преподователя нет')
        else:
            s = len(three_results)
            if s >= 30:
                s = 30
            print(s)
            for i in range(s):
                conten = sDrawer()
                conten.add_widget(
                    FitImage(
                        source=f"{three_results[i][4]}",
                        size_hint={0.4, 0.77}
                    )
                )
                self.se.append(
                    conten.add_widget(
                        ThreeLineIconListItem(
                            text=f'{three_results[i][1]}',
                            secondary_text=f"{three_results[i][3]}",
                            tertiary_text=f"{three_results[i][2]}",
                            on_press=lambda x: self.screen_travel(x)
                        )
                    )
                )
                self.root.ids.rv.add_widget(conten)
    def search_news(self, x = 0):
        TEXT = 'Новочебоксарск, кафе'
        # колличество запросов, то есть заведений которых код выдаст, максимум 50
        RESULTS = 10

        response = requests.get(
            f'https://search-maps.yandex.ru/v1/?apikey={API}&text={TEXT}&lang=ru_RU&results={RESULTS}')
        text = json.loads(response.text)
        print(len(text['features']))
        for i in text['features']:
            # тут по порядку: название, вид, описание, адресс, номер, время работы. Делай с ними что хочешь в этом цикле
            name = i['properties']['CompanyMetaData']['name']
            clas = i['properties']['CompanyMetaData']['Categories'][0]['name']
            description = i['properties']['description']
            address = i['properties']['CompanyMetaData']['address']
            phone = i['properties']['CompanyMetaData']['Phones'][0]['formatted']
            hours = i['properties']['CompanyMetaData']['Hours']['Availabilities']
            print(name, '\n', clas, '\n', description, '\n', address, '\n', phone, '\n', hours, '\n')
        if x == 0:
            search = self.root.ids.search_field.text
            self.root.ids.rv.clear_widgets()
        else:
            search = self.root.ids.search_field2.text
            self.root.ids.rv2.clear_widgets()
        fut = sqlite3.connect("DBBrowser/mydb.db")
        searchs = fut.cursor()
        searchs.execute(f'''SELECT * FROM search WHERE name LIKE '%{search}%';''')
        three_results = searchs.fetchall()

        if len(three_results) == 0:
            toast('Такого нет')
        else:
            s = len(three_results)
            print(s)
            if s > 30:
                s = 30
            print(s)
            for i in range(s):
                conten = sDrawer()
                self.se.append(
                    MDCard(
                        orientation="vertical",
                        size_hint=(.5, None),
                        height=ids.box_top.height + ids.box_bottom.height,
                        focus_behavior=True,
                        ripple_behavior=True,
                        pos_hint={"center_x": .5, "center_y": .5},
                        children=[
                            MDBoxLayout(
                                id='box_top',
                                spacing="20dp",
                                adaptive_height=True,
                            ),
                            FitImage(
                                source="/Users/macbookair/album.jpeg",
                                size_hint=(.3, None),
                                height=text_box.height,
                            ),
                            MDBoxLayout(
                                id='text_box',
                                orientation="vertical",
                                adaptive_height=True,
                                spacing="10dp",
                                padding=(0, "10dp", "10dp", "10dp"),
                            ),
                            MDLabel(
                                text="Ride the Lightning",
                                theme_text_color="Primary",
                                font_style="H5",
                                bold=True,
                                size_hint_y=None,
                                height=self.texture_size[1],
                            ),
                            MDLabel(
                                text="July 27, 1984",
                                size_hint_y=None,
                                height=self.texture_size[1],
                                theme_text_color="Primary",
                            ),
                            MDSeparator(),
                            MDBoxLayout(
                                id='box_bottom',
                                adaptive_height=True,
                                padding=("10dp", 0, 0, 0),
                            ),
                            MDLabel(
                                text="Rate this album",
                                size_hint_y=None,
                                height=self.texture_size[1],
                                pos_hint={"center_y": .5},
                                theme_text_color="Primary",
                            ),
                            MDIconButton(
                                icon='star'
                            ),
                        ]
                    )
                )
                if x == 0:
                    self.root.ids.rv.add_widget(conten)
                else:
                    self.root.ids.rv2.add_widget(conten)

    def screen_travel(self, x):
        fut = sqlite3.connect("DBBrowser/mydb.db")
        searchs = fut.cursor()
        searchs.execute(f'''SELECT * FROM search WHERE name LIKE '%{x.text}%';''')
        three_results = searchs.fetchall()
        if len(three_results) == 0:
            toast('Такого преподователя нет')
        else:
            self.root.ids.optravel.text = f"{three_results[0][3]}"
            self.screen("travela")
            self.root.ids.imagetravel.source = f"{three_results[0][4]}"
            self.root.ids.h1travel.source = f"{three_results[0][9]}"
            self.root.ids.h2travel.source = f"{three_results[0][5]}"
            self.root.ids.h3travel.source = f"{three_results[0][6]}"
            self.root.ids.h4travel.source = f"{three_results[0][7]}"
            self.root.ids.h5travel.source = f"{three_results[0][8]}"
            self.root.ids.phonetravel.text = f"7(987) 123-80-50"
            self.root.ids.emailtravel.text = f"zoom.main21@gmail.com"
            self.root.ids.nametravel.text = f"{three_results[0][1]}"
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
            fut = sqlite3.connect("DBBrowser/search-base.db")
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
            fut = sqlite3.connect("DBBrowser/search-base.db")
            searchs = fut.cursor()
            searchs.execute(f'''SELECT * FROM search WHERE login LIKE '%{poisk}%';''')
            three_results = searchs.fetchall()
            if len(three_results) == 0:
                toast('Такого преподователя нет')
            else:
                s = len(three_results)
                print(s)
                if s >= 30:
                    s = 30
                for i in range(s):
                    prconten = sDrawer()
                    prconten.add_widget(
                        FitImage(
                            source=f"{three_results[i][4]}", size_hint={0.25, 0.59}))
                    self.se.append(
                        prconten.add_widget(
                            ThreeLineIconListItem(
                                text=f'{three_results[i][0]}',
                                secondary_text=f"{three_results[i][1]}",
                                tertiary_text=f"{three_results[i][11]}",
                                on_press=lambda x: self.compiration(x) #self.compiration(
                                    # m=self.se.index(
                                    #     conten
                                    # )
                            )
                         )
                    )
                    self.root.ids.md_list.add_widget(prconten)


        except sqlite3.Error as e:
                print("Error", e)
    def data(self):
        anim = Animation(pos_hint=({"center_x": .5, "center_y": .5}))
        anim.start(self.root.ids.Enters)
    def compiration(self, x):
        fut = sqlite3.connect("DBBrowser/search-base.db")
        searchs = fut.cursor()
        searchs.execute(f'''SELECT * FROM search WHERE name LIKE '%{x.text}%';''')
        three_results = searchs.fetchall()
        if len(three_results) == 0:
            toast('Такого преподователя нет')
        else:
            self.root.ids.optravel.text = f"{three_results[0][1]}"
            self.screen("travela")
            self.root.ids.imagetravel.source = f"{three_results[0][9]}"
            self.root.ids.h1travel.source = f"{three_results[0][4]}"
            self.root.ids.h2travel.source = f"{three_results[0][5]}"
            self.root.ids.h3travel.source = f"{three_results[0][6]}"
            self.root.ids.h4travel.source = f"{three_results[0][7]}"
            self.root.ids.h5travel.source = f"{three_results[0][8]}"
            self.root.ids.phonetravel.text = f"{three_results[0][2]}"
            self.root.ids.emailtravel.text = f"{three_results[0][3]}"
            self.root.ids.nametravel.text = f"{three_results[0][0]}"

TravelGO().run()