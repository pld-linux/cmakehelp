%define	snap	20070917
Summary:	Qt 4 based interface to cmake help
Summary(pl.UTF-8):	Oparty na Qt 4 interfejs do pomocy cmake
Name:		cmakehelp
Version:	0
Release:	0.%{snap}.1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://proli.net/meu/los_otros/%{name}.tar.bz2
# Source0-md5:	fab9ba5eb40c5c6a65be93fe74e02744
URL:		http://www.proli.net/2007/09/17/cmake-help/
Requires:	cmake
Requires:	python-PyQt4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qt 4 based interface to cmake help.

%description -l pl.UTF-8
Oparty na Qt 4 interfejs do pomocy cmake.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_bindir}}

cp *.py* *.ui $RPM_BUILD_ROOT%{_datadir}/%{name}

cat > $RPM_BUILD_ROOT%{_bindir}/cmakehelp << 'EOF'
cd %{_datadir}/%{name}
exec %{__python} main.py
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
