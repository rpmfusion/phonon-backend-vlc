
name: phonon-backend-vlc
Summary: VLC phonon backend
Version: 0.8.2
Release: 1%{?dist}

License: LGPLv2+
URL:     http://phonon.kde.org/
%if 0%{?snap}
# git clone git://anongit.kde.org/phonon-vlc; cd phonon-vlc
# git archive --prefix=phonon-backend-vlc-%{version}/ master | xz > phonon-backend-vlc-%{version}-%{snap}.tar.xz
Source0: phonon-backend-vlc-%{version}-%{snap}.tar.xz
%else
Source0: http://download.kde.org/stable/phonon/phonon-backend-vlc/%{version}/src/phonon-backend-vlc-%{version}.tar.xz
%endif

## downstream patches
# reset initial preference below (fedora's default) gstreamer
Patch1: phonon-backend-vlc-0.7.0-initial_preference.patch

BuildRequires: automoc4 >= 0.9.86
BuildRequires: cmake 
BuildRequires: kde-filesystem
BuildRequires: pkgconfig(libvlc) >= 1.1.10
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(phonon) >= 4.7.80
BuildRequires: pkgconfig(phonon4qt5) >= 4.7.80
BuildRequires: pkgconfig(QtGui)
BuildRequires: pkgconfig(Qt5Gui) pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(xcb) 
# Oh, the irony of being in the default buildroot @ rpmfusion
BuildRequires: phonon-backend-gstreamer

%global phonon_ver %(pkg-config --modversion phonon 2>/dev/null || echo 4.7.0)
%global vlc_ver %(pkg-config --modversion libvlc 2>/dev/null || echo 1.1.10)

Provides: phonon-backend%{?_isa} = %{phonon_ver}

Requires: vlc-core%{?_isa} >= %{vlc_ver} 
Requires: phonon%{?_isa} >= %{phonon_ver}
%{?_qt4_version:Requires: qt4%{?_isa} >= %{_qt4_version}}

%package -n phonon-qt5-backend-vlc
Summary:  Vlc phonon-qt5 backend
Provides: phonon-qt5-backend%{?_isa} = %{phonon_version}
%{?_qt5_version:Requires: qt5-qtbase%{?_isa} >= %{_qt5_version}}
%description -n phonon-qt5-backend-vlc
%{summary}.

%description
%{summary}.


%prep
%setup -q -n phonon-backend-vlc-%{version}%{?pre:-%{pre}}

%patch1 -p1 -b .initial_preference


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} ..
make %{?_smp_mflags}
popd

mkdir -p %{_target_platform}-Qt5
pushd %{_target_platform}-Qt5
%{cmake} -DPHONON_BUILD_PHONON4QT5:BOOL=ON ..
make %{?_smp_mflags}
popd


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}-Qt5
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%files
%doc AUTHORS COPYING.LIB
%{_kde4_libdir}/kde4/plugins/phonon_backend/phonon_vlc.so
%{_kde4_datadir}/kde4/services/phononbackends/vlc.desktop

%files -n phonon-qt5-backend-vlc
%doc AUTHORS COPYING.LIB
%{_qt5_plugindir}/phonon4qt5_backend/phonon_vlc.so


%changelog
* Fri Dec 12 2014 Rex Dieter <rdieter@fedoraproject.org> 0.8.2-1
- 0.8.2

* Mon Nov 17 2014 Nicolas Chauvet <kwizart@gmail.com> - 0.8.1-2
- Rebuild for vlc 2.2.0

* Sat Nov 08 2014 Rex Dieter <rdieter@fedoraproject.org> 0.8.1-1
- 0.8.1

* Mon Sep 08 2014 Rex Dieter <rdieter@fedoraproject.org> 0.8.0-1
- 0.8.0

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Dec 06 2013 Rex Dieter <rdieter@fedoraproject.org> 0.7.1-1
- 0.7.1

* Wed Nov 06 2013 Rex Dieter <rdieter@fedoraproject.org> 0.7.0-1
- 0.7.0, Qt5 support

* Wed Oct 02 2013 Rex Dieter <rdieter@fedoraproject.org> 0.6.2-2
- rebuild (vlc)

* Wed Feb 13 2013 Rex Dieter <rdieter@fedoraproject.org> 0.6.2-1
- 0.6.2

* Tue Nov 13 2012 Rex Dieter <rdieter@fedoraproject.org> 0.6.1-1
- 0.6.1

* Mon Aug 20 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.6.0-3
- Rebuilt (branching)

* Sat Aug 11 2012 Rex Dieter <rdieter@fedoraproject.org> 0.6.0-1
- 0.6.0

* Fri Mar 02 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.5.0-2
- Rebuilt for c++ ABI breakage

* Sat Feb 18 2012 Rex Dieter <rdieter@fedoraproject.org> 0.5.0-1
- 0.5.0

* Sat Jan 07 2012 Rex Dieter <rdieter@fedoraproject.org> 0.5.0-0.2.20120107git
- 20120107 (master branch) snapshot

* Mon Dec 12 2011 Rex Dieter <rdieter@fedoraproject.org> 0.5.0-0.1.20111212git
- 20111212 (master branch) snapshot

* Fri Oct 21 2011 Rex Dieter <rdieter@fedoraproject.org> 0.4.55-0.1.20111021
- 20111021 snapshot
- pkgconfig-style deps

* Mon Aug 15 2011 Rex Dieter <rdieter@fedoraproject.org> 0.4.1-2
- rebuild

* Mon Aug 01 2011 Rex Dieter <rdieter@fedoraproject.org> 0.4.1-1
- 0.4.1

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
