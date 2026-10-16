## Bioimage-QuPath : with cellpose
## Dockerfile for Cellpose, QuPath, SAM for Image Analysis on jupyterhub 


## Tools:

- Cellpose  GUI **3.1.1.2** (in cellpose environment python 3.10)
- QuPath v0.7.0 (latest)
- SAM (QuPath extension v0.9.1 supports python 3.12)
- SAMAPI server 0.7.1 (workaround for downloading issue for SAM3 models)
- biabob, ezomero


## Extension for QuPath:

- cellpose (0.10.2)
- stardist (0.5.0)
- omero    (0.1.0)
- omero-java ice (5.6.15)



## Version History

### v0.1.0
- Updated packages for Ubuntu 24.04
- New samapi supports python 3.12 therefore removed extra python-environment

Building Docker File

```
docker build . -t bioimage-qupath:version

# run on jupyter lab locally

sudo docker run --name bioimage --rm --net=host -w "/usr/local/src" -e HOME="/tmp" bioimage-qupath:version jupyter lab --ip 0.0.0.0 



# execute docker container at bash
docker exec -itu root bioimage-qupath bash

```









