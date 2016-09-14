#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : exempi
Version  : 2.3.0
Release  : 1
URL      : https://libopenraw.freedesktop.org/download/exempi-2.3.0.tar.bz2
Source0  : https://libopenraw.freedesktop.org/download/exempi-2.3.0.tar.bz2
Summary  : Library for easy parsing of XMP metadata.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: exempi-bin
Requires: exempi-lib
Requires: exempi-doc
BuildRequires : boost-dev
BuildRequires : expat-dev
BuildRequires : valgrind

%description
exempi is a port of Adobe XMP SDK to work on UNIX and to be build with
GNU automake.

%package bin
Summary: bin components for the exempi package.
Group: Binaries

%description bin
bin components for the exempi package.


%package dev
Summary: dev components for the exempi package.
Group: Development
Requires: exempi-lib
Requires: exempi-bin
Provides: exempi-devel

%description dev
dev components for the exempi package.


%package doc
Summary: doc components for the exempi package.
Group: Documentation

%description doc
doc components for the exempi package.


%package lib
Summary: lib components for the exempi package.
Group: Libraries

%description lib
lib components for the exempi package.


%prep
%setup -q -n exempi-2.3.0

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
rm -rf %{buildroot}
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
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
