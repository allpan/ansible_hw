# version 2.0.0
FROM centos/systemd
MAINTAINER Oleksandr Panfilov
COPY inventories/production/group_vars/all/id_rsa.pub /root/.ssh/authorized_keys
RUN chmod 644 /root/.ssh/authorized_keys
RUN yum install -y openssh-server
RUN yum clean all
RUN systemctl enable sshd.service
RUN yum install -y epel-release
EXPOSE 22
CMD ["/usr/sbin/init"]
