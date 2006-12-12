Summary:	Libsyncml - an implementation of the SyncML protocol
Summary(pl):	Libsyncml - implementacja protoko³u SyncML
Name:		libsyncml
Version:	0.4.1
Release:	3
License:	LGPL
Group:		Libraries
Source0:	http://libsyncml.opensync.org/attachment/wiki/download/%{name}-%{version}.tar.gz?format=raw
# Source0-md5:	7a9261dd4d2a6049f064f16054af3187
URL:		http://libsyncml.opensync.org/
BuildRequires:	check
BuildRequires:	libsoup-devel
BuildRequires:	libxml2-devel
BuildRequires:	openobex-devel >= 1.3
BuildRequires:	wbxml2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libsyncml is a implementation of the SyncML protocol.

%description -l pl
Libsyncml jest implementacj± protoko³u SyncML.

%package devel
Summary:	Header files for libsyncml library
Summary(pl):	Pliki nag³ówkowe biblioteki libsyncml
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libsyncml library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libsyncml.

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
