import os

def setup_cellpose():
    def _cellpose_command(port):
        return [ "/usr/bin/startvnc", str(port), "21", "/opt/conda/envs/cellprofiler/bin/cellpose" ]

    return {
        'command' : _cellpose_command,
        'environment' : {},
        'timeout' : 120,
        'launcher_entry' : {
            'title' : 'Cellpose',
         #   'category': 'X11 Applications', # disable X11 Appliations for now so that icons show up  in Notebook category
            'icon_path' : os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'Cellpose_Logo.svg')
        }
    }
