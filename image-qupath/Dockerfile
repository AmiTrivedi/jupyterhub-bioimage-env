# image version 0.1.0
# image-qupath---contains only cellpose (in cellpose-env only) and QuPath-SAM

# Replace base image with your prefereed-base image

FROM jupyterhub/base

ENV LD_LIBRARY_PATH=/usr/lib:$LD_LIBRARY_PATH 
USER root:root


# ------------------------------------------------------------
# System packages
# ------------------------------------------------------------

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y \
        software-properties-common \
        libxml2-dev libssl-dev python3-dev g++ libffi-dev freeglut3-dev xvfb libglib2.0-dev \
        make gcc build-essential libgtk-3-dev wget git default-jre xz-utils curl openssh-client xauth xorg unzip \
        libnotify-dev libsdl2-dev libwebkit2gtk-4.1-dev libiconv-hook-dev pkg-config libnotify4 libmysqlclient-dev \
        libblosc-dev libglu1-mesa libpulse-mainloop-glib0 libnss3 libasound2t64 qt5dxcb-plugin libsm6 libxcb-cursor0 libxcb-xinerama0 \
    && rm -rf /var/lib/apt/lists/*   

# -----------------------------------------------------------
# Set PATH and ENV
# -----------------------------------------------------------
ENV JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64
ENV PATH=/opt/conda/bin:$PATH
RUN PATH=/usr/local/cuda-11.8/bin:$PATH
RUN LD_LIBRARY_PATH=/usr/local/cuda-11.8/lib64:$LD_LIBRARY_PATH



# -----------------------------------------------------------
# Cellpose GUI  version 3.1.1.2
# -----------------------------------------------------------

RUN conda create -n cellpose python=3.10 -y
RUN conda run -n cellpose pip install "cellpose[gui]==3.1.1.2"

# -----------------------------------------------------------
# QuPATH version 0.7.0
# -----------------------------------------------------------

WORKDIR /opt
RUN wget https://github.com/qupath/qupath/releases/download/v0.7.0/QuPath-v0.7.0-Linux.tar.xz && \
    tar -xf QuPath-v0.7.0-Linux.tar.xz && \
    rm QuPath-v0.7.0-Linux.tar.xz && \
    chmod a+x /opt/QuPath/bin/QuPath
RUN chown -R root:root /opt/QuPath

# -----------------------------------------------------------
# QuPATH extenstions
# -----------------------------------------------------------

RUN mkdir /opt/QuPath/lib/app/extensions
WORKDIR /opt/QuPath/lib/app/extensions
RUN wget https://github.com/BIOP/qupath-extension-cellpose/releases/download/v0.10.2-code/qupath-extension-cellpose-0.10.2.zip && \
    unzip qupath-extension-cellpose-0.10.2.zip && \
    rm qupath-extension-cellpose-0.10.2.zip && \
    wget https://github.com/qupath/qupath-extension-stardist/releases/download/v0.5.0/qupath-extension-stardist-0.5.0.jar && \
    wget https://github.com/qupath/qupath-extension-omero/releases/download/v0.1.0/qupath-extension-omero-0.1.0.jar && \
    wget https://github.com/ome/openmicroscopy/releases/download/v5.6.15/OMERO.java-5.6.15-ice36.zip && \
    unzip OMERO.java-5.6.15-ice36.zip && \
    rm OMERO.java-5.6.15-ice36.zip

# -----------------------------------------------------------
# QuPATH-extension-SAM version 0.9.1 , SAMAPI server 0.7.1
# -----------------------------------------------------------

WORKDIR /opt/QuPath/lib/app/extensions
RUN wget https://github.com/ksugar/qupath-extension-sam/releases/download/v0.9.1/qupath-extension-sam-0.9.1-all.jar
RUN python -m pip install git+https://github.com/ksugar/samapi.git@v0.7.1

RUN conda install -n cellpose -y ipykernel && \
    conda run -n cellpose python -m ipykernel install --name cellpose --display-name "Python Cellpose_v3"


COPY ./config/script.groovy /opt  
COPY ./config/sam_manager.sh /usr/local/bin/sam_manager.sh
RUN chmod +x /usr/local/bin/sam_manager.sh


# ----------------------------------------------------------------
# Jupyterlab proxies
# ----------------------------------------------------------------
    
RUN mkdir -p /opt/proxies 
COPY ./proxies/ /opt/proxies
 
RUN pip install --no-cache-dir \
      "notebook>=4" \  
    /opt/proxies/jupyter_cellpose_proxy \
    /opt/proxies/jupyter_qupath_proxy \
    /opt/proxies/jupyter_sam_proxy
   

WORKDIR /usr/local/src
USER ${NB_UID}









