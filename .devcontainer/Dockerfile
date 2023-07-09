FROM jupyter/minimal-notebook:lab-3.6.3

# USER root

# USER jovyan

WORKDIR /home/jovyan


COPY env-jup.yml env-jup.yml
RUN conda env update -f env-jup.yml && \
    rm env-jup.yml

COPY .devcontainer/jupyter/ /home/${NB_USER}/.jupyter/lab/

USER root

RUN fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}" && \
    fix-permissions "/home/${NB_USER}/.jupyter/lab/"

USER jovyan

RUN jupyter lab build

ENV PYTHONPATH="/src/app:/src/app/tests"

USER root

# RUN echo "root:a"|chpasswd

USER jovyan

COPY env-app.yml env-app.yml
RUN conda env update -f env-app.yml && \
    rm env-app.yml

RUN source activate app && \
    python -m ipykernel install --user --name app --display-name "app"
RUN jupyter kernelspec uninstall --y python3

# USER root