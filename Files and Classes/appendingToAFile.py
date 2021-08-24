appendMe = ' → Some text 2'

saveFile = open('exampleWrite.txt', 'a')
saveFile.write('\n')
saveFile.write(appendMe)
saveFile.close()

# We add more text to the files without overwrite the last data it has.