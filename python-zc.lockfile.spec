# TODO:
# - fix tests - zope.testing upgrade needed ?

%bcond_with	doc	# don't build doc
%bcond_with	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		zc.lockfile
%define		egg_name	zc.lockfile
%define		pypi_name	zc.lockfile
Summary:	Basic inter-process locks
Summary(pl.UTF-8):	Podstawowe blokady pomiędzy procesami 
Name:		python-%{pypi_name}
Version:	1.2.1
Release:	1
License:	ZPL 2.1
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/z/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	163f0293d53a84f608f9008d9c0afc60
URL:		https://pypi.python.org/pypi/%{pypi_name}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
BuildRequires:	python-zope.exceptions
BuildRequires:	python-zope.testing
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
BuildRequires:	python3-zope.exceptions
BuildRequires:	python3-zope.testing

%endif
# when using /usr/bin/env or other in-place substitutions
#BuildRequires:        sed >= 4.0
# replace with other requires if defined in setup.py
Requires:	python-modules
Requires:	python-zope.exceptions
Requires:	python-zope.testing
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl.UTF-8

%package -n python3-%{pypi_name}
Summary:	-
Summary(pl.UTF-8):	-
Group:		Libraries/Python
Requires:	python3-modules
Requires:	python3-zope.exceptions
Requires:	python3-zope.testing

%description -n python3-%{pypi_name}

%description -n python3-%{pypi_name} -l pl.UTF-8

%package apidocs
Summary:	API documentation for Python %{module} module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona %{module}
Group:		Documentation

%description apidocs
API documentation for Pythona %{module} module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona %{module}.

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
cd docs
%{__make} -j1 html
rm -rf _build/html/_sources
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

# when files are installed in other way that standard 'setup.py
# they need to be (re-)compiled
# change %{py_sitedir} to %{py_sitescriptdir} for 'noarch' packages!
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

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
%doc CHANGES.txt doc.txt README.txt
%dir %{py_sitescriptdir}/zc
%{py_sitescriptdir}/zc/lockfile
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%{py_sitescriptdir}/*.pth
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%defattr(644,root,root,755)
%doc CHANGES.txt doc.txt README.txt
%dir %{py3_sitescriptdir}/zc
%{py3_sitescriptdir}/zc/lockfile
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%{py3_sitescriptdir}/*.pth
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/*
%endif
