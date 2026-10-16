import os

def setup_cellpose():
    def _cellpose_command(port):
        return [ "/usr/bin/startvnc", str(port), "21", "/opt/conda/envs/cellpose/bin/cellpose" ]

    return {
        'command' : _cellpose_command,
        'environment' : {},
        'timeout' : 120,
        'launcher_entry' : {
            'title' : 'Cellpose',
            'icon_path' : os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'Cellpose_Logo.svg')
        }
    }
