#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x2D1FB7916A52E121 (carl@carljm.me)
#
Name     : MonkeyType
Version  : 21.5.0
Release  : 49
URL      : https://files.pythonhosted.org/packages/17/89/59d5f222e88763a4dca897a1af7556f33297169c5f6db872fc64cefc3bc2/MonkeyType-21.5.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/17/89/59d5f222e88763a4dca897a1af7556f33297169c5f6db872fc64cefc3bc2/MonkeyType-21.5.0.tar.gz
Source1  : https://files.pythonhosted.org/packages/17/89/59d5f222e88763a4dca897a1af7556f33297169c5f6db872fc64cefc3bc2/MonkeyType-21.5.0.tar.gz.asc
Summary  : Generating type annotations from sampled production types
Group    : Development/Tools
License  : BSD-3-Clause
Requires: MonkeyType-bin = %{version}-%{release}
Requires: MonkeyType-license = %{version}-%{release}
Requires: MonkeyType-python = %{version}-%{release}
Requires: MonkeyType-python3 = %{version}-%{release}
Requires: libcst
Requires: mypy_extensions
Requires: retype
Requires: typed_ast
BuildRequires : buildreq-distutils3
BuildRequires : libcst
BuildRequires : mypy_extensions
BuildRequires : retype
BuildRequires : typed_ast

%description
==========
        
        MonkeyType collects runtime types of function arguments and return values, and
        can automatically generate stub files or even add draft type annotations
        directly to your Python code based on the types collected at runtime.
        
        Example
        -------

%package bin
Summary: bin components for the MonkeyType package.
Group: Binaries
Requires: MonkeyType-license = %{version}-%{release}

%description bin
bin components for the MonkeyType package.


%package license
Summary: license components for the MonkeyType package.
Group: Default

%description license
license components for the MonkeyType package.


%package python
Summary: python components for the MonkeyType package.
Group: Default
Requires: MonkeyType-python3 = %{version}-%{release}
Provides: monkeytype-python

%description python
python components for the MonkeyType package.


%package python3
Summary: python3 components for the MonkeyType package.
Group: Default
Requires: python3-core
Provides: pypi(monkeytype)
Requires: pypi(libcst)
Requires: pypi(mypy_extensions)

%description python3
python3 components for the MonkeyType package.


%prep
%setup -q -n MonkeyType-21.5.0
cd %{_builddir}/MonkeyType-21.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635753839
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/MonkeyType
cp %{_builddir}/MonkeyType-21.5.0/LICENSE %{buildroot}/usr/share/package-licenses/MonkeyType/79b9908e17ebbbf31047a17cf12b7156e19186eb
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/monkeytype

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/MonkeyType/79b9908e17ebbbf31047a17cf12b7156e19186eb

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
