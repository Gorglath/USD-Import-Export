import maya.standalone as ms

ms.initialize(name='python')
import maya.cmds as cmds


def export_usd(path):
    '''
    Load the given scene and export content as usd.
    :param path:
    :return:
    '''

    # Load maya usd plugin.
    cmds.loadPlugin("mayaUsdPlugin.mll")

    # Open the scene, add the usd file ending to the path.
    cmds.file(path, o=True)
    path += ".usd"

    # Import all references before exporting.
    refs = cmds.ls(type='reference')
    for ref in refs:
        ref_file = cmds.referenceQuery(ref, f=True)
        cmds.file(ref_file, importReference=True)

    # Export the scene as usd.
    cmds.file(rename=path)
    cmds.file(ea=True, type="USD Export", f=True)

    ms.uninitialize()
    return True


if __name__ == "__main__":
    export_usd('C:/Users/User/Desktop/SchoolFiles/Pipeline/MOVIE/ASSETS/CAR/SURFACING/WIP/CAR_SURFACING_V002.ma')
