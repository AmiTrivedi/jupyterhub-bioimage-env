
import os

def setup_sam_api():
    def _sam_api_command(port):
        # Call the script with 'start' and the assigned port
        return [ "/bin/bash", "/usr/local/bin/sam_manager.sh", "start", str(port) ]

    return {
        'command' : _sam_api_command,
        'environment' : {},
        'timeout' : 60, # Increased timeout to give the server time to boot
        'launcher_entry' : {
            'title' : 'START SAM API',
            'icon_path' : os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'start.svg')
        }
    }

def setup_sam_api_stop():
    def _sam_api_stop_command(port):
        # Call the script with 'stop' and the assigned port
        return [ "/bin/bash", "/usr/local/bin/sam_manager.sh", "stop", str(port) ]

    return {
        'command' : _sam_api_stop_command,
        'environment' : {},
        'timeout' : 60,
        'launcher_entry' : {
            'title' : 'STOP SAM API',
            'icon_path' : os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'stop.svg')
        }
    }