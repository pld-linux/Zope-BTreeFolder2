%define		zope_subname	BTreeFolder2
Summary:	Zope product that acts like a Zope folder but can store many more items
Summary(pl.UTF-8):   Dodatek do Zope rozszerzający możliwości pracy na folderach
Name:		Zope-%{zope_subname}
Version:	1.0.2
Release:	1
License:	ZPL 2.0
Group:		Development/Tools
Source0:	http://plone.org/Members/tiran/BTreeFolder2-%{version}.tar.gz
# Source0-md5:	ff9ac5d485ca2a9d4f65e85509c88f2e
URL:		http://hathawaymix.org/Software/BTreeFolder2/
BuildRequires:	python
BuildRequires:	rpmbuild(macros) >= 1.268
%pyrequires_eq	python-modules
Requires(post,postun):	/usr/sbin/installzopeproduct
Requires:	Zope
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BTreeFolder2 is a Zope product that acts like a Zope folder but can
store many more items.

%description -l pl.UTF-8
BTreeFolder2 jest dodatkiem do Zope rozszerzającym możliwości pracy na
folderach.

%prep
%setup -q -n %{zope_subname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -af tests *.py *.dtml *.gif version.txt $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
%service -q zope restart

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	%service -q zope restart
fi

%files
%defattr(644,root,root,755)
%doc README.txt CHANGES.txt
%{_datadir}/%{name}
