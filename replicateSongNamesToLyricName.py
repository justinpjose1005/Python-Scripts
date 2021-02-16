import os

folderName = 'Malayalam Lyrics'

allSongs = os.listdir('Malayalam Songs')
#print(allSongNames)

allLyrics = os.listdir('Malayalam Lyrics')
#print(allLyricNames)

all_songs_list = []

for i in allLyrics:
    j = i.split()
    if (j[0] == 'Song'):
        print(j[1]+" was already renamed")
    else:
        print("checking if "+j[2]+" needs to be renamed")
        # storing song names
        for eachSong in allSongs:
            s = ''
            for i in eachSong:
                if (i != '.'):
                    s += i
                else:
                    break
            all_songs_list.append(s)

        # storing lyric names
        for eachLyric in allLyrics:
            s = ''
            matchingName = ''
            n = 0
            name_list = eachLyric.split('-')
            
            for i in name_list[1]:
                if (i != '.'):
                    s += i
                else:
                    break
            try:
                n = int(s)
            except ValueError:
                pass

            for names in all_songs_list:
                split_list = names.split()
                if (int(split_list[1]) == n):
                    matchingName = names
                    src = 'Malayalam Lyrics/' + eachLyric
                    dst = 'Malayalam Lyrics/' + matchingName + ".pdf"
                    os.rename(src,dst)
                    print(str(n)+" has been renamed")
                    break

                
                
