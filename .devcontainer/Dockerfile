# Use Ubuntu 20.04 as the base image (Crucial for GCC 7 compatibility)
FROM ubuntu:20.04

# Set environment variables for non-interactive installation
ENV DEBIAN_FRONTEND=noninteractive

# 1. Install essential build tools, add the toolchain PPA, and install GCC 7
RUN apt update && \
    apt install -y software-properties-common wget git build-essential flex bison cmake libscotch-dev libptscotch-dev bc gnuplot && \
    add-apt-repository -y ppa:ubuntu-toolchain-r/test && \
    apt update && \
    apt install -y gcc-7 g++-7 openmpi-bin openmpi-common libopenmpi-dev && \
    rm -rf /var/lib/apt/lists/*

# Set GCC 7 as the default compilers
# Priority 70 for GCC 7, higher than typical default to ensure it's selected
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 70 && \
    update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-7 70

# Verify compiler versions
RUN gcc --version && g++ --version

# Set OpenFOAM environment variables
ENV WM_NCOMPPROCS=16
ENV WM_DIR=/opt/OpenFOAM
ENV WM_PROJECT_INST_DIR=${WM_DIR}
ENV WM_PROJECT_VERSION=OpenFOAM-v1706
ENV WM_PROJECT_DIR=${WM_PROJECT_INST_DIR}/${WM_PROJECT_VERSION}
ENV WM_3RDPARTY_DIR=/opt/OpenFOAM/ThirdParty-v1706

# Create OpenFOAM directories
RUN mkdir -p ${WM_PROJECT_DIR} ${WM_3RDPARTY_DIR}

# Copy OpenFOAM source and ThirdParty files from the build context
# Ensure these files are in the same directory as your Dockerfile
COPY OpenFOAM-v1706.tgz ${WM_PROJECT_INST_DIR}/
COPY ThirdParty-v1706.tgz ${WM_PROJECT_INST_DIR}/

# Extract OpenFOAM and ThirdParty
RUN tar -xzf ${WM_PROJECT_INST_DIR}/OpenFOAM-v1706.tgz -C ${WM_PROJECT_INST_DIR} && \
    tar -xzf ${WM_PROJECT_INST_DIR}/ThirdParty-v1706.tgz -C ${WM_PROJECT_INST_DIR} && \
    rm ${WM_PROJECT_INST_DIR}/*.tgz # Clean up archives

# Source OpenFOAM environment and compile ThirdParty tools
# The 'bash -c' is needed to properly source the environment for subsequent commands
RUN bash -c "source ${WM_PROJECT_DIR}/etc/bashrc && \
    cd ${WM_3RDPARTY_DIR} && \
    ./Allwmake"

# Compile OpenFOAM
RUN bash -c "source ${WM_PROJECT_DIR}/etc/bashrc && \
    cd ${WM_PROJECT_DIR} && \
    ./Allwmake -j ${WM_NCOMPPROCS}"


# --- User Setup for Dev Container ---
    
# The user (devuser) will be created by the 'common-utils' feature.
# We just need to ensure Docker knows the subsequent steps (WORKDIR, CMD)
# should run as this user, and ensure it has a home directory.

# # Create the home directory for the user that will be created by the feature
# RUN mkdir -p /home/devuser && \
#     chown 1000:1000 /home/devuser
# Create the devuser and its home directory.  THIS MUST COME FIRST
RUN groupadd -g 1000 devuser && \
    useradd -m -u 1000 -g 1000 -s /bin/bash devuser && \
    apt update && \
    apt install -y sudo && \
    echo "devuser ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/devuser && \
    chmod 0440 /etc/sudoers.d/devuser && \
    rm -rf /var/lib/apt/lists/*
    
# Switch to the non-root user (which will be mapped to host UID/GID by the feature)
USER devuser

# Set the default working directory for the non-root user
WORKDIR /home/devuser/workspace


# --- hyStrath Setup ---

# # Create user project directory (WM_HYSTRATH_INST_DIR) for hyStrath
# ENV WM_HYSTRATH_INST_DIR=/opt/OpenFOAM/hyStrath
# # # Clone and build hyStrath (containing hy2foam)
# # # Assume hyStrath is cloned into WM_PROJECT_USER_DIR
# RUN bash -c "mkdir -p ${WM_HYSTRATH_INST_DIR} && cd ${WM_HYSTRATH_INST_DIR} && \
#     git clone --branch master --single-branch https://github.com/hystrath/hyStrath.git ${WM_HYSTRATH_INST_DIR} && \
#     printf '4\n' | bash install.sh ${WM_NCOMPPROCS}"
    
# # # Set default working directory inside the container
# # WORKDIR ${WM_PROJECT_USER_DIR}/hyStrath
# Define paths for hyStrath:
# 1. Clone location (as root during build)
ENV HYSTRATH_CLONE_DIR=/home/devuser/hyStrath_source
# 2. Final compiled build target (for devuser)
ENV HYSTRATH_BUILD_TARGET_DIR=/home/devuser/hyStrath_build

# Create the  clone directory
RUN echo "--- Creating hyStrath source clone directory ---" && \
    mkdir -p ${HYSTRATH_CLONE_DIR}

# Clone hyStrath source into the  directory (as root)
RUN echo "--- Cloning hyStrath repository source code into ${HYSTRATH_CLONE_DIR} ---" && \
    cd ${HYSTRATH_CLONE_DIR} && \
    git clone --branch master --single-branch https://github.com/hystrath/hyStrath.git .

# --- User-specific setup for devuser (still run as root in Dockerfile build phase) ---
# Set HOME for the expected user, assuming common-utils creates /home/devuser
ENV HOME=/home/devuser

# Create the final build target directory for hyStrath (as root)
# And assign ownership to the expected devuser UID/GID (1000:1000)
RUN echo "--- Creating hyStrath build target directory: ${HYSTRATH_BUILD_TARGET_DIR} ---" && \
    mkdir -p ${HYSTRATH_BUILD_TARGET_DIR}

# Install hy2foam using its dedicated script.
# This RUN command will be executed as root during the build.
# IMPORTANT: We explicitly export WM_PROJECT_USER_DIR to the subshell.
# RUN echo "--- Installing hy2Foam (module 4) into ${HYSTRATH_BUILD_TARGET_DIR} ---" && \
#     bash -c "source ${WM_PROJECT_DIR}/etc/bashrc && \
#     export WM_PROJECT_USER_DIR=${HYSTRATH_BUILD_TARGET_DIR} && \
#     cd ${HYSTRATH_CLONE_DIR} && \ 
#     printf '4\n' | bash ./install.sh ${WM_NCOMPPROCS}"

# Command to run when the container starts - provides a bash shell with OpenFOAM sourced
CMD ["bash", "-c", "source /opt/OpenFOAM/OpenFOAM-v1706/etc/bashrc && exec bash"]