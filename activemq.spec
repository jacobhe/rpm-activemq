# To Build:
#
# sudo yum -y install rpmdevtools && rpmdev-setuptree
#
# rpmbuild -bb ~/rpmbuild/SPECS/activemq.spec

%define debug_package %{nil}
%define __jar_repack %{nil}
%define activemq_home /opt/activemq
%define activemq_group activemq
%define activemq_user activemq

Summary:    Apache ActiveMQ
Name:       activemq
Version:    5.15.9
BuildArch:  x86_64
Release:    1
License:    Apache Software License
Group:      Networking/Daemons
URL:        http://activemq.apache.org
Source0:    apache-activemq-%{version}.tar.gz
Source1:    %{name}.service
Source2:    %{name}.logrotate
BuildRequires:    systemd-units
Requires:   jpackage-utils
Requires(pre): shadow-utils
Requires(post):   systemd-units
Requires(preun):  systemd-units
Requires(postun): systemd-units
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Apache ActiveMQ is the most popular and powerful open source messaging
and Integration Patterns server.

Apache ActiveMQ is fast, supports many Cross Language Clients and
Protocols, comes with easy to use Enterprise Integration Patterns and
many advanced features while fully supporting JMS 1.1 and J2EE 1.4.

%prep
%setup -q -n apache-activemq-%{version}

%build

%install
install -d -m 755 %{buildroot}/%{activemq_home}/
cp -R * %{buildroot}/%{activemq_home}/

# Remove *.bat
rm -f %{buildroot}/%{activemq_home}/bin/*.bat

# Drop service script
install -d -m 755 %{buildroot}/%{_unitdir}
install    -m 644 %_sourcedir/%{name}.service %{buildroot}/%{_unitdir}/%{name}.service

# Drop logrotate script
install -d -m 755 %{buildroot}/%{_sysconfdir}/logrotate.d
install    -m 644 %_sourcedir/%{name}.logrotate %{buildroot}/%{_sysconfdir}/logrotate.d/%{name}

%clean
rm -rf %{buildroot}

%pre
getent group %{activemq_group} >/dev/null || groupadd -r %{activemq_group}
getent passwd %{activemq_user} >/dev/null || /usr/sbin/useradd --comment "Acitvemq Daemon User" --shell /sbin/nologin -M -r -g %{activemq_group} --home %{activemq_home} %{activemq_user}

%files
%defattr(-,%{activemq_user},%{activemq_group})
%{activemq_home}
%defattr(-,root,root)
%{_unitdir}/%{name}.service
%{_sysconfdir}/logrotate.d/%{name}

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%changelog
* Mon Apr 22 2019 kaha2010@gmail.com
  - Initial packaging
