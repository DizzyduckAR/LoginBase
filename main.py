

import os.path
import json
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QStatusBar
from PyQt5.QtGui import QIcon, QMovie
from PyQt5.QtCore import *

#Reletive Image Path
PathAll2 = "resources\\Core\\Mirror\\"

#FireBase Public Api  (you get this data after open Firebase project. this is a public data)
global config
config = {
            'apiKey': "Put Fire base data here",
            'authDomain': "Put Fire base data here",
            'databaseURL': "Put Fire base data here",
            'storageBucket': "Put Fire base data here",
        }

#Buttom bar Links   (Change links to fit your own project)
DiscordLink = "https://discord.gg/ggRCXS2"
YouTubeLink = "https://www.youtube.com/channel/UC5OzmTUVUxZAPTRJwpwHCYg"
PatrLink = "https://www.patreon.com/AutoMirror"
WebSiteLink = "https://github.com/DizzyduckAR/LoginBase"


#Cloud Function Links

#Login
#Put Function link "https://us-central1-name-project.cloudfunctions.net/Login"
LoginApi = 'yourLinkHere'

#Set Nick Name
#Put Function link "https://us-central1-Name-project.cloudfunctions.net/SetNick"
SetNickApi = 'yourLinkHere'


from Gui.Login import Ui_MainWindow
try:
    import pyrebase
except:
    print("no pyre")
import re
import sys
import webbrowser





xset = None
email = None
connection = None
auth = None
user = None
uid = None
Nick = None
Time = None
Token = None


#main Flow
class MainWindow(QMainWindow, Ui_MainWindow):
    

    def __init__(self):
        super(MainWindow, self).__init__()
        from client_config import ClientConfig
        self.setWindowTitle(ClientConfig.APP_NAME+ "   " +ClientConfig.APP_VERSION )

        import concurrent.futures
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
                    tasks = []
                    tasks.append(executor.submit(self.startLogin()))


        
    
    
    
    #Call "login.py" Gui 

    def startLogin(self):
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(
        Qt.Window |
        Qt.CustomizeWindowHint |
        Qt.WindowTitleHint 

        )
     
        #json
        import json
        with open('resources/Settings.json') as f:
            # some JSON:
            datajson = json.load(f)
            self.ui.UsernameTXT.setText(datajson["name"])
            self.ui.PassLoginTXT.setText(datajson["password"])

        #TopBAR
        
        self.ui.Closegui.clicked.connect(self.CloseguiD)
        self.ui.MinimizeGUI.clicked.connect(self.MinimizeD)
        self.ui.BackLogin.clicked.connect(self.BackLoginD)
        #

        #Buttons
        self.ui.RegisterBTN.clicked.connect(self.RegisterBTND)
        self.ui.PassresetBTN.clicked.connect(self.PassresetBTND)
        self.ui.GuestBTN.clicked.connect(self.GuestBTND)
        self.ui.LoginBTN.clicked.connect(self.LoginBTND)
        self.ui.LifeBTN.clicked.connect(self.LifeBTND)
        self.ui.RecoverBTN.clicked.connect(self.RecoverBTND)
        self.ui.ResentBTN.clicked.connect(self.ResentBTND)
        #

        #ButtomBar
        self.ui.Discord.clicked.connect(self.DiscordBtnD)
        self.ui.Youtube.clicked.connect(self.YoutubeBtnD)
        self.ui.Patr.clicked.connect(self.PatrD)
        self.ui.WebSiteicon.clicked.connect(self.WebSiteiconD)
        self.ui.LangCombo.currentIndexChanged.connect(lambda Menupick: self.SetLangLog("login"))
        import time
        
    


    @pyqtSlot()



#Login GUI Funcs and Actions

    def RegisterBTND(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def PassresetBTND(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def BackLoginD(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def MinimizeD(self): 
        self.showMinimized()

    def CloseguiD(self):
        sys.exit(app.exec_())   
        
    def GuestBTND(self):
        pass
        
    def DiscordBtnD(self, accion):
        print("DiscordBt")
        webbrowser.open_new_tab(DiscordLink)

    def YoutubeBtnD(self, accion):
        print("YoutubeBtn")
        webbrowser.open_new_tab(YouTubeLink)
    
    def PatrD(self, accion):
        print("PatrD")
        webbrowser.open_new_tab(PatrLink)

    def WebSiteiconD(self, accion):
        print("WebSiteiconD")
        webbrowser.open_new_tab(WebSiteLink)
   
    def RecoverBTND(self):
        print("Pass Recover")
        self.ui.ResentBTN.setEnabled(True)
        self.ui.RecoverBTN.setEnabled(False)
        email = self.ui.RecoverEmailEdit.text()
        
        
        self.ui.RecoverStatus.setText("")
        # connectivity to the fire base
        
        
        connection = pyrebase.initialize_app(config)
        auth = connection.auth()
        try:
        
            user = auth.send_password_reset_email(email)
            self.ui.RecoverStatus.setText("Reset Sent")
        
        except:
            self.ui.RecoverStatus.setText("No Email Found")

    def ResentBTND(self):
        print("Resend")
        self.ui.ResentBTN.setEnabled(False)
        email = self.ui.RecoverEmailEdit.text()
        self.ui.RecoverStatus.setText("")
        # connectivity to the fire base
        
        
        connection = pyrebase.initialize_app(config)
        auth = connection.auth()
        try:
            user = auth.send_password_reset_email(email)
            self.ui.RecoverStatus.setText("Reset Sent")
        except:
            self.ui.RecoverStatus.setText("No Email Found")


#Login Funcs
    def LoginBTND(self):
        global email 
        email = self.ui.UsernameTXT.text()
        password = self.ui.PassLoginTXT.text()

       
        self.ui.LoginStatus.setText("")
        
        # connectivity to the fire base
      
        global connection
        connection = pyrebase.initialize_app(config)
        global auth
        auth = connection.auth()
        
        import json
        import requests
        


        try:
            global user
            user = auth.sign_in_with_email_and_password(email, password)
            global uid
            uid = user["localId"]
            userset = user["idToken"]
            xset = userset[0:20]
            
            import json

            with open('resources/Token.json','r') as jsonfile:
                json_content = json.load(jsonfile)
                #print(json_content["Token"])
                data = {
                            "Token": userset
                        }
                

            with open('resources/Token.json','w') as jsonfile:
                json.dump(data, jsonfile)

            connection = pyrebase.initialize_app(config)
            firebase: Database = connection.database()
            
        except:
            self.ui.LoginStatus.setText("Error User/Pass")



        try:
                
                payload = {'UserPCUID': uid}
                
                r = requests.get(LoginApi, params=payload)
                data = r.json()
                
                
                global Nick
                Nick = data["Nick"]
                global Time
                Time = data["Time"]
                global Token
                Token = data["Token"]

        except:
                self.ui.LoginStatus.setText("User Not in DB")
                return

        try:
            
            import json 
            # first, get the absolute path to json file
            
            with open('resources/Settings.json','r') as jsonfile:
                json_content = json.load(jsonfile)
                
                data = {
                            "name": email,
                            "password": password,
                            "NickName": Nick
                        }
                

            with open('resources/Settings.json','w') as jsonfile:
                json.dump(data, jsonfile)

            # read existing json to memory. you do this to preserve whatever existing data. 
                        
            self.ui.LoginStatus.setText("Logged IN")
            #self.startMainWindow()
            #Do DO DO
        
        
        
        except:
            self.ui.LoginStatus.setText("Error DB Check")
            return
#Register
    def LifeBTND(self):
        print("Free User")
        global Nick
        email = self.ui.UserRegEmail.text()
        password = self.ui.UserRegPass.text()
        Nick = self.ui.UserRegNick.text()
        
        
        
        
        self.ui.StatusSingup.setText("")
        # connectivity to the fire base
        
        connection: Firebase = pyrebase.initialize_app(config)
        auth = connection.auth()
        
        try:
        
            user = auth.create_user_with_email_and_password(email, password)
            security = auth.send_email_verification(user['idToken'])
            uid = user["localId"]
            print(uid)
            userset = user["idToken"]
        
            global xset
            xset = userset[0:20]
            connection = pyrebase.initialize_app(config)
            firebase: Database = connection.database()
        
        
        except:
        
            self.ui.StatusSingup.setText("Error User/Pass")

        try:
                import time
                import json
                import requests
                time.sleep(3)
                payload = {'UserPCUID': uid,'NickSet': Nick}
                
                r = requests.get(SetNickApi, params=payload)
                data = r.json()
                print("Nick Set")
        except:
                print("Fail push")
                return
        
        self.ui.StatusSingup.setText("New User Added")

        try:
            self.ui.UsernameTXT.setText(email)
                # print(Emailtmp)
        except:
                print("no Email")
            
        self.ui.stackedWidget.setCurrentIndex(0)

        print("Free User")
        global Nick
        email = self.ui.UserRegEmail.text()
        password = self.ui.UserRegPass.text()
        Nick = self.ui.UserRegNick.text()
        
        
        
        
        self.ui.StatusSingup.setText("")
        # connectivity to the fire base
        
        connection: Firebase = pyrebase.initialize_app(config)
        auth = connection.auth()
        
        try:
        
            user = auth.create_user_with_email_and_password(email, password)
            security = auth.send_email_verification(user['idToken'])
            uid = user["localId"]
            print(uid)
            userset = user["idToken"]
        
            global xset
            xset = userset[0:20]
            connection = pyrebase.initialize_app(config)
            firebase: Database = connection.database()
        
        
        except:
        
            self.ui.StatusSingup.setText("Error User/Pass")

        try:
                import time
                import json
                import requests
                time.sleep(3)
                payload = {'UserPCUID': uid,'NickSet': Nick}
                r = requests.get('https://us-central1-botit-project.cloudfunctions.net/SetNick', params=payload)
                data = r.json()
                print("Nick Set")
        except:
                print("Fail push")
                return
        
        self.ui.StatusSingup.setText("New User Added")

        try:
            self.ui.UsernameTXT.setText(email)
                # print(Emailtmp)
        except:
                print("no Email")
            
        self.ui.stackedWidget.setCurrentIndex(0)
#Recover
    def RecoverBTND(self):
        print("Pass Recover")
        self.ui.ResentBTN.setEnabled(True)
        self.ui.RecoverBTN.setEnabled(False)
        email = self.ui.RecoverEmailEdit.text()
        
        
        self.ui.RecoverStatus.setText("")
        # connectivity to the fire base
        
        
        connection = pyrebase.initialize_app(config)
        auth = connection.auth()
        try:
        
            user = auth.send_password_reset_email(email)
            self.ui.RecoverStatus.setText("Reset Sent")
        
        except:
            self.ui.RecoverStatus.setText("No Email Found")
#Resend recover
    def ResentBTND(self):
        print("Resend")
        self.ui.ResentBTN.setEnabled(False)
        email = self.ui.RecoverEmailEdit.text()
        
        
        self.ui.RecoverStatus.setText("")
        # connectivity to the fire base
        
        
        connection = pyrebase.initialize_app(config)
        auth = connection.auth()
        try:
            user = auth.send_password_reset_email(email)
            self.ui.RecoverStatus.setText("Reset Sent")
        except:
            self.ui.RecoverStatus.setText("No Email Found")
#lang set 
    def SetLangLog(self,Menupick):    
        if Menupick == "login":
            try:
                LangPick = self.ui.LangCombo.currentIndex()
                #print(LangPick)
                if LangPick == 0:
                            import json
                            try:
                                with open("resources/Lang.json", "r+") as jsonFile:
                                    data = json.load(jsonFile)

                                    data['Pick'][0]['Lang']="EN"
                                    
                                    jsonFile.seek(0)  # rewind
                                    json.dump(data, jsonFile, indent=2)
                                    #jsonFile.truncate()

                                try:
                                    self.langPush("EN","login")
                                    
                                except:
                                    print("fail push Func")


                            except:
                                print("Err EN")

                if LangPick == 1:
                            import json
                            try:
                                with open("resources/Lang.json", "r+") as jsonFile:
                                    data = json.load(jsonFile)

                                    data['Pick'][0]['Lang']="SP"
                                    
                                    jsonFile.seek(0)  # rewind
                                    json.dump(data, jsonFile, indent=2)
                                    jsonFile.truncate()
                                self.langPush("SP",Menupick)
                                return

                            except:
                                print("Err SP")

                if LangPick == 2:
                            import json
                            try:
                                with open("resources/Lang.json", "r+") as jsonFile:
                                    data = json.load(jsonFile)

                                    data['Pick'][0]['Lang']="RU"
                                    
                                    jsonFile.seek(0)  # rewind
                                    json.dump(data, jsonFile, indent=2)
                                    jsonFile.truncate()
                                self.langPush("RU",Menupick)

                            except:
                                print("Err RU")

                if LangPick == 3:
                            import json
                            try:
                                with open("resources/Lang.json", "r+") as jsonFile:
                                    data = json.load(jsonFile)

                                    data['Pick'][0]['Lang']="CN"
                                    
                                    jsonFile.seek(0)  # rewind
                                    json.dump(data, jsonFile, indent=2)
                                    jsonFile.truncate()
                                self.langPush("CN",Menupick)

                            except:
                                print("Err CN")

                if LangPick == 4:
                            import json
                            try:
                                with open("resources/Lang.json", "r+") as jsonFile:
                                    data = json.load(jsonFile)

                                    data['Pick'][0]['Lang']="FR"
                                    
                                    jsonFile.seek(0)  # rewind
                                    json.dump(data, jsonFile, indent=2)
                                    jsonFile.truncate()
                                self.langPush("FR",Menupick)

                            except:
                                print("Err FR")

                if LangPick == 5:
                            import json
                            try:
                                with open("resources/Lang.json", "r+") as jsonFile:
                                    data = json.load(jsonFile)

                                    data['Pick'][0]['Lang']="DE"
                                    
                                    jsonFile.seek(0)  # rewind
                                    json.dump(data, jsonFile, indent=2)
                                    jsonFile.truncate()
                                self.langPush("DE",Menupick)

                            except:
                                print("Err DE")

                if LangPick == 6:

                            import json
                            try:
                                with open("resources/Lang.json", "r+") as jsonFile:
                                    data = json.load(jsonFile)

                                    data['Pick'][0]['Lang']="ES"
                                    
                                    jsonFile.seek(0)  # rewind
                                    json.dump(data, jsonFile, indent=2)
                                    jsonFile.truncate()
                                self.langPush("ES",Menupick)

                            except:
                                print("Err ES")
            except:
                print("Err")

        
        if Menupick == "Botit":
            try:
                LangPick = self.ui2.LangCombo.currentIndex()

                if LangPick == 0:
                            import json
                            try:
                                with open("resources/Lang.json", "r+") as jsonFile:
                                    data = json.load(jsonFile)

                                    data['Pick'][0]['Lang']="EN"
                                    
                                    jsonFile.seek(0)  # rewind
                                    json.dump(data, jsonFile, indent=2)
                                    #jsonFile.truncate()

                                try:
                                    self.langPush("EN","Botit")
                                    
                                except:
                                    print("fail push Func")


                            except:
                                print("Err EN")

                if LangPick == 1:
                        import json
                        try:
                            with open("resources/Lang.json", "r+") as jsonFile:
                                data = json.load(jsonFile)

                                data['Pick'][0]['Lang']="SP"
                                                    
                                jsonFile.seek(0)  # rewind
                                json.dump(data, jsonFile, indent=2)
                                jsonFile.truncate()
                                                
                                self.langPush("bot SP",Menupick)


                        except:
                            print("Err SP")

                if LangPick == 2:
                        import json
                        try:
                            with open("resources/Lang.json", "r+") as jsonFile:
                                data = json.load(jsonFile)

                                data['Pick'][0]['Lang']="RU"
                                                    
                                jsonFile.seek(0)  # rewind
                                json.dump(data, jsonFile, indent=2)
                                jsonFile.truncate()
                                                
                                self.langPush("RU",Menupick)


                        except:
                            print("Err bot RU")

                if LangPick == 3:
                                import json
                                try:
                                    with open("resources/Lang.json", "r+") as jsonFile:
                                        data = json.load(jsonFile)

                                        data['Pick'][0]['Lang']="CN"
                                        
                                        jsonFile.seek(0)  # rewind
                                        json.dump(data, jsonFile, indent=2)
                                        jsonFile.truncate()

                                    self.langPush("CN",Menupick)


                                except:
                                    print("Err bot CN")

                if LangPick == 4:
                        import json
                        try:
                            with open("resources/Lang.json", "r+") as jsonFile:
                                data = json.load(jsonFile)

                                data['Pick'][0]['Lang']="FR"
                                                    
                                jsonFile.seek(0)  # rewind
                                json.dump(data, jsonFile, indent=2)
                                jsonFile.truncate()
                                                
                                self.langPush("FR",Menupick)


                        except:
                            print("Err bot FR")

                if LangPick == 5:
                        import json
                        try:
                            with open("resources/Lang.json", "r+") as jsonFile:
                                data = json.load(jsonFile)

                                data['Pick'][0]['Lang']="DE"
                                                    
                                jsonFile.seek(0)  # rewind
                                json.dump(data, jsonFile, indent=2)
                                jsonFile.truncate()
                                                
                                self.langPush("DE",Menupick)


                        except:
                            print("Err bot ES")

                if LangPick == 6:
                    import json
                    try:
                        with open("resources/Lang.json", "r+") as jsonFile:
                            data = json.load(jsonFile)

                            data['Pick'][0]['Lang']="ES"
                                                
                            jsonFile.seek(0)  # rewind
                            json.dump(data, jsonFile, indent=2)
                            jsonFile.truncate()
                                            
                            self.langPush("ES",Menupick)


                    except:
                        print("Err bot ES")


            except:
                print("Err")
#push lang on gui
    def langPush(self,lang,Menupick):
        #print("push")
        try:
            if Menupick == "login":
                import json
                with open('resources/Lang.json') as f:
                    # some JSON:
                        datajson = json.load(f)
                        lang = str(lang)
                        
                        Menupick = str(Menupick)
                        #print(Menupick)
                        LangPick = datajson['Pick'][0]['Lang']
                        
                        #print(LangPick)
                        for key in datajson[lang][0][Menupick].keys():
                                    try:
                                        textjson = datajson[lang][0][Menupick][key][0]
                                        status = datajson[lang][0][Menupick][key][1]
                                        Mode = datajson[lang][0][Menupick][key][2]

                                        if Mode == "text":
                                                getattr(self.ui, key).setText(textjson)
                                                getattr(self.ui, key).setToolTip(status)
                                                getattr(self.ui, key).setStatusTip(status)
                                                continue
                                        if Mode == "NoText":
                                                getattr(self.ui, key).setToolTip(status)
                                                getattr(self.ui, key).setStatusTip(status)
                                                continue
                                        if Mode == "Holder":
                                                getattr(self.ui, key).setPlaceholderText(textjson)
                                                getattr(self.ui, key).setToolTip(status)
                                                getattr(self.ui, key).setStatusTip(status)
                                                continue
                                    except:
                                        print("error",key)
                        return

            if Menupick == "Botit":
                import json
                with open('resources/Lang.json') as f:
                    # some JSON:
                        datajson = json.load(f)
                        lang = str(lang)
                        Menupick = str(Menupick)
                        LangPick = datajson['Pick'][0]['Lang']
                        #print(LangPick)
                        for key in datajson[lang][0][Menupick].keys():
                                    textjson = datajson[lang][0][Menupick][key][0]
                                    status = datajson[lang][0][Menupick][key][1]
                                    Mode = datajson[lang][0][Menupick][key][2]

                                    if Mode == "text":
                                            getattr(self.ui2, key).setText(textjson)
                                            getattr(self.ui2, key).setToolTip(status)
                                            getattr(self.ui2, key).setStatusTip(status)
                                            continue
                                    if Mode == "NoText":
                                            getattr(self.ui2, key).setToolTip(status)
                                            getattr(self.ui2, key).setStatusTip(status)
                                            continue
                                    if Mode == "Holder":
                                            getattr(self.ui2, key).setPlaceholderText(textjson)
                                            getattr(self.ui2, key).setToolTip(status)
                                            getattr(self.ui2, key).setStatusTip(status)
                                            continue

                        
        except:
            print(key,"error")
            

    

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.setWindowIcon(QIcon('resources/base/Gui/Icon.ico'))
    sys.exit(app.exec_())
    