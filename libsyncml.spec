Summary:	Libsyncml - an implementation of the SyncML protocol
Summary(pl):	Libsyncml - implementacja protokołu SyncML
Name:		libsyncml
Version:	0.4.0
Release:	0.1
License:	LGPL
Group:		Libraries
Source0:	http://libsyncml.opensync.org/attachment/wiki/download/%{name}-%{version}.tar.gz?format=raw
# Source0-md5:	a6b5becd4b61e246ed2ee95db9f6e746
URL:		http://libsyncml.opensync.org/
BuildRequires:	wbxml2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libsyncml is a implementation of the SyncML protocol.

%description -l pl
Libsyncml jest implementacją protokołu SyncML.

%package devel
Summary:	Header files for libsyncml library
Summary(pl):	Pliki nagłówkowe biblioteki libsyncml
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libsyncml library.

%description devel -l pl
Pliki nagłówkowe biblioteki libsyncml.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/syncml*
%attr(755,root,root) %{_libdir}/libsyncml.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsyncml.so*
%{_libdir}/libsyncml.la
%{_includedir}/libsyncml-1.0
%{_pkgconfigdir}/libsyncml-1.0.pc
