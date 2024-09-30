import os

current_file = os.path.realpath(__file__)
current_directory = os.path.dirname(current_file)
print("1-Start static version\n2-Start normal version (recommended)\n3-exit")
while True:
    num = input(":")
    if num == "1":
        os.system(f"py -3.8 {current_directory}/main.py")
    elif num == "2":
        os.system(f"py -3.8 {current_directory}/system-master/main.py")
    elif num == "3":
        break
    else:
        print("You print bad number")
