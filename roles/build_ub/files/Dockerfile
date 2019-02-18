# version 2.0.0
FROM phusion/baseimage
MAINTAINER Oleksandr Panfilov
COPY inventories/production/group_vars/all/id_rsa.pub /root/.ssh/authorized_keys
RUN apt-get update
RUN apt-get install -y python-simplejson
RUN apt-get install -y openssh-server
RUN service ssh start
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
