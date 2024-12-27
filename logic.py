import os
import re
import shutil

# TODO: Functions that handel part of project

def searchInSpeceficDirectory(files):
    whole = [[], []]
    for file in files:
        name = re.findall("[\S]+S[\d]+\.?E[\d]+", file)
        if len(name) > 0:
            whole[0].append(name[0])
            whole[1].append(file)
    return whole

def detectDirection(names, path, actualName, destenation):
    i = 0
    for name in names:
        for index in reversed(range(len(name))):
            if name[index] == '.':
                
                # Detect serial name
                serialName = name[:index]
                serialName = serialName.replace('.', ' ')

                # Detect serial season
                season = re.findall("S[\d]+", name)
                season = season[0]
                season = season[1:]
                season = int(season)
                season = str(season)

                # Detect episode season
                episode = re.findall("E[\d]+", name)
                episode = episode[0]
                episode = episode[1:]
                episode = int(episode)
                episode = str(episode)

                makeDirections(serialName, season, episode, path, actualName[i], destenation)
                break
        i = i + 1

def makeDirections(serialName, season, episode, path, actualName, destenation):

    targetPath = destenation + "\\" + serialName + "\\" + season + "\\" + episode
    if not os.path.isdir(destenation+ "\\" + serialName):
        os.mkdir(destenation + "\\" + serialName)
    if not os.path.isdir(destenation + "\\" + serialName + "\\" + season):
        os.mkdir(destenation +"\\"  + serialName + "\\" + season)
    if not os.path.isdir(targetPath):
        os.mkdir(targetPath)

    shutil.move(path + "\\" + actualName, targetPath)
