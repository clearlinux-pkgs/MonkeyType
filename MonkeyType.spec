#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x2D1FB7916A52E121 (carl@carljm.me)
#
Name     : MonkeyType
Version  : 20.4.1
Release  : 37
URL      : https://files.pythonhosted.org/packages/0c/17/95ea27b4ca17daf4c049bd87fa5ba720a621f3a875351e5175abe167aeda/MonkeyType-20.4.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/0c/17/95ea27b4ca17daf4c049bd87fa5ba720a621f3a875351e5175abe167aeda/MonkeyType-20.4.1.tar.gz
Source1  : https://files.pythonhosted.org/packages/0c/17/95ea27b4ca17daf4c049bd87fa5ba720a621f3a875351e5175abe167aeda/MonkeyType-20.4.1.tar.gz.asc
Summary  : Generating type annotations from sampled production types
Group    : Development/Tools
License  : BSD-3-Clause
Requires: MonkeyType-bin = %{version}-%{release}
Requires: MonkeyType-python = %{version}-%{release}
Requires: MonkeyType-python3 = %{version}-%{release}
Requires: mypy_extensions
Requires: retype
Requires: typed_ast
BuildRequires : buildreq-distutils3
BuildRequires : mypy_extensions
BuildRequires : retype
BuildRequires : typed_ast

%description
MonkeyType
==========
MonkeyType collects runtime types of function arguments and return values, and
can automatically generate stub files or even add draft type annotations
directly to your Python code based on the types collected at runtime.

%package bin
Summary: bin components for the MonkeyType package.
Group: Binaries

%description bin
bin components for the MonkeyType package.


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
Requires: pypi(mypy_extensions)

%description python3
python3 components for the MonkeyType package.


%prep
%setup -q -n MonkeyType-20.4.1
cd %{_builddir}/MonkeyType-20.4.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1585957129
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/monkeytype

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
