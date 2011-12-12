
%define snap 20111212

name: phonon-backend-vlc
Summary: VLC phonon backend
Version: 0.5.0
Release: 0.1.%{snap}git%{?dist}
Group: Applications/Multimedia
License: LGPLv2+
URL:     http://phonon.kde.org/
%if 0%{?snap}
# git clone git://anongit.kde.org/phonon-vlc
# git archive --prefix=phonon-backend-vlc-%{version}/ master | bzip -9 > phonon-vlc-%{version}-%{snap}.tar.bz2
Source0: phonon-backend-vlc-%{version}-%{snap}.tar.bz2
%else
Source0: ftp://ftp.kde.org/pub/kde/stable/phonon/phonon-backend-vlc/%{version}/phonon-backend-vlc-%{version}.tar.xz
%endif
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: automoc4 >= 0.9.86
BuildRequires: cmake >= 2.6.0
BuildRequires: kde-filesystem
BuildRequires: pkgconfig(libvlc) >= 1.1.10
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(phonon) >= 4.5.50
BuildRequires: pkgconfig(QtCore) pkgconfig(QtGui)
BuildRequires: pkgconfig(xcb) 
# Oh, the irony of being in the default buildroot @ rpmfusion
BuildRequires: phonon-backend-gstreamer

%global phonon_ver %(pkg-config --modversion phonon 2>/dev/null || echo 4.5.50)
%global vlc_ver %(pkg-config --modversion libvlc 2>/dev/null || echo 1.1.10)

Provides: phonon-backend%{?_isa} = %{phonon_ver}

Requires: vlc-core%{?_isa} >= %{vlc_ver} 
Requires: phonon%{?_isa} >= %{phonon_ver}
%{?_qt4:Requires: qt4%{?_isa} >= %{_qt4_version}}


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
