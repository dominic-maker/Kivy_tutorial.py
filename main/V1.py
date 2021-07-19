from os import listdir, path

from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget

Builder.load_string('''
<MusicPlayer>:
     Canvas.before:
        color:
            rgba: 0, 0, 1,1
        Rectangle:
            pos:self.pos
            size.self.size

    TextInput:
            id:direct
            pos: 0, root.top-35

    Button:
            id:searchBtn
            text:'Browse'
            size:200,35
            background_color: 0,0,1,1
            pos:root.width-200,root.top-35
            on_release:root.getSongs()

    ScrollView:
            size_hint:None,None
            size:root.width,root.height=135
            pos:0,100
            GridLayout:
                id:scroll
                cols:2
                spacing:10
                size_hint_y:None
                row_force_default:True
                row_default_height:40

    GridLayout:
            rows:1
            pos:0,50
            size:root.width,50
            Button:
                text:'<=='
                background_color:1,1,1,1
            Button:
                id:now play
                text:'Now Playing'
                pos:0,0
                size:root.width,50
                background_color:1,1,1,1

            Label:
                id:status
                text:''
                center:root.center

<ChooseFile>:
        Canvas.before:
            color:
                rgba:0,0,.4,1
            Rectangle:
                pos:self.pos
                size:self:size
        BoxLayout:
            size:root.size
            pos:root.pos
            orientation:"vertical"
            FileChooseIconView:
                id:fileChooser
            BoxLayout:
                size_hint_y:None
                height:30
                Button:
                    text:"Cancel"
                    background_color:0,.5,1,1
                    on_release:root.cancel()
                Button:
                    text:"Select Folder"
                    background_color:0,.5,1,1
                    on_release:root.select(fileChooser,path)

''')


class ChooseFile(FloatLayout):
    select = ObjectProperty(None)
    cancel = ObjectProperty(None)


class MusicPlayer(Widget):
    directory = ''
    nowPlaying = ''

    def getpath(self):
        try:
            f = open("save.data", "C:/")
            self.ids.direct.text = str(f.readline())
            f.close()
            self.ids.searchBtn.text = "scan"
            self.getsongs()
        except:
            self.ids.direct.text = ''

    def dismiss_Popup(self):
        pass

    def FileSelect(self):
        content = ChooseFile(select=self.select, cancel=self.dismiss_Popup)

        self_Popup = Popup(title="SelectFolder", Content=content, size_hint=(0.9, 0.9))
        self_Popup.open()

    def select(self, Path):
        self.directory = path
        self.ids.direct.text = self.directory
        self.ids.SearchBtn.text = "Scan"
        self.savePath(self.directory)
        self.getsongs()
        self.dismiss_Popup()

    def getSongs(self, fil=None):
        Songs = []
        self.directory = self.ids.direct.text

        if self.directory == '':
            self.file.Select()
        if not self.directory.endswith('/'):
            self.directory += '/'

        if not path.exists(self.directory):
            self.ids.status.text = 'folder not found'
            self.ids.status.color = (1, 0, 0, 1)
        else:
            self.ids.status.text = ''
            self.ids.scroll.bind(minimum_height=self.ids.scroll.setter('height'))
            for fil in listdir(self.directory):
                if fil.endswith('.mp3'):
                    Songs.append(fil)
                if Songs == [] and self.directory != '':
                    self.ids.status.text = 'No Music Found'
                    self.ids.status.color = (1, 0, 0, 1)
        Songs.sort()
        for Songs in Songs:
            def playSong(bt):
                try:
                    self.nowPlaying.stop()
                except:
                    pass
                finally:
                    self.nowPlaying = SoundLoader.load(self.directory + bt.text + '.mp3')
                    self.nowPlaying.play()
                    self.ids.nowplay.text = bt.text

            btn = Button(text=Songs[:-4], on_press=playSong)
            icon = Button(size_hint_x=None, width=50, background_down='music icons/image.png')

            if Songs.index(Songs) % 2 == 0:
                btn.background_color = (1, 0, 1, 1)
            else:
                btn.background_color = (1, 0, 1, 1)

            self.ids.scroll.add_widget(icon)
            self.ids.scroll.add_widget(btn)


class KVMusicApp(App):
    def build(self):
        music = MusicPlayer()
        music.getpath()
        return music

    def on_pause(self):
        return True

    def on_resume(self):
        pass


if __name__ == "__main__":
    KVMusicApp().run()
