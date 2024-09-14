import os, json

new_lib = True
while True:
    try:
        import gay, porno
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
            print("not install lib")
