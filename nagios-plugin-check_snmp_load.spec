%include	/usr/lib/rpm/macros.perl
Summary:	Nagios plugin to check system load via SNMP
Summary(pl.UTF-8):	Wtyczka Nagiosa do sprawdzania obciążenia systemu poprzez SNMP
Name:		nagios-plugin-check_snmp_load
Version:	1.2
Release:	1
License:	GPL
Group:		Networking
Source0:	http://patrick.proy.free.fr/nagios/check_snmp_load.pl
# Source0-md5:	c28aeb0029afc7e839ade6e85f47a25b
Source1:	check_snmp_load.cfg
Patch0:		%{name}-paths.patch
URL:		http://patrick.proy.free.fr/nagios/snmp_load.html
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	sed >= 4.0
Requires:	nagios-core
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%{_libdir}/nagios/plugins
%define		_sysconfdir	/etc/nagios/plugins

%define		_noautoreq 'perl(utils)'

%description
Checks by SNMP load or CPU usage (Windows, Linux/Unix, AS400, Cisco,
Cisco Catalyst, HP Procurve, LinkProof, Blucoat, Nokia, Fortinet,
Netscreen).

%description -l pl.UTF-8
Ta wtyczka sprawdza poprzez SNMP obciążenie lub wykorzystanie CPU w
systemach Windows, Linux/Unix, AS400, Cisco, Cisco Catalyst, HP
Procurve, LinkProof, Blucoat, Nokia, Fortinet, Netscreen.

%prep
%setup -q -c -T
install %{SOURCE0} .
%patch0 -p1
sed -i -e 's,@plugindir@,%{_plugindir},' check_snmp_load.pl

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_plugindir}}
install check_snmp_load.pl $RPM_BUILD_ROOT%{_plugindir}/check_snmp_load
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_plugindir}/*
