from maya import cmds 
import maya.api.OpenMaya as om

class Renamer():
    def __init__(self, selection = True):
        self.name = None
        
        self.input_ui()
        
        if not self.name:
            print("No input for name. Rename function won't run.")
            return
            
        if selection:
            self.renameSelection(self.name)

    def renameSelection(self, name):
        selList = om.MGlobal.getActiveSelectionList()
        dagNode = om.MFnDagNode()
        for i in range(selList.length()):
            path = selList.getDagPath(i)
            dagNode.setObject(path)
            try:
                dagNode.setName("{}_{}".format(name, i))
            except Exception as e:
                cmds.warning(e)
                
    
    def input_ui(self):    
        prompt = cmds.promptDialog(title = "Rename Hierarchy",
        message = "Name",
        button =['OK', "Cancel"],
        defaultButton = "OK",
        cancelButton = "Cancel",
        dismissString = "Cancel")
        
        if prompt == "OK":
            self.name = cmds.promptDialog(query = True, text = True)

if __name__ == "__main__":
    Renamer()