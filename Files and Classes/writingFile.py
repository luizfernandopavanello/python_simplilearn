writeMe = 'Example how to write and save files! Open, filename, method, than the .write with whatever we wanna write, data, and the close to finish right.'

saveFile = open('exampleWrite.txt', 'w')
saveFile.write(writeMe)
saveFile.close()

# If we write something, we will overwriting previous data.