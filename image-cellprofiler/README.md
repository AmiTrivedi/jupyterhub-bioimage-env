
## Bioimage-Cellprofiler : with cellpose
## Dockerfile Cellprofiler, Cellpose for Image Analysis on jupyterhub 


## Tools:

- CellProfiler **4.2.8**
- Cellpose **3.1.1.2** (in cellprofiler environment)
- Cellpose GUI
- biabob, ezomero

## Plugins:

- cellpose
- stardist
- omnipose


## Version History

### v0.1.0
- Updated packages for Ubuntu 24.04
- Replace conda install instead of pip intall for some packages


Building Docker File

```
docker build . -t bioimage-cellprofiler:version

# run on jupyter lab locally

sudo docker run --name bioimage --rm --net=host -w "/usr/local/src" -e HOME="/tmp" bioimage-cellprofiler:version jupyter lab --ip 0.0.0.0 



# execute docker container at bash
docker exec -itu root bioimage-cellprofiler bash

```




