import hou


def import_usd(scene_path, usd_path):
    '''
    Import the given usd to the given scene.
    :param scene_path:
    :param usd_path:
    :return:
    '''
    # Open the houdini scene.
    hou.hipFile.load(scene_path)

    # Create a new geomatry node.
    hou.node("/obj").createNode("geo", "test_geomatry")

    # Create a new file node.
    hou.node("/obj/test_geomatry").createNode("file", "test")

    # Set the geomatry file path to the usd path.
    file = hou.node("/obj/test_geomatry/test")
    file.parm("file").set(usd_path)

    # Save the houdini scene
    hou.hipFile.save(scene_path)


if __name__ == "__main__":
    import_usd("C:/Users/User/GavGav.hipnc",
               "C:/Users/User/Desktop/SchoolFiles/Pipeline/MOVIE/ASSETS/CAR/SURFACING/WIP/CAR_SURFACING_V002.ma.usd")
