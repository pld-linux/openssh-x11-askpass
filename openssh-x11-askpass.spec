%define	_rn	x11-ssh-askpass
Summary:	OpenSSH X11 passphrase dialog
Summary(pl):	Odpytywacz has³a OpenSSH dla X11
Name:		openssh-x11-askpass
Version:	1.0
Release:	1
Copyright:	free
Group:		Applications/Networking
Group(pl):	Aplikacje/Sieciowe
Source:		http://www.pobox.com/~jmknoble/software/x11-ssh-askpass/%{_rn}-%{version}.tar.gz
BuildRequires:	XFree86-devel
URL:		http://www.pobox.com/~jmknoble/software/x11-ssh-askpass/
Requires:	openssh
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr/X11R6

%description
This is an X11-based passphrase dialog for use with OpenSSH. 

%description -l pl
To jest bazuj±cy na X11 odpytywacz has³a do u¿ytku z OpenSSH.

%prep 
%setup -q -n %{_rn}-%{version}

%build
LDFLAGS="-s"; export LDFLAGS
%{_bindir}/xmkmf
CXXEXTRA_DEFINES="$RPM_OPT_FLAGS" make includes all

%install
rm -rf $RPM_BUILD_ROOT

make install \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir}

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/*
/etc/X11/app-defaults/SshAskpass
