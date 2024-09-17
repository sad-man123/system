import os, json, pyVariable

new_lib = True
while True:
    try:
        from pynput.keyboard import Events
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from bs4 import BeautifulSoup
        import pyfiglet, time, requests

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
                                                 "       exit       "]}
        self.menu_manager = {"main menu": "<<              >>",
                             "not found": ""}
        self.current_manager = "main menu"
        self.cur_menu = "main"
        self.now_array = []
        self.data_json = json.load(open("data.json"))
        self.creator_mod = eval(self.data_json["creator mod"])
        self.now_version = self.data_json["version"]
        self.update_bool = False
        self.password_input = ""
        self.current_creator_menu = "main menu"
        self.creator_github_url = "sad-man123"
        self.end_array = []
        print("Press q, for the start")
        with Events() as events:
            for event in events:
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
                if "Release" in str(event):
                    os.system("cls")
                    key = str(event.key).replace("'", "")
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
                    elif key == "Key.enter":
                        if self.cur_menu == "main":
                            if self.current_line == 4:
                                os.system("cls")
                                json.dump(self.data_json, open("data.json", "w"))
                                break
                            elif self.current_line == 2:
                                self.cur_menu = "creator mod"
                            elif self.current_line == 5:
                                self.cur_menu = "version control"
                                sait = requests.get(f"https://github.com/sad-man123/system")
                                soup = BeautifulSoup(sait.content, 'html.parser')
                                text = soup.find("p", attrs={"dir": "auto"})
                                for i in text:
                                    self.new_version = i
                                self.update_bool = True
                            else:
                                self.cur_menu = "not found"
                        elif self.cur_menu == "version control":
                            if self.current_line == 1:
                                self.cur_menu = "main"

                    if self.cur_menu == "main":
                        if self.creator_mod:
                            for i in self.creator[self.current_creator_menu]:
                                print(i)
                        else:
                            styled_text = pyfiglet.figlet_format('Python3', font='doom')
                            print(styled_text)
                    self.current_array()
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
                        else:
                            self.end_array = self.current_menu[self.cur_menu]
                    print(self.current_line)
                    for i in self.end_array:
                        print(i)
                    time.sleep(0.3)

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
