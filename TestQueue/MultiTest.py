import subprocess


def run_test():
    '''
    Launch a process queue of exporting a maya scene as usd and importing the usd into houdini scene.
    :return:
    '''
    # Launch a subprocess to run the maya engine script using mayapy.
    command = 'mayapy.exe "C:\\Users\\User\\PycharmProjects\\HeadlessMaya\\Engine\\MayaEngine.py"'
    test = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)

    # Wait for the first process to finish.
    poll = test.poll()
    while poll is None:
        poll = test.poll()

    # Launch a subprocess to run the houdini engine script using hython (only full path worked for me).
    command = '"C:\\Program Files\\Side Effects Software\\Houdini 18.5.696\\bin\\hython.exe" "C:\\Users\\User\\PycharmProjects\\HeadlessMaya\\Engine\\HoudiniEngine.py"'
    test = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
