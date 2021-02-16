import os

folderName = 'Malayalam Songs'

allSongNames = os.listdir(folderName)
#print(allSongNames)

allLyricNames = os.listdir('Malayalam Lyrics')
#print(allLyricNames)

new_song_name_list = []
for eachSongName in allSongNames:
    i = eachSongName.split()
    if (len(i[1]) == 3):
        print(i[1]+" is already renamed")
    else:
        print("---------------------------------")
        print(i[1]+" is in need of renaming")
        new_song_name = ''
        s = ''
        first_part = ''
        middle_part = ''
        last_part = ''
        space_counter = 0
        for eachChar in eachSongName:
            if (space_counter <= 1 and eachChar != ' '):
                s = s + eachChar
            if (space_counter == 2):
                last_part = last_part + eachChar
            if (space_counter == 1 and eachChar == ' '):
                if (len(s) == 1):
                    middle_part = '00' + s
                elif (len(s) == 2):
                    middle_part = '0' + s
                elif (len(s) == 3):
                    middle_part = s
                space_counter = 2
                s = ''
            if (space_counter == 0 and eachChar == ' '):
                first_part = s
                space_counter = 1
                s = ''
        new_song_name = first_part + ' ' + middle_part + ' ' + last_part
        new_song_name_list.append(new_song_name)
        src = folderName + "/" + eachSongName
        dst = folderName + "/" + new_song_name
        print("old dir: "+src)
        print("new dir: "+dst)
        os.rename(src,dst)
    

                  
