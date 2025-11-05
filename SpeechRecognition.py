
def get_command():
    x =True
    file = open ("D:\\code\\ZOYA\\Module\\Speech_Recognition.txt", "w+")
    while x:   
        Text = file.read()
        if len(Text)!= 0 : 
            x = False 
            file.truncate()
            file.close()

    return Text.lower()