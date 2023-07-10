# CQF Labs in docker container

Setup encapsulates the whole environment in a docker container, so it works the same on all machines and doesn't clash with other workspaces. There are two kernels inside the image - one for jupyter, other one for the labs (app). I've split them so Jupyter setups and version requirements don't mess up with application setups.

## Browse Notebooks

GitHub displays bare minimum of the notebooks output. To see more, like charts, you need to use the nbviewer and paste the github link there.

Click [here](https://nbviewer.org/github/wojciechfrys/CQF_Labs/tree/master/) to see the repo under nbviewer.

## Setup

1. Requirements
    You need only 2 applications. Docker desktop for handling the Virtual Machines and VS Code as an IDE that handles Docker. Generally follow [here](https://code.visualstudio.com/docs/devcontainers/containers#_installation) for more detailed steps.
    * Install Docker Desktop from [here](https://www.docker.com/products/docker-desktop).
    * Install VS Code from [here](https://code.visualstudio.com/download).
        * Instal Dev Container extension from [here](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).

2. Start up
    1. Open VS Code
    1. `File -> Open Folder...` and select the folder with this repository.
    1. Press `F1` or `ctrl + shift + p` for Command Pallet (little popup window at the top of the screen). Type `> Dev Containers: Rebuild and Reopen in Container` and press enter.
        * VS Code should take 10-20 minutes to download all the packages and build environment.
        * In bottom right there should be blue `show logs` that you can click to see the download progress.
    1. Once the image is build it is done. To start jupyter press `F1` or `ctrl + shift + p` for Command Pallet, type `>Tasks: Run Task`, press enter and select `jupyter`. In your browser go to [localhost:8888](http://localhost:8888/). Jupyter should be working there.

