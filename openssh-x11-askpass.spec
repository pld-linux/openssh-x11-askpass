%define	_rn	x11-ssh-askpass
Summary:	OpenSSH X11 passphrase dialog
Summary(de):	OpenSSH X11 Passwort-Dialog
Summary(es):	DiАlogo para introducciСn de passphrase para X11
Summary(fr):	Dialogue pass-phrase X11 d'OpenSSH
Summary(it):	Finestra di dialogo X11 per la frase segreta di OpenSSH
Summary(pl):	Odpytywacz hasЁa OpenSSH dla X11
Summary(pt):	DiАlogo de pedido de senha para X11 do OpenSSH
Summary(pt_BR):	DiАlogo para entrada de passphrase para X11
Summary(ru):	OpenSSH - диалог ввода ключевой фразы (passphrase) для X11
Summary(uk):	OpenSSH - д╕алог вводу ключово╖ фрази (passphrase) для X11
Name:		openssh-x11-askpass
Version:	1.2.4.1
Release:	2
License:	Free
Group:		Applications/Networking
Source0:	http://www.pobox.com/~jmknoble/software/x11-ssh-askpass/%{_rn}-%{version}.tar.gz
# Source0-md5:	b83a9f5f6c63ef32054178b19b142a5c
URL:		http://www.pobox.com/~jmknoble/software/x11-ssh-askpass/
BuildRequires:	XFree86-devel
Requires:	openssh
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
This is an X11-based passphrase dialog for use with OpenSSH.

%description -l es
Este paquete contiene un programa que abre una caja de diАlogo para
entrada de passphrase en X11.

%description -l pl
To jest bazuj╠cy na X11 odpytywacz hasЁa do u©ytku z OpenSSH.

%description -l pt_BR
Esse pacote contИm um programa que abre uma caixa de diАlogo para
entrada de passphrase no X11.

%description -l ru
Ssh (Secure Shell) - это программа для "захода" (login) на удаленную
машину и для выполнения команд на удаленной машине.

Этот пакет содержит диалог ввода ключевой фразы для использования под
X11.

%description -l uk
Ssh (Secure Shell) - це програма для "заходу" (login) до в╕ддалено╖
машини та для виконання команд на в╕ддален╕й машин╕.

Цей пакет м╕стить д╕алог вводу ключово╖ фрази для використання п╕д
X11.

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
