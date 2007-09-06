%define	_rn	x11-ssh-askpass
Summary:	OpenSSH X11 passphrase dialog
Summary(de.UTF-8):	OpenSSH X11 Passwort-Dialog
Summary(es.UTF-8):	Diálogo para introducción de passphrase para X11
Summary(fr.UTF-8):	Dialogue pass-phrase X11 d'OpenSSH
Summary(it.UTF-8):	Finestra di dialogo X11 per la frase segreta di OpenSSH
Summary(pl.UTF-8):	Odpytywacz hasła OpenSSH dla X11
Summary(pt.UTF-8):	Diálogo de pedido de senha para X11 do OpenSSH
Summary(pt_BR.UTF-8):	Diálogo para entrada de passphrase para X11
Summary(ru.UTF-8):	OpenSSH - диалог ввода ключевой фразы (passphrase) для X11
Summary(uk.UTF-8):	OpenSSH - діалог вводу ключової фрази (passphrase) для X11
Name:		openssh-x11-askpass
Version:	1.2.4.1
Release:	6
License:	Free
Group:		Applications/Networking
Source0:	http://www.jmknoble.net/software/x11-ssh-askpass/%{_rn}-%{version}.tar.gz
# Source0-md5:	8f2e41f3f7eaa8543a2440454637f3c3
URL:		http://www.jmknoble.net/software/x11-ssh-askpass/
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-proto-xproto-devel
Requires:	openssh
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdefsdir	%{_datadir}/X11/app-defaults

%description
This is an X11-based passphrase dialog for use with OpenSSH.

%description -l es.UTF-8
Este paquete contiene un programa que abre una caja de diálogo para
entrada de passphrase en X11.

%description -l pl.UTF-8
To jest bazujący na X11 odpytywacz hasła do użytku z OpenSSH.

%description -l pt_BR.UTF-8
Esse pacote contém um programa que abre uma caixa de diálogo para
entrada de passphrase no X11.

%description -l ru.UTF-8
Ssh (Secure Shell) - это программа для "захода" (login) на удаленную
машину и для выполнения команд на удаленной машине.

Этот пакет содержит диалог ввода ключевой фразы для использования под
X11.

%description -l uk.UTF-8
Ssh (Secure Shell) - це програма для "заходу" (login) до віддаленої
машини та для виконання команд на віддаленій машині.

Цей пакет містить діалог вводу ключової фрази для використання під
X11.

%prep
%setup -q -n %{_rn}-%{version}
rm -f Imakefile

%build
./configure \
	--libexecdir=%{_bindir} \
	--mandir=%{_mandir} \
	--with-app-defaults-dir=%{_appdefsdir}
xmkmf

%{__make} includes all \
	CC="%{__cc}" \
	CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_appdefsdir}/SshAskpass
