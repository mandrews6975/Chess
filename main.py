import eel
import platform
import sys

eel.init('web')
try:
    eel.start('main.html', mode='chrome', size=(1280, 720))
except EnvironmentError:
    if sys.platform in ['win32', 'win64'] and int(platform.release()) >= 10:
        eel.start('main.html', mode='edge', size=(1280, 720))
    else:
        raise
