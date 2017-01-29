Summary:	Library for easy parsing of XMP metadata
Name:		exempi
Version:	2.4.0
Release:	1%{?dist}
License:	BSD
Group:		System Environment/Libraries
URL:		http://libopenraw.freedesktop.org/wiki/Exempi
Source0:	http://libopenraw.freedesktop.org/download/%{name}-%{version}.tar.bz2
BuildRequires:	boost-devel expat-devel zlib-devel pkgconfig
# Work around for aarch64 support (https://bugzilla.redhat.com/show_bug.cgi?id=925327)
BuildRequires:	autoconf automake libtool
Provides:	bundled(md5-polstra)

%description
Exempi provides a library for easy parsing of XMP metadata. It is a port of 
Adobe XMP SDK to work on UNIX and to be build with GNU automake.
It includes XMPCore and XMPFiles.

%package devel
Summary:	Headers for developing programs that will use %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig

%description devel
This package contains the libraries and header files needed for
developing with exempi.

%prep
%setup -q

%build
libtoolize -vi
./autogen.sh
# BanEntityUsage needed for #888765
%configure CPPFLAGS="-I%{_includedir} -fno-strict-aliasing -DBanAllEntityUsage=1"

# Disable rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags} V=1

%check
make check

%install
make DESTDIR=%{buildroot} install

rm -rf %{buildroot}%{_libdir}/*.la
rm -rf %{buildroot}%{_libdir}/*.a

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/exempi
%{_libdir}/*.so.*
%{_mandir}/man1/exempi.1.gz

%files devel
%{_includedir}/exempi-2.0/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Sat Jan 07 2017 Hubert Figuière <hub@figuiere.net> - 2.4.0-1
- Update to version 2.4.0

* Thu Mar 17 2016 Nikola Forró <nforro@redhat.com> - 2.3.0-1
- Update to version 2.3.0
  Resolves #1318279

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 2.2.1-14
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 2.2.1-13
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 2.2.1-11
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.2.1-9
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 2.2.1-8
- Rebuild for boost 1.57.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Petr Machata <pmachata@redhat.com> - 2.2.1-5
- Rebuild for boost 1.55.0

* Fri Jan 10 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.1-4
- Run libtoolize before autogen.sh
- Resolves: rhbz#1051186

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 2.2.1-2
- Rebuild for boost 1.54.0

* Mon Jul 22 2013 Deji Akingunola <dakingun@gmail.com> - 2.2.1-1
- Update to version 2.2.1

* Wed Jan 30 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.0-6
- Get rid of unnecessary LDFLAGS definition overwriting RPM flags

* Wed Jan 02 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.0-5
- Make sure we respect RPM_OPT_FLAGS and simplify configure (#889554)

* Wed Dec 19 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.0-4
- Add BanAllEntityUsage into macro definitions (#888765)

* Thu Aug 16 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.0-3
- Add bundled(md5-polstra) provides
- Update to current guidelines

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 22 2012 Deji Akingunola <dakingun@gmail.com> - 2.2.0-1
- Update to version 2.2.0

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon May  3 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.1.1-1
- Update to 2.1.1
- Add testsuite execution
- Removed build patch for gcc-4.4 (fixed in upstream)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 04 2009 Deji Akingunola <dakingun@gmail.com> - 2.1.0-2
- Add patch to build with gcc-4.4

* Tue Jan 06 2009 Deji Akingunola <dakingun@gmail.com> - 2.1.0-1
- Update to 2.1.0
    
* Sat May 17 2008 Deji Akingunola <dakingun@gmail.com> - 2.0.1-1
- Update to 2.0.1

* Wed Apr 02 2008 Deji Akingunola <dakingun@gmail.com> - 2.0.0-1
- Update to 2.0.0

* Fri Feb 08 2008 Deji Akingunola <dakingun@gmail.com> - 1.99.9-1
- Update to 1.99.9

* Sun Jan 13 2008 Deji Akingunola <dakingun@gmail.com> - 1.99.7-1
- Update to 1.99.7

* Mon Dec 03 2007 Deji Akingunola <dakingun@gmail.com> - 1.99.5-1
- Update to 1.99.5

* Wed Sep 05 2007 Deji Akingunola <dakingun@gmail.com> - 1.99.4-2
- Rebuild for expat 2.0

* Wed Aug 22 2007 Deji Akingunola <dakingun@gmail.com> - 1.99.4-1
- Update tp 1.99.4

* Tue Jul 10 2007 Deji Akingunola <dakingun@gmail.com> - 1.99.3-1
- Initial packaging for Fedora
