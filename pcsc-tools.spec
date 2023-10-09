#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
# Source0 file verified with key 0x78A1B4DFE8F9C57E (ludovic.rousseau@free.fr)
#
Name     : pcsc-tools
Version  : 1.7.0
Release  : 6
URL      : https://pcsc-tools.apdu.fr/pcsc-tools-1.7.0.tar.bz2
Source0  : https://pcsc-tools.apdu.fr/pcsc-tools-1.7.0.tar.bz2
Source1  : https://pcsc-tools.apdu.fr/pcsc-tools-1.7.0.tar.bz2.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: pcsc-tools-bin = %{version}-%{release}
Requires: pcsc-tools-data = %{version}-%{release}
Requires: pcsc-tools-license = %{version}-%{release}
Requires: pcsc-tools-locales = %{version}-%{release}
Requires: pcsc-tools-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : pkgconfig(libpcsclite)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Some tools to be used with smart cards and PC/SC
================================================

%package bin
Summary: bin components for the pcsc-tools package.
Group: Binaries
Requires: pcsc-tools-data = %{version}-%{release}
Requires: pcsc-tools-license = %{version}-%{release}

%description bin
bin components for the pcsc-tools package.


%package data
Summary: data components for the pcsc-tools package.
Group: Data

%description data
data components for the pcsc-tools package.


%package license
Summary: license components for the pcsc-tools package.
Group: Default

%description license
license components for the pcsc-tools package.


%package locales
Summary: locales components for the pcsc-tools package.
Group: Default

%description locales
locales components for the pcsc-tools package.


%package man
Summary: man components for the pcsc-tools package.
Group: Default

%description man
man components for the pcsc-tools package.


%prep
%setup -q -n pcsc-tools-1.7.0
cd %{_builddir}/pcsc-tools-1.7.0
pushd ..
cp -a pcsc-tools-1.7.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1696862553
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1696862553
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pcsc-tools
cp %{_builddir}/pcsc-tools-%{version}/LICENCE %{buildroot}/usr/share/package-licenses/pcsc-tools/dfac199a7539a404407098a2541b9482279f690d || :
pushd ../buildavx2/
%make_install_v3
popd
%make_install
%find_lang pcsc-tools
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/pcsc_scan
/usr/bin/ATR_analysis
/usr/bin/gscriptor
/usr/bin/pcsc_scan
/usr/bin/scriptor

%files data
%defattr(-,root,root,-)
/usr/share/applications/gscriptor.desktop
/usr/share/pcsc/gscriptor.png
/usr/share/pcsc/smartcard_list.txt

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pcsc-tools/dfac199a7539a404407098a2541b9482279f690d

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/ATR_analysis.1p
/usr/share/man/man1/gscriptor.1p
/usr/share/man/man1/pcsc_scan.1
/usr/share/man/man1/scriptor.1p

%files locales -f pcsc-tools.lang
%defattr(-,root,root,-)

