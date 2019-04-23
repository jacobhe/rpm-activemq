rpm-acitvemq
===========

An RPM spec file to install Activemq.

To Build:

`sudo yum -y install rpmdevtools`

`rpmdev-setuptree`

`wget "http://www.apache.org/dyn/closer.cgi?filename=/activemq/$VERSION/apache-activemq-5.15.9-bin.tar.gz&action=download" -O apache-activemq-5.15.9.tar.gz`

`rpmbuild -bb ~/rpmbuild/SPECS/acitvemq.spec`

To clean the RPM build dir

`rpmdev-wipetree && rm -rf rpmbuild` 