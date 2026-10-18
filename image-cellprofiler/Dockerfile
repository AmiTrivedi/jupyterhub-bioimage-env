# image version 0.1.0
# image-cellprofiler-----> only cellpose (in cellprofiler-env only) and cellprofiler

# Replace base image with your prefereed-base image

FROM jupyterhub/base

USER root:root

RUN cat /etc/apt/sources.list || true && ls /etc/apt/sources.list.d/ || true

# ------------------------------------------------------------
# System packages
# ------------------------------------------------------------
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y \
        software-properties-common \
        libxml2-dev libssl-dev python3-dev g++ libffi-dev freeglut3-dev xvfb libglib2.0-dev gnupg\
        make gcc build-essential libgtk-3-dev wget git default-jre xz-utils curl openssh-client xauth xorg unzip \
        libnotify-dev libsdl2-dev libwebkit2gtk-4.1-dev libiconv-hook-dev pkg-config libnotify4 libmysqlclient-dev \
        libblosc-dev libglu1-mesa libpulse-mainloop-glib0 libnss3 libasound2t64 qt5dxcb-plugin libsm6 libxcb-cursor0 libxcb-xinerama0 \
    && rm -rf /var/lib/apt/lists/*

# -----------------------------------------------------------
# Set PATH and ENV
# -----------------------------------------------------------

ENV JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64

ENV PATH=/opt/conda/bin:$PATH
ENV PATH=/usr/local/cuda/bin:$PATH

ENV LD_LIBRARY_PATH=/usr/local/cuda/lib64:/usr/lib/x86_64-linux-gnu:/usr/lib64:$LD_LIBRARY_PATH

# --------------------------------------------------------------
# CellProfiler Environment Python 3.9
# --------------------------------------------------------------

RUN conda create -n cellprofiler python=3.9 -y && \
    conda config --add channels conda-forge 

# Install Python dependencies 

RUN conda run -n cellprofiler pip install numpy centrosome "cellpose[GUI]==3.1.1.2" ezomero bia-bob stackview pyclesperanto && \
    conda run -n cellprofiler python -m pip install --upgrade pip wheel && \
    conda run -n cellprofiler pip install jpype1==1.4.1 && \
    conda run -n cellprofiler python -m pip install setuptools==69.0.0 && \
    conda install -n cellprofiler -c conda-forge wxpython=4.2.* python-javabridge typing_extensions mysqlclient mysql jupyterlab_widgets ipywidgets


  
# Cellprofiler Plugins
WORKDIR /opt
RUN git clone --branch v4.2.8 https://github.com/CellProfiler/CellProfiler.git
WORKDIR /opt/CellProfiler
RUN conda run -n cellprofiler pip install . --no-build-isolation


WORKDIR /opt
RUN git clone https://github.com/CellProfiler/CellProfiler-plugins.git
WORKDIR /opt/CellProfiler-plugins
RUN conda run -n cellprofiler pip install -e ".[cellpose,stardist,omnipose]"

# remove some plugins 
RUN rm -f \
    /opt/CellProfiler-plugins/active_plugins/runvista2d.py \
    /opt/CellProfiler-plugins/active_plugins/runilastik.py \
    /opt/CellProfiler-plugins/active_plugins/runimagejscript.py \
    /opt/CellProfiler-plugins/unmaintained_plugins/CellProfiler3/runimagej.py \
    /opt/CellProfiler-plugins/unmaintained_plugins/CellProfiler4_autoconverted/runimagej.py

# Patches 
COPY ./config/patch_runcellpose.py /tmp/patch_runcellpose.py
RUN conda run -n cellprofiler python /tmp/patch_runcellpose.py

# Download CellPose models 
COPY ./config/download_cellpose_models.py /
RUN conda run -n cellprofiler python /download_cellpose_models.py
RUN conda install -n cellprofiler -y ipykernel && \
    conda run -n cellprofiler python -m ipykernel install \
    --name cellprofiler \
    --display-name "Python CellProfiler_v4"

COPY ./config/CellProfilerLocal.cfg /tmp/

# ----------------------------------------------------------------
# Jupyterlab proxies
# ----------------------------------------------------------------
RUN mkdir -p /opt/proxies 
COPY ./proxies/ /opt/proxies
 
RUN pip install --no-cache-dir \
      "notebook>=4" \  
    /opt/proxies/jupyter_cellprofiler_proxy \
    /opt/proxies/jupyter_cellpose_proxy 
   
   
WORKDIR /usr/local/src
USER ${NB_UID}















