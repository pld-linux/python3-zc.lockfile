#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		zc.lockfile
Summary:	Basic inter-process locks
Summary(pl.UTF-8):	Podstawowe blokady pomiędzy procesami 
Name:		python-%{module}
# keep 2.x here for python2 support
Version:	2.0
Release:	1
License:	ZPL v2.1
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/zc.lockfile/
Source0:	https://files.pythonhosted.org/packages/source/z/zc.lockfile/%{module}-%{version}.tar.gz
# Source0-md5:	3895445752278ddcc4578658c3c9a492
URL:		https://pypi.org/project/zc.lockfile
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-mock
BuildRequires:	python-zope.testing
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-zope.testing
%endif
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The zc.lockfile package provides a basic portable implementation of
interprocess locks using lock files. The purpose if not specifically
to lock files, but to simply provide locks with an implementation
based on file-locking primitives. Of course, these locks could be
used to mediate access to other files. For example, the ZODB file
storage implementation uses file locks to mediate access to
file-storage database files. The database files and lock file files
are separate files.

%description -l pl.UTF-8
Pakiet zc.lockfile zapewnia podstawową, przenośną implementację
blokad międzyprocesowych przy użyciu plików blokad. Celem nie jest
samo blokowanie plików, ale po prostu zapewnienie blokad z
implementacją opartą na blokowaniu plików. Oczywiście te blokady mogą
służyć do negocjowania dostępu do innych plików. Na przykład
implementacja przechowywania danych w plikach ZODB wykorzystuje
blokady plikowe do negocjowania dostępu do plików baz danych. Pliki
baz danych i pliki blokad to osobne pliki.

%package -n python3-%{module}
Summary:	Basic inter-process locks
Summary(pl.UTF-8):	Podstawowe blokady pomiędzy procesami 
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-%{module}
The zc.lockfile package provides a basic portable implementation of
interprocess locks using lock files. The purpose if not specifically
to lock files, but to simply provide locks with an implementation
based on file-locking primitives. Of course, these locks could be
used to mediate access to other files. For example, the ZODB file
storage implementation uses file locks to mediate access to
file-storage database files. The database files and lock file files
are separate files.

%description -n python3-%{module} -l pl.UTF-8
Pakiet zc.lockfile zapewnia podstawową, przenośną implementację
blokad międzyprocesowych przy użyciu plików blokad. Celem nie jest
samo blokowanie plików, ale po prostu zapewnienie blokad z
implementacją opartą na blokowaniu plików. Oczywiście te blokady mogą
służyć do negocjowania dostępu do innych plików. Na przykład
implementacja przechowywania danych w plikach ZODB wykorzystuje
blokady plikowe do negocjowania dostępu do plików baz danych. Pliki
baz danych i pliki blokad to osobne pliki.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.rst COPYRIGHT.txt README.rst
%dir %{py_sitescriptdir}/zc
%{py_sitescriptdir}/zc/lockfile
%{py_sitescriptdir}/zc.lockfile-%{version}-py*.egg-info
%{py_sitescriptdir}/zc.lockfile-%{version}-py*-nspkg.pth
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGES.rst COPYRIGHT.txt README.rst
%dir %{py3_sitescriptdir}/zc
%{py3_sitescriptdir}/zc/lockfile
%{py3_sitescriptdir}/zc.lockfile-%{version}-py*.egg-info
%{py3_sitescriptdir}/zc.lockfile-%{version}-py*-nspkg.pth
%endif
