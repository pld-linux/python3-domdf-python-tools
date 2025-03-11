#
# Conditional build:
%bcond_with	tests	# unit tests (some files missing in sdist)

Summary:	Helpful functions for Python
Summary(pl.UTF-8):	Przydatne funkcje dla Pythona
Name:		python3-domdf-python-tools
Version:	3.9.0
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/domdf-python-tools/
Source0:	https://files.pythonhosted.org/packages/source/d/domdf-python-tools/domdf_python_tools-%{version}.tar.gz
# Source0-md5:	ab1984c8d939bf907a2ff0651b5b1944
URL:		https://pypi.org/project/domdf-python-tools/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools >= 1:40.6.0
%if %{with tests}
BuildRequires:	python3-click
BuildRequires:	python3-coincidence
BuildRequires:	python3-faker
%if "%{_ver_lt '%{py3_ver}' '3.9'}" == "1"
BuildRequires:	python3-importlib_metadata >= 3.6.0
%endif
%if "%{_ver_lt '%{py3_ver}' '3.7'}" == "1"
BuildRequires:	python3-importlib_resources >= 3.0.0
%endif
BuildRequires:	python3-natsort >= 7.0.1
BuildRequires:	python3-pytest
%if "%{_ver_lt '%{py3_ver}' '3.8'}" == "1"
BuildRequires:	python3-typing-extensions >= 3.7.4.1
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.749
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Helpful functions for Python.

%description -l pl.UTF-8
Przydatne funkcje dla Pythona.

%prep
%setup -q -n domdf_python_tools-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd) \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/domdf_python_tools
%{py3_sitescriptdir}/domdf_python_tools-%{version}-py*.egg-info
