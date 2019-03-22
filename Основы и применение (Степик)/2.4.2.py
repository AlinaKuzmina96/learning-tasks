import os.path

os.chdir('main')
with open("text.txt", "w") as f:
    for dir, dirs, files in os.walk("main"):
        for i in files:
            if i[-3:] == ".py":
                a = dir.replace('\\','/')
                a1 = str(a)+"\n"
                f.write(a1)
                break