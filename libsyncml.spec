#TODO	- split devel package

Summary:	Libsyncml is a implementation of the SyncML protocol
Summary(pl):	Libsyncml jest implementacja protoko³u SyncML
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
Libsyncml is a implementation of the SyncML protocol

%description -l pl
Libsyncml jest implementacja protoko³u SyncML

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

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/syncml*
%attr(755,root,root) %{_libdir}/libsyncml.so*
%{_pkgconfigdir}/libsyncml-1.0.pc
%{_libdir}//libsyncml.la
%{_includedir}/libsyncml-1.0
