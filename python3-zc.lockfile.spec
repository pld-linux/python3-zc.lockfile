#
# Conditional build:
%bcond_without	tests	# unit tests

%define		module		zc.lockfile
Summary:	Basic inter-process locks
Summary(pl.UTF-8):	Podstawowe blokady pomiędzy procesami 
Name:		python3-%{module}
Version:	3.0.post1
Release:	1
License:	ZPL v2.1
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/zc.lockfile/
Source0:	https://files.pythonhosted.org/packages/source/z/zc.lockfile/%{module}-%{version}.tar.gz
# Source0-md5:	5e902492de505a0f98e49b1e31cf2bc2
URL:		https://pypi.org/project/zc.lockfile
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-zope.testing
BuildRequires:	python3-zope.testrunner
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.7
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

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd)/src \
zope-testrunner-3 --test-path=src -v
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst COPYRIGHT.txt README.rst
%dir %{py3_sitescriptdir}/zc
%{py3_sitescriptdir}/zc/lockfile
%{py3_sitescriptdir}/zc.lockfile-%{version}-py*.egg-info
%{py3_sitescriptdir}/zc.lockfile-%{version}-py*-nspkg.pth
