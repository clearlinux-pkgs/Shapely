#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Shapely
Version  : 1.6.4.post2
Release  : 1
URL      : https://files.pythonhosted.org/packages/a2/fb/7a7af9ef7a35d16fa23b127abee272cfc483ca89029b73e92e93cdf36e6b/Shapely-1.6.4.post2.tar.gz
Source0  : https://files.pythonhosted.org/packages/a2/fb/7a7af9ef7a35d16fa23b127abee272cfc483ca89029b73e92e93cdf36e6b/Shapely-1.6.4.post2.tar.gz
Summary  : Geometric objects, predicates, and operations
Group    : Development/Tools
License  : BSD-3-Clause
Requires: Shapely-license = %{version}-%{release}
Requires: Shapely-python = %{version}-%{release}
Requires: Shapely-python3 = %{version}-%{release}
Requires: numpy
Requires: pytest
Requires: pytest-cov
BuildRequires : buildreq-distutils3
BuildRequires : geos-dev

%description
Shapely
        =======

%package license
Summary: license components for the Shapely package.
Group: Default

%description license
license components for the Shapely package.


%package python
Summary: python components for the Shapely package.
Group: Default
Requires: Shapely-python3 = %{version}-%{release}
Provides: shapely-python

%description python
python components for the Shapely package.


%package python3
Summary: python3 components for the Shapely package.
Group: Default
Requires: python3-core

%description python3
python3 components for the Shapely package.


%prep
%setup -q -n Shapely-1.6.4.post2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1548354170
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Shapely
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/Shapely/LICENSE.txt
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Shapely/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
