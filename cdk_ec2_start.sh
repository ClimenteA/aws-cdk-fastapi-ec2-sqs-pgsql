#!/bin/bash -xe
# Install OS packages
yum update -y
amazon-linux-extras install docker
service docker start
usermod -a -G docker ec2-user
chkconfig docker on


# Code Deploy Agent
# cd /home/ec2-user
# wget https://aws-codedeploy-us-west-2.s3.us-west-2.amazonaws.com/latest/install
# chmod +x ./install
# ./install auto