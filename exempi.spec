#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x5FEE05E6A56E15A3 (hub@nit.ca)
#
Name     : exempi
Version  : 2.4.5
Release  : 13
URL      : https://libopenraw.freedesktop.org/download/exempi-2.4.5.tar.bz2
Source0  : https://libopenraw.freedesktop.org/download/exempi-2.4.5.tar.bz2
Source99 : https://libopenraw.freedesktop.org/download/exempi-2.4.5.tar.bz2.asc
Summary  : A library to parse XMP metadata
Group    : Development/Tools
License  : BSD-3-Clause-Clear
Requires: exempi-bin = %{version}-%{release}
Requires: exempi-lib = %{version}-%{release}
Requires: exempi-license = %{version}-%{release}
Requires: exempi-man = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : expat-dev
BuildRequires : pkgconfig(zlib)
Patch1: cve-2018-12648.patch

%description
exempi is a port of Adobe XMP SDK to work on UNIX and to be build with
GNU automake.

%package bin
Summary: bin components for the exempi package.
Group: Binaries
Requires: exempi-license = %{version}-%{release}

%description bin
bin components for the exempi package.


%package dev
Summary: dev components for the exempi package.
Group: Development
Requires: exempi-lib = %{version}-%{release}
Requires: exempi-bin = %{version}-%{release}
Provides: exempi-devel = %{version}-%{release}
Requires: exempi = %{version}-%{release}

%description dev
dev components for the exempi package.


%package lib
Summary: lib components for the exempi package.
Group: Libraries
Requires: exempi-license = %{version}-%{release}

%description lib
lib components for the exempi package.


%package license
Summary: license components for the exempi package.
Group: Default

%description license
license components for the exempi package.


%package man
Summary: man components for the exempi package.
Group: Default

%description man
man components for the exempi package.


%prep
%setup -q -n exempi-2.4.5
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557084418
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fcf-protection=full -ffat-lto-objects -flto=4 -fstack-protector-strong "
export FCFLAGS="$CFLAGS -O3 -fcf-protection=full -ffat-lto-objects -flto=4 -fstack-protector-strong "
export FFLAGS="$CFLAGS -O3 -fcf-protection=full -ffat-lto-objects -flto=4 -fstack-protector-strong "
export CXXFLAGS="$CXXFLAGS -O3 -fcf-protection=full -ffat-lto-objects -flto=4 -fstack-protector-strong "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1557084418
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/exempi
cp COPYING %{buildroot}/usr/share/package-licenses/exempi/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/exempi

%files dev
%defattr(-,root,root,-)
/usr/include/exempi-2.0/exempi/xmp++.hpp
/usr/include/exempi-2.0/exempi/xmp.h
/usr/include/exempi-2.0/exempi/xmpconsts.h
/usr/include/exempi-2.0/exempi/xmperrors.h
/usr/lib64/libexempi.so
/usr/lib64/pkgconfig/exempi-2.0.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libexempi.so.3
/usr/lib64/libexempi.so.3.4.5

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/exempi/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/exempi.1
