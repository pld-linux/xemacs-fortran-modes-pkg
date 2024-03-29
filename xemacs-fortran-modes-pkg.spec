%define 	srcname	fortran-modes
Summary:	XEmacs modes for Fortran programming language
Summary(pl.UTF-8):	XEmacsowe tryby do języka programowania Fortran
Name:		xemacs-%{srcname}-pkg
Version:	1.05
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	http://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
# Source0-md5:	2c2545602482660ad0d811b0574a3eed
URL:		http://www.xemacs.org/
Requires:	xemacs
Requires:	xemacs-base-pkg
Requires:	xemacs-devel-pkg
Requires:	xemacs-mail-lib-pkg
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XEmacs modes for Fortran programming language (Fortran 77 and 90
standards), moved from xemacs-prog-modes package.

%description -l pl.UTF-8
XEmacsowe tryby do języka programowania Fortran (w standardach Fortran
77 i 90), wyjęte z pakietu xemacs-prog-modes.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/fortran-modes/ChangeLog
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.el*
