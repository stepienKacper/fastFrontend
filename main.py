import os
import sys
import string

html_text = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
    <script src="script.js"></script>
</head>
<body>
    
</body>
</html>"""
def main():
    utworzono = False
    available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
    path = str(input("Podaj symbol dysku w którym utworzyć: (C, D, E, F , G) lub podaj dokladna scieżkę: \n"))
    print("Obecna ścieżka: ", os.getcwd())
    if path in available_drives or os.path.exists(path=path):
        os.chdir(path=path)
        print(os.getcwd())
        print("Foldery: ")
        [print(x) for x in os.listdir()]
        new_folder = str(input("Czy utworzyć nowy folder? [y,n]: "))
        if new_folder == 'y':
            folder_name = str(input("Podaj nazwe tego folderu: "))
            if not os.path.isdir(folder_name):
                os.mkdir(folder_name)
                os.chdir(folder_name)
                h = open('index.html','w+')
                h.write(html_text)
                c = open('style.css','w+')
                j = open('script.js','w+')
                print('Wszystkio utworzono prawidłowo')
                h.close(), c.close(), j.close()
            else:
                print("Taki folder juz istnieje")
                main()
        else:
            h = open('index.html','w+')
            h.write(html_text)
            c = open('style.css','w+')
            j = open('script.js','w+')
            print('Wszystkio utworzono prawidłowo')
            h.close(), c.close(), j.close()
    else:
        print('Nie ma takiego dysku')
        main()

if __name__ == '__main__':
    main()
