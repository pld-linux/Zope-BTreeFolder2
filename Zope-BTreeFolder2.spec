%include	/usr/lib/rpm/macros.python
%define		zope_subname	BTreeFolder2
Summary:	BTreeFolder2 - a Zope product that acts like a Zope folder but can store many more items
Summary(pl):	BTreeFolder2 - dodatek do Zope rozszerzaj±cy mo¿liwo¶ci pracy na folderach
Name:		Zope-%{zope_subname}
Version:	0.5.0
Release:	1
License:	GNU
Group:		Development/Tools
Source0:	http://hathaway.freezope.org/Software/%{zope_subname}/%{zope_subname}-%{version}.tar.gz
# Source0-md5:	f301851803326d774d438b35aeb2322d
URL:		http://hathaway.freezope.org/Software/BTreeFolder2/
%pyrequires_eq	python-modules
Requires:	Zope
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	product_dir	/usr/lib/zope/Products

%description
BTreeFolder2 is a Zope product that acts like a Zope folder but can
store many more items.

%description -l pl
BTreeFolder2 jest dodatkiem do Zope rozszerzaj±cym mo¿liwo¶ci pracy na
folderach

%prep
%setup -q -c %{zope_subname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{product_dir}
cp -af * $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

%py_comp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}
%py_ocomp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;
rm -rf $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}/*.txt

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%files
%defattr(644,root,root,755)
%doc %{zope_subname}/*.txt
%{product_dir}/%{zope_subname}
