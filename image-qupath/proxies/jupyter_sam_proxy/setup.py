

import setuptools

setuptools.setup(
    name="jupyter-sam-proxy",
    author="Ami Trivedi",
    description="Proxy to start and stop SAM API Server",
    packages=setuptools.find_packages(),
    install_requires=[
        'jupyter-server-proxy'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            # ICON 1: Calls the start function
            'samapi_start = jupyter_sam_proxy:setup_sam_api',
            # ICON 2: Calls the stop function
            'samapi_stop = jupyter_sam_proxy:setup_sam_api_stop',
        ]
    },
    package_data={
        'jupyter_sam_proxy': ['icons/start.svg', 'icons/stop.svg'],
    },
)