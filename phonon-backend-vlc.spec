
name: phonon-backend-vlc
Summary: VLC phonon backend
Version: 0.4.0
Release: 1%{?dist}
Group: Applications/Multimedia
License: LGPLv2+
URL:     http://phonon.kde.org/
%if 0%{?snap}
# git clone git://gitorious.org/phonon/phonon-vlc.git
# git archive --prefix=phonon-backend-vlc-%{version}/ master | bzip2 > phonon-vlc-%{version}-%{snap}.tar.bz2
Source0: phonon-vlc-%{version}-%{snap}.tar.bz2
%else
Source0: ftp://ftp.kde.org/pub/kde/stable/phonon/phonon-backend-vlc/%{version}/src/phonon-backend-vlc-%{version}.tar.bz2
%endif
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: automoc4 >= 0.9.86
BuildRequires: cmake >= 2.6.0
BuildRequires: phonon-devel >= 4.5.0
BuildRequires: kde-filesystem
BuildRequires: libxcb-devel
BuildRequires: libxml2-devel
BuildRequires: qt4-devel
BuildRequires: vlc-devel >= 1.1.1

%global phonon_ver %(pkg-config --modversion phonon 2>/dev/null || echo 4.5.0)
%global vlc_ver %(pkg-config --modversion libvlc 2>/dev/null || echo 1.1.0)

Provides: phonon-backend%{?_isa} = %{phonon_ver}

Requires: vlc-core%{?_isa} >= %{vlc_ver} 
Requires: phonon%{?_isa} >= %{phonon_ver}
Requires: qt4%{?_isa} >= %{_qt4_version}


%description
%{summary}.

%prep
%setup -q -n phonon-backend-vlc-%{version}%{?pre:-%{pre}}


%build

mkdir -p %{_target_platform}
pushd %{_target_platform}

%{cmake} \
  %{?_cmake_skip_rpath} \
  ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
rm -rf %{buildroot}

make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING.LIB
%{_kde4_libdir}/kde4/plugins/phonon_backend/phonon_vlc.so
%{_kde4_datadir}/kde4/services/phononbackends/vlc.desktop


%changelog
* Tue Apr 26 2011 Rex Dieter <rdieter@fedoraproject.org> - 0.4.0-1
- 0.4.0

* Wed Dec 01 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.3.1-1
- 0.3.1

* Tue Nov 30 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.3.0-1
- 0.3.0

* Sat Sep 11 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.2.0-2
- %%doc AUTHORS COPYING.LIB
- drop BR: pkgconfig

* Sun Jul 25 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.2.0-1
- phonon-backend-vlc-0.2.0 release

* Thu Jul 01 2010 Rex Dieter <rdieter@fedoraproject.org. - 0.2-0.7.20100701
- 20100701 snapshot

* Sun May 02 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.2-0.4.20100501
- 20100501 snapshot

* Mon Apr 26 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.2-0.3.20100420
- Provides: phonon-backend

* Tue Apr 20 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.2-0.2.20100420 
- phonon-vlc 20100420 snapshot 
