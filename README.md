# atmospheric_reentry

## Installation Guideline

This project is set up to create a containerized dev environment 


After the container has been built, the hyStrath repository still needs to be built - theoretically, this should also be done during the build process of the container, but I did not manage to set it up correctly. Paste the following line into the terminal to start the built process. This will compile all three modules available in the hyStrath repository.

```
source ${WM_PROJECT_DIR}/etc/bashrc && export WM_PROJECT_USER_DIR=${HYSTRATH_BUILD_TARGET_DIR} && cd ${HYSTRATH_CLONE_DIR} && printf '4\n' | ./install.sh 16
```

installation guideline (decently maintained): https://hpc.nmsu.edu/discovery/software/recipes/hy2foam/
