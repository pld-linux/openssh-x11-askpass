%define	_rn	x11-ssh-askpass
Summary:	OpenSSH X11 passphrase dialog
Summary(pl):	Odpytywacz has³a OpenSSH dla X11
Name:		openssh-x11-askpass
Version:	1.2.4.1
Release:	1
License:	Free
Group:		Applications/Networking
Source0:	http://www.pobox.com/~jmknoble/software/x11-ssh-askpass/%{_rn}-%{version}.tar.gz
URL:		http://www.pobox.com/~jmknoble/software/x11-ssh-askpass/
BuildRequires:	XFree86-devel
Requires:	openssh
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
This is an X11-based passphrase dialog for use with OpenSSH.

%description -l pl
To jest bazuj±cy na X11 odpytywacz has³a do u¿ytku z OpenSSH.

%prep
%setup -q -n %{_rn}-%{version}

%build
xmkmf
CXXEXTRA_DEFINES="%{rpmcflags}" %{__make} includes all

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_libdir}/X11/app-defaults/SshAskpass
