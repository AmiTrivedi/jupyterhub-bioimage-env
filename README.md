## 🧬 JupyterHub Bioimage Environment

A **JupyterHub-based Docker image** with a pre-configured **Python environment**, including a wide range of tools for bioimage analysis such as:

- [CellProfiler](https://cellprofiler.org/)
- [Cellpose](https://www.cellpose.org/)
- [QuPath](https://qupath.github.io/)
- [SAMAPI](https://github.com/ksugar/samapi)

---

## 📦 Overview

This repository outlines two separate docker images ( image-cellprofiler and image-qupath )  configuration and Jupyter proxy integration used to support image analysis tools.

The base image we used here is based on the **University of Münster JupyterHub.nrw** [instace] (https://www.jupyterhub.nrw/de/). However, we are planning to build a separate, standalone base image to ensure accessibility and compatibility with various JupyterHub instances.

To build the image yourself, you can start with either

- A standard Linux base image (e.g., `ubuntu`, `debian`)
- A JupyterHub notebook base image (e.g., from [Jupyter Docker Stacks](https://jupyter-docker-stacks.readthedocs.io/en/latest/))

Make sure to install the necessary components, including:

- `noVNC`
- `X11`
- Other required dependencies for your image analysis tools

This setup enables support for **GUI-based applications** within the Jupyter notebook interface.

---

## 🧰 Installed Bioimage Tools and Plugins

| No. | Tool         | Version     | Plugins                                                                 |
|-----|--------------|-------------|-------------------------------------------------------------------------|
| 1   | CellProfiler | v4.2.8      | cellpose, stardist, omnipose                                        |
| 2   | Cellpose     | v3.1.1.2    | –                                                                       |
| 3   | QuPath       | v0.7.0      | Cellpose (0.10.2), StarDist, OMERO extension                            |
| 4   | SAMAPI server| v0.7.1      |                                                                         |

---

## 🔗 Useful Links

- [JupyterHub](https://jupyter.org/hub)
- [Jupyter Docker Stacks](https://jupyter-docker-stacks.readthedocs.io/en/latest/)
- [OMERO](https://www.openmicroscopy.org/omero/)

---









