import os
# TO DO
#   NEED TO MAKE STACK ACTIONS AND FILETYPE SAVING
#   NEED TO MAKE PROJECT FILE FORMAT
class Project():

    redoActions = []
    undoActions = []

    def getNewPath(self, ImgSwtImage):
        # Figures out the name of the next file
        # Each file has an index
        # Doesn't create the file

        historyDir = "./History/"
        currentPath = ImgSwtImage.path
        newIndex = str(len(self.undoActions))
        fileExtension = os.path.splitext(currentPath)[1]
        newPath = historyDir + newIndex + fileExtension
        print("newPath: " + newPath)
        return newPath