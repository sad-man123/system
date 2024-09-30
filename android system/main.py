import os, pyVariable, zipfile

new_lib = True
while True:
    try:
        from bs4 import BeautifulSoup
        import pyfiglet, time, requests, shutil, wget, json

        break
    except Exception as ex:
        if new_lib:
            with open("lib.json") as f:
                lib = json.loads(f.read())
                new_lib = False
        ex1 = str(ex)
        ex1 = ex1.replace("No module named ", "")
        ex1 = ex1.replace("'", "")
        if ex1 in lib:
            ex1 = lib[ex1]
        print(ex1)
        try:
            os.system(f"pip install {ex1}")
        except:
            print("install lib is not successfully")

#py -3.8 Desktop/my promming system/main.py
class Main():
    def __init__(self):
        super().__init__()
        self.current_line = 0
        self.current_menu = {"main": ["    start code    ",
                                      "    github        ",
                                      "    creator       ",
                                      "    directory     ",
                                      "    exit          ",
                                      "    check update  "],
                             "creator mod": ["for exit click Y in keyboard"],
                             "not found": ["This part isn't make",
                                           "Coming soon",
                                           "exit for Y"],
                             "version control": ["      update      ",
                                                 "       exit       "],
                             "reboot": ["   reboot system  ",
                                        "       exit       "],
                             "github": ["    check github  ",
                                        "     add github   ",
                                        "        exit      "],
                             "show": [""],
                             "show github": [""],
                             "github menu": [""],
                             "github project": ["      install     ",
                                                "       check      ",
                                                "       exit       "],
                             "direction": ["       exit       ",
                                           "       local      "]}
        self.menu_manager = {"main menu": "<<              >>",
                             "not found": "",
                             "reboot": ">>                "}
        self.current_manager = "main menu"
        self.cur_menu = "main"
        self.now_array = []
        self.github_sh_bo = False
        self.data_json = json.load(open("data.json"))
        self.creator_mod = eval(self.data_json["creator mod"])
        self.now_version = self.data_json["version"]
        self.update_bool = False
        self.github_now = "sad-man123"
        self.password_input = ""
        self.hub = ""
        self.hub_bo = ""
        self.local_dirs_names = ""
        self.git_bo = False
        self.github_project = ""
        self.current_creator_menu = "main menu"
        self.github = self.data_json["github list"]
        self.creator_github_url = "sad-man123"
        self.end_array = []
        self.description_project = ""
        print("Press q, for the start")
        self.check_all_project()
        while True:

                self.creator = {"main menu": ["",
                                              "",
                                              f"   {'  ' * self.current_line}@@   |   @@",
                                              f"   {'  ' * self.current_line}@@   |   @@",
                                              f"   {'  ' * self.current_line}@@       @@",
                                              f"   {'  ' * self.current_line}@@=======@@",
                                              f"   {'  ' * self.current_line}@@       @@",
                                              f"   {'  ' * self.current_line}@@       @@",
                                              f"   {'  ' * self.current_line}@@       @@",
                                              ""]}
                if True:
                    key = input()
                    if key == "":
                        key = "Key.enter"
                    elif len(key) > 1:
                        key = f"Key.{key}"
                    os.system("cls")
                    if key == "s":
                        self.current_line += 1
                    elif key == "w":
                        self.current_line -= 1
                    elif key == "y":
                        if self.cur_menu == "creator mod":
                            self.cur_menu = "main"
                        elif self.cur_menu == "not found":
                            self.cur_menu = "main"
                    if self.cur_menu == "creator mod":
                        if "Key.shift" in key:
                            ...
                        else:
                            if key == "d":
                                self.password_input = ""
                            else:
                                self.password_input += key
                        if self.password_input == "123123_vn122":
                            self.creator_mod = True
                            self.data_json["creator mod"] = "True"
                    if self.current_line == -1:
                        self.current_line = len(self.current_menu[self.cur_menu]) - 1
                    elif self.current_line >= len(self.current_menu[self.cur_menu]):
                        self.current_line = 0


                    #Buttons def

                    if key == "Key.enter":
                        #Main menu
                        if self.cur_menu == "main":
                            if self.current_line == 4:
                                os.system("cls")
                                json.dump(self.data_json, open("data.json", "w"))
                                break
                            elif self.current_line == 2:
                                self.cur_menu = "creator mod"
                            elif self.current_line == 5:

                                self.current_line = 0
                                self.cur_menu = "version control"
                                sait = requests.get(f"https://github.com/sad-man123/system")
                                soup = BeautifulSoup(sait.content, 'html.parser')
                                text = soup.find("p", attrs={"dir": "auto"})
                                for i in text:
                                    self.new_version = i
                                self.update_bool = True
                            elif self.current_line == 1:
                                self.current_line = 0
                                self.cur_menu = "github"
                            elif self.current_line == 3:
                                self.cur_menu = "direction"
                            else:
                                self.cur_menu = "not found"
                        # versions
                        elif self.cur_menu == "version control":
                            if self.current_line == 1:
                                self.cur_menu = "main"
                            elif self.current_line == 0:
                                self.installer_updates()
                                self.cur_menu = "main"
                                print("please, reboot the program")
                        # direction menu
                        elif self.cur_menu == "direction":
                            if self.current_line == 0:
                                self.cur_menu = "main"
                            elif self.current_line == 1:
                                self.local_names()
                                print(self.local_dirs_names)
                        # github project
                        elif self.cur_menu == "show":
                            if self.current_line == 0:
                                self.cur_menu = "github"
                                self.git_bo = False
                                self.github_sh_bo = True
                            else:
                                self.github_sh_bo = False
                                self.git_bo = False
                                self.github_project = self.all_project1[self.current_line]
                                self.cur_menu = "github project"
                        elif self.cur_menu == "github menu":
                            ...
                        # github creators
                        elif self.cur_menu == "github creators":
                            if self.current_line == 0:
                                self.github_sh_bo = False
                                self.cur_menu = "github"
                        # Github project
                        elif self.cur_menu == "github project":
                            if self.current_line == 0:
                                self.install_github()
                            elif self.current_line == 1:
                                self.check_readme()
                                print(self.description_project)
                            elif self.current_line == 2:
                                self.cur_menu = "show"
                                self.git_bo = True
                        # Show creators
                        elif self.cur_menu == "show creators":
                            if self.current_line == 0:
                                self.cur_menu = "github"
                                self.github_sh_bo = False
                            else:
                                self.github_now = self.all_project2[self.current_line]
                                self.git_bo = True
                                self.github_sh_bo = False


                        # reboot
                        elif self.cur_menu == "reboot":
                            if self.current_line == 1:
                                self.cur_menu = "main"
                            elif self.current_line == 0:
                                ...
                            else:
                                self.cur_menu = "not found"
                        # github menu
                        elif self.cur_menu == "github":
                            if self.current_line == 0:
                                self.github_sh_bo = True
                            elif self.current_line == 1:
                                self.cur_menu = "show github"
                            elif self.current_line == 2:
                                self.cur_menu = "main"
                            else:
                                self.cur_menu = "not found"
                    elif key == "Key.esc":
                        self.cur_menu = "main"
                        self.github_sh_bo = False
                        self.git_bo = False
                    if self.cur_menu == "show github":
                        print(" press by buttons in keyboard to ford word\nF1 - end the word\nesc - exit")
                        if key == "Key.f1":
                            self.hub_bo = True
                        elif key == "Key.backspace":
                            self.hub = self.hub[0:len(self.hub) - 1]
                        elif key == "Key.esc":
                            self.cur_menu = "github"
                        else:
                            if not key == "Key.enter":
                                self.hub += key
                        print(self.hub)
                        if self.hub_bo:
                            req = requests.get(f"https://github.com/{self.hub}")
                            if req.status_code == 200:
                                if self.hub in self.github:
                                    print("This creator is already on the list")
                                    self.cur_menu = "github"
                                else:
                                    print("OK, I add your coder in catalog")
                                    self.github.append(self.hub)
                                    self.cur_menu = "github"
                            else:
                                print("This maker is not found")

                    #Creator mod

                    if self.cur_menu == "main":
                        if self.creator_mod:
                            for i in self.creator[self.current_creator_menu]:
                                print(i)
                        else:
                            styled_text = pyfiglet.figlet_format('Python3', font='doom')
                            print(styled_text)
                    self.current_array()

                    #def for grafics

                    if self.cur_menu == "creator mod":
                        self.end_array = self.current_menu[self.cur_menu]
                    else:
                        if not self.cur_menu == "not found":
                            self.array_1 = self.current_menu[self.cur_menu]
                            self.adder()
                            if self.cur_menu == "version control":
                                print(f"version now: {self.now_version}")
                                print(f"version new: {self.new_version}")
                                self.array_1 = self.current_menu[self.cur_menu]
                                self.adder()
                            elif self.cur_menu == "reboot":
                                self.current_manager = "reboot"
                                self.current_array()
                                self.array_1 = self.current_menu[self.cur_menu]
                                self.adder()
                        else:

                            self.end_array = self.current_menu[self.cur_menu]
                    print(self.current_line)
                    if self.github_sh_bo:
                        self.check_all_github()
                    if self.git_bo:
                        self.github_show()
                    for i in self.end_array:
                        print(i)
                    time.sleep(0.3)

    def check_readme(self):
        req = requests.get(f"https://github.com/{self.github_now.replace('   ', '')}/{self.github_project.replace('   ', '').replace('  ', '')}")
        soup = BeautifulSoup(req.content, 'html.parser')
        text = soup.find_all("p", attrs={"dir": "auto"})
        for i in text:
            for ii in i:
                self.description_project = ii

    def current_array(self):
        self.array_2 = []
        num_1 = 0
        for i in self.current_menu[self.cur_menu]:
            num_1 += 1
        for i in range(num_1):
            if i == self.current_line:
                self.array_2.append(self.menu_manager[self.current_manager])
            else:
                self.array_2.append(" " * len(self.menu_manager[self.current_manager]))

    def install_github(self):
        response = requests.get(f"https://github.com/{self.github_now.replace('   ', '')}/{self.github_project.replace('   ', '').replace('  ', '')}/archive/refs/heads/master.zip")
        file_Path = f'local/{self.github_project}.zip'

        if response.status_code == 200:
            with open(file_Path, 'wb') as file:
                file.write(response.content)
            print('File downloaded successfully')
        else:
            print('Failed to download file')
        with zipfile.ZipFile(file_Path) as f:
            f.extractall()
        print('File extract successfully')
        os.remove(file_Path)

    def installer_updates(self):
        current_file = os.path.realpath(__file__)
        current_directory = os.path.dirname(current_file)
        print("Wait a few seconds")
        wget.download("https://github.com/sad-man123/system/archive/refs/heads/master.zip")
        time.sleep(2.5)
        print("Archive is downlands")
        disk_array = ["C", "D", "E", "F"]
        disk_bool = False
        for i in disk_array:
            start = f"{i}:/Downloads"
            for dirpath, dirnames, filenames in os.walk(start):
                for filename in filenames:
                    if filename == "system-android.zip":
                        filename = os.path.join(dirpath, filename)
                        print(filename)
                        print(dirpath)
                        disk_bool = True
                        break
                if disk_bool:
                    break
            if disk_bool:
                break
        shutil.move(filename, f"{current_directory}")
        with zipfile.ZipFile(f"{current_directory}/system-android.zip") as f:
            f.extractall()
        os.remove("system-android.zip")


    def local_names(self):
        current_file = os.path.realpath(__file__)
        current_directory = os.path.dirname(current_file)
        self.local_dirs_names = os.listdir(f"{current_directory}/local")

    def github_show(self):
        array = []
        self.all_project1 = []
        for i in self.all_project:
            i += " " * (len(pyVariable.max_str(self.all_project)) - len(i))
            self.all_project1.append(f"   {i}")
        self.t1= f">>{' ' * (len(i) + 3)}"
        num_1 = 0
        self.array_2 = []
        for i in self.all_project1:
            num_1 += 1
        for i in range(num_1):
            if i == self.current_line:
                self.array_2.append(self.t1)
            else:
                self.array_2.append(" " * len(self.t1))
        self.array_1 = self.all_project1
        for i in self.array_1:
            array.append(" ")
        self.current_menu["show"] = array
        self.adder()
        self.cur_menu = "show"

    def check_all_github(self):
        array = []
        self.all_project2 = []
        if not "exit" in self.github:
            self.github.insert(0, "exit")
        for i in self.github:
            i += " " * (len(pyVariable.max_str(self.github)) - len(i))
            self.all_project2.append(f"   {i}")
        self.t1 = f">>{' ' * (len(i) + 3)}"
        num_1 = 0
        self.array_2 = []
        for i in self.all_project2:
            num_1 += 1
        for i in range(num_1):
            if i == self.current_line:
                self.array_2.append(self.t1)
            else:
                self.array_2.append(" " * len(self.t1))
        self.array_1 = self.all_project2
        for i in self.array_1:
            array.append(" ")

        self.current_menu["show creators"] = array
        self.adder()
        self.cur_menu = "show creators"

    def check_all_project(self):
        req = requests.get(f"https://github.com/{self.github_now}")
        soup = BeautifulSoup(req.content, 'html.parser')
        self.all_project = []
        for ii in soup.find_all("span", {"class": "repo"}):
            for i in ii:
                self.all_project.append(str(i.replace("\n" + " " * 16, "")).replace("\n" + " " * 14, ""))
        if self.github_now == "sad-man123":
            creator = "creator"
        else:
            creator = self.github_now
        self.all_project.insert(0, "exit")

    def adder(self):
        self.end_array = []
        array_line = ""
        num_1 = 0
        num_2 = 0
        for i in self.array_1:
            for i1 in i:
                part_line = self.array_2[num_1][num_2]
                if i1 == " ":
                    array_line += part_line
                else:
                    array_line += i1
                num_2 += 1
            self.end_array.append(array_line)
            array_line = ""
            num_1 += 1
            num_2 = 0


Main()
