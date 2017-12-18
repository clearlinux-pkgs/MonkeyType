#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x2D1FB7916A52E121 (carl@carljm.me)
#
Name     : MonkeyType
Version  : 17.12.2
Release  : 3
URL      : https://pypi.python.org/packages/cc/97/f5d2957fa234b505bd0e07be250def66c0724032dc9f28aa0a79bd7ce8fa/MonkeyType-17.12.2.tar.gz
Source0  : https://pypi.python.org/packages/cc/97/f5d2957fa234b505bd0e07be250def66c0724032dc9f28aa0a79bd7ce8fa/MonkeyType-17.12.2.tar.gz
Source99 : https://pypi.python.org/packages/cc/97/f5d2957fa234b505bd0e07be250def66c0724032dc9f28aa0a79bd7ce8fa/MonkeyType-17.12.2.tar.gz.asc
Summary  : Generating type annotations from sampled production types
Group    : Development/Tools
License  : BSD-3-Clause
Requires: MonkeyType-bin
Requires: MonkeyType-python3
Requires: MonkeyType-python
Requires: retype
Requires: typed-ast
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : retype
BuildRequires : setuptools
BuildRequires : typed-ast

%description
==========
        
        MonkeyType collects runtime types of function arguments and return values, and
        can automatically generate stub files or even add draft type annotations
        directly to your Python code based on the types collected at runtime.
        
        Examples
        --------
        
        Run a script under call-trace logging of functions and methods in all imported

%package bin
Summary: bin components for the MonkeyType package.
Group: Binaries

%description bin
bin components for the MonkeyType package.


%package python
Summary: python components for the MonkeyType package.
Group: Default
Requires: MonkeyType-python3
Provides: monkeytype-python

%description python
python components for the MonkeyType package.


%package python3
Summary: python3 components for the MonkeyType package.
Group: Default
Requires: python3-core

%description python3
python3 components for the MonkeyType package.


%prep
%setup -q -n MonkeyType-17.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1513615810
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
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
