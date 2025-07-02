# atmospheric_reentry

## Installation Guideline

This project is set up to create a containerized dev environment for OpenFOAM v1706 with the hypersonic solvers published by [hyStrath](https://github.com/hystrath/hyStrath) on Ubuntu 20.04. The following guidelines expect the developer to work in VScode. 

### 1. Prerequisites
Make sure to download [Visual Studio Code](https://code.visualstudio.com/download) and install the `Dev Containers` extension inside VScode. Moreover, we will need [Docker Desktop](https://docs.docker.com/desktop/setup/install/windows-install/#install-interactively). Follow the steps to [install interactively](https://docs.docker.com/desktop/setup/install/windows-install/#install-interactively).

![Dev Containers Extension](https://github.com/user-attachments/assets/de789831-f3fd-49b1-8684-1cc96db11104)

### 2. Clone this repository
Clone this repository to a location of your choice. Open the repository with Visual Studio Code.

### 3. Build container
After you opened the repository with VScode, the `Dev Containers` extension should recognize the container description inside `./.devcontainer`. By pressing `Ctrl + Shift + P` you enter the command terminal of VScode. Execute the command `Dev Containers: Reopen in Container` (or similar, cf. to following screenshot). This will trigger the build process of the container. This might take a while as several steps will be performed: installation of Ubuntu 20.04, compilation of OpenFOAM-v1706 and its third party libraries and lastly the cloning of the [hyStrath](https://github.com/hystrath/hyStrath) repository. 
![image](https://github.com/user-attachments/assets/7c3669bb-883b-4602-bc05-319fb30efc31)

To follow along and to make sure the process is not stuck, press `(show log)` in the pop up window in the bottom right after you started the container build process.

![image](https://github.com/user-attachments/assets/22c452b1-3268-468b-b5a4-a3ed23f381c3)

In case you would have to rebuild the container, the duration is expected to be much shorter as cached build files can be used.

### 4. Building HyStrath repo
After the container has been built, the hyStrath repository still needs to be built - theoretically, this should also be done during the build process of the container, but I did not manage to set it up correctly. Paste the following line into the terminal to start the built process. This will compile all three modules available in the hyStrath repository.
```
source ${WM_PROJECT_DIR}/etc/bashrc && export WM_PROJECT_USER_DIR=${HYSTRATH_BUILD_TARGET_DIR} && cd ${HYSTRATH_CLONE_DIR} && printf '4\n' | ./install.sh 16
```
After the compilation has finished, you should be able to enter `hy2Foam` into the terminal to see the solver trying to start, but failing due to a missing `controlDict` file. This means everything went according to plan and you are good to go to play around with hypersonic flows :D.


## What to find Where?

By default, the working directory of your terminal will be `/home/devuser/workspace`. At the same time, this folder will contain all the files and folders of this repository. Also, you can imagine this workspace as a tunnel to the host operating system of your laptop. In case you generated files which you would like to make available to your host system (e.g. because you would like to see something in ParaView), move these files into `/home/devuser/workspace` and they will appear in the file explorer of your host system at the location where you cloned this repository into. 

The source code of the HyStrath repository is located at `/home/devuser/hyStrath_source`. Copy the example cases to your workspace directory if you want to run, modify these cases. The compiled code is available at `/home/devuser/hyStrath_build` (although I do not expect to ever have to touch this build folder again in the course of this project :D).
