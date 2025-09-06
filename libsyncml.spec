Summary:	Libsyncml - an implementation of the SyncML protocol
Summary(pl.UTF-8):	Libsyncml - implementacja protokołu SyncML
Name:		libsyncml
Version:	0.5.4
Release:	3
License:	LGPL 2.1+
Group:		Libraries
Source0:	https://downloads.sourceforge.net/libsyncml/%{name}-%{version}.tar.bz2
# Source0-md5:	b8ce1f222cccc12acdcd6807d65c1aea
Patch0:		wbxml.patch
Patch1:		%{name}-openobex.patch
Patch2:		%{name}-types.patch
# dead
#URL:		http://libsyncml.opensync.org/
BuildRequires:	bluez-libs-devel
BuildRequires:	cmake
BuildRequires:	glib2-devel >= 1:2.12
BuildRequires:	libsoup-devel >= 2.2.91
BuildRequires:	libwbxml-devel >= 0.10.0
BuildRequires:	libxml2-devel
BuildRequires:	openobex-devel >= 1.6
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.385
BuildRequires:	sed >= 4.0
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
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

# CHECK_FOUND resets ENABLE_UNIT_TEST to ON
%{__sed} -i '/FIND_PACKAGE( Check )/d' CMakeLists.txt

%build
install -d build
cd build
%cmake .. \
	-DENABLE_UNIT_TEST=OFF

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
%ghost %{_libdir}/libsyncml.so.2

%files devel
%defattr(644,root,root,755)
%{_libdir}/libsyncml.so
%{_includedir}/libsyncml-1.0
%{_pkgconfigdir}/libsyncml-1.0.pc
