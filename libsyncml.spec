Summary:	Libsyncml - an implementation of the SyncML protocol
Summary(pl.UTF-8):	Libsyncml - implementacja protokołu SyncML
Name:		libsyncml
Version:	0.4.7
Release:	0.1
License:	LGPL
Group:		Libraries
Source0:	http://libsyncml.opensync.org/download/releases/0.4.7/%{name}-%{version}.tar.bz2
# Source0-md5:	03f5696b8c55ecdb90da076819b1747f
URL:		http://libsyncml.opensync.org/
BuildRequires:	check
BuildRequires:	libsoup-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	openobex-devel >= 1.3
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.385
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
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" != "lib"
	-DLIB_SUFFIX=64 \
%endif
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/syncml*
%attr(755,root,root) %{_libdir}/libsyncml.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsyncml.so.?

%files devel
%defattr(644,root,root,755)
%{_libdir}/libsyncml.so
%{_includedir}/libsyncml-1.0
%{_pkgconfigdir}/libsyncml-1.0.pc
