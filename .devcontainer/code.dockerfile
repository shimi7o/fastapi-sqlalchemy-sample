FROM python:3.9.13

USER root

ARG USERNAME=student
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
  && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
  && apt-get update \
  && apt-get install -y sudo \
  && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
  && chmod 0440 /etc/sudoers.d/$USERNAME

USER ${USERNAME}

RUN pip install \
  black \
  flake8 \
  mypy

ENV PATH=$PATH:/home/$USERNAME/.local/bin

ENV DATABASE="mysql+pymysql" USER="root" PASSWORD="password" HOST="fastapi-sqlalchemy-sample-mysql" PORT="3306" DB_NAME="fastapi-sqlalchemy-sample"
