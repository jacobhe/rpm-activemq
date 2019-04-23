VERSION=$(grep "Version:" activemq.spec |cut -d ":" -f2 |tr -d "[:space:]")
RELEASE=$(grep "Release:" activemq.spec |cut -d ":" -f2 |tr -d "[:space:]")
ARCH=$(grep "BuildArch:" activemq.spec |cut -d ":" -f2 |tr -d "[:space:]")

echo "Version: $VERSION-$RELEASE BuildArch: $ARCH"

rm -rf rpmbuild
mkdir rpmbuild
mkdir rpmbuild/BUILD
mkdir rpmbuild/RPMS
mkdir rpmbuild/SOURCES
mkdir rpmbuild/SPECS
mkdir rpmbuild/SRPMS

wget "http://www.apache.org/dyn/closer.cgi?filename=/activemq/$VERSION/apache-activemq-$VERSION-bin.tar.gz&action=download" -O apache-activemq-$VERSION.tar.gz

ln -v -s "$(pwd)/apache-activemq-$VERSION.tar.gz" "rpmbuild/SOURCES/"
ln -v -s "$(pwd)/activemq."{logrotate,service} "rpmbuild/SOURCES/"
ln -v -s "$(pwd)/activemq.spec" "rpmbuild/SPECS/"

cd rpmbuild

rpmbuild --buildroot "`pwd`/BUILDROOT" ../activemq.spec -bb --define "_topdir `pwd`"

#publish-rpm $VERSION $RELEASE $ARCH activemq "RPMS/$ARCH/activemq-$VERSION-$RELEASE.$ARCH.rpm"

