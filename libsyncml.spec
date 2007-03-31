Summary:	Libsyncml - an implementation of the SyncML protocol
Summary(pl.UTF-8):	Libsyncml - implementacja protokołu SyncML
Name:		libsyncml
Version:	0.4.4
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://libsyncml.opensync.org/attachment/wiki/download/%{name}-%{version}.tar.bz2?format=raw
# Source0-md5:	192f42dc0a17e43edf5f893f1ca7fa5b
URL:		http://libsyncml.opensync.org/
BuildRequires:	check
BuildRequires:	libsoup-devel
BuildRequires:	libxml2-devel
BuildRequires:	openobex-devel >= 1.3
BuildRequires:	wbxml2-devel >= 0.9.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libsyncml is a implementation of the SyncML protocol.

%description -l pl.UTF-8
Libsyncml jest implementacją protokołu SyncML.

%package devel
Summary:	Header files for libsyncml library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libsyncml
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libsyncml library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libsyncml.

%prep
%setup -q

%build
%configure \
  --enable-http \
  --enable-obex \
  --enable-bluetooth \
  --enable-tools \
  --enable-unit-tests \
  --enable-tracing \

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
%{_mandir}/man1/syncml-http-server.1*
%{_mandir}/man1/syncml-obex-client.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsyncml.so
%{_libdir}/libsyncml.la
%{_includedir}/libsyncml-1.0
%{_pkgconfigdir}/libsyncml-1.0.pc
