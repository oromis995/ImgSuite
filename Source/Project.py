import os
from ImgSwtImage import ImgSwtImage
from xml.dom import minidom


# TO DO
#   NEED TO MAKE PROJECT FILE FORMAT

class Project():

    redoActions = []
    undoActions = []
    projectName = "defaultName"

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
    
    def saveDataToXML(self):
        
        # Document object is created here 
        root = minidom.Document()

        # Root Node 'Project' is created here
        project_RootNode = root.createElement('Project')
        project_RootNode.setAttribute('name', self.projectName)
        root.appendChild(project_RootNode)

        # Undo and Redo child nodes are created and added
        undo_Node = root.createElement('undoList')
        redo_Node = root.createElement('redoList')
        project_RootNode.appendChild(undo_Node)
        project_RootNode.appendChild(redo_Node)

        # Undo and Redo Items are created as child nodes and added
        for element in self.undoActions:
            newNode = root.createElement('File')
            newNode.setAttribute('name', str(element))
            undo_Node.appendChild(newNode)
        for element in self.redoActions:
            newNode = root.createElement('File')
            newNode.setAttribute('name', str(element))
            redo_Node.appendChild(newNode)

        # File is written to disk
        xml_str = root.toprettyxml(indent ="\t")
        if not os.path.exists('./Projects/'+self.projectName+'/'):
            os.makedirs('./Projects/'+self.projectName+'/')
        outputDir = './Projects/'+self.projectName+'/'+'ProjectData.xml'
        with open(outputDir, "w") as f:
            f.write(xml_str)
    