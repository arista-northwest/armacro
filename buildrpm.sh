#!/bin/sh
# Created this script to remind myself that when building RPMs in
# Vagrant/VirtualBox the bdist-base must be changed
/usr/bin/env python setup.py bdist_rpm --bdist-base /tmp/armacro
