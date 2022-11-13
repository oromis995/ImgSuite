import os
from ImgSwtImage import ImgSwtImage
# TO DO
#   NEED TO MAKE PROJECT FILE FORMAT

class Project():

    redoActions = []
    undoActions = []

    def getNewPath(self, ImgSwtImage):
        # Figures out the name of the next file
        # Each file has an index
        # Doesn't create the file

        historyDir = "./Source/History/"
        currentPath = ImgSwtImage.path
        newIndex = str(len(self.undoActions))
        fileExtension = os.path.splitext(currentPath)[1]
        newPath = historyDir + newIndex + fileExtension
        print("newPath: " + newPath)
        return newPath
    
    def undo(self, myRoot):

        if len(self.undoActions) >= 2:
            self.redoActions.append(self.undoActions.pop())
            myRoot.image.loadImage(self.undoActions.pop(), myRoot, self)
            print("undoStack",self.undoActions,"redoStack",self.redoActions)

    def redo(self, myRoot):

        if len(self.redoActions) >= 1:
            myRoot.image.loadImage(self.redoActions.pop(), myRoot, self)
            print("undoStack",self.undoActions,"redoStack",self.redoActions)
    
    def emptyRedoStack(self):
        self.redoActions = []