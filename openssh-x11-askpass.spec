%define	_rn	x11-ssh-askpass
Summary:	OpenSSH X11 passphrase dialog
Summary(de):	OpenSSH X11 Passwort-Dialog
Summary(es):	Di�logo para introducci�n de passphrase para X11
Summary(fr):	Dialogue pass-phrase X11 d'OpenSSH
Summary(it):	Finestra di dialogo X11 per la frase segreta di OpenSSH
Summary(pl):	Odpytywacz has�a OpenSSH dla X11
Summary(pt):	Di�logo de pedido de senha para X11 do OpenSSH
Summary(pt_BR):	Di�logo para entrada de passphrase para X11
Summary(ru):	OpenSSH - ������ ����� �������� ����� (passphrase) ��� X11
Summary(uk):	OpenSSH - Ħ���� ����� ������ϧ ����� (passphrase) ��� X11
Name:		openssh-x11-askpass
Version:	1.2.4.1
Release:	3
License:	Free
Group:		Applications/Networking
Source0:	http://www.jmknoble.net/software/x11-ssh-askpass/%{_rn}-%{version}.tar.gz
# Source0-md5:	8f2e41f3f7eaa8543a2440454637f3c3
URL:		http://www.jmknoble.net/software/x11-ssh-askpass/
BuildRequires:	XFree86-devel
Requires:	openssh
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdefsdir	/usr/X11R6/lib/X11/app-defaults

%description
This is an X11-based passphrase dialog for use with OpenSSH.

%description -l es
Este paquete contiene un programa que abre una caja de di�logo para
entrada de passphrase en X11.

%description -l pl
To jest bazuj�cy na X11 odpytywacz has�a do u�ytku z OpenSSH.

%description -l pt_BR
Esse pacote cont�m um programa que abre uma caixa de di�logo para
entrada de passphrase no X11.

%description -l ru
Ssh (Secure Shell) - ��� ��������� ��� "������" (login) �� ���������
������ � ��� ���������� ������ �� ��������� ������.

���� ����� �������� ������ ����� �������� ����� ��� ������������� ���
X11.

%description -l uk
Ssh (Secure Shell) - �� �������� ��� "������" (login) �� צ������ϧ
������ �� ��� ��������� ������ �� צ�����Φ� ����Φ.

��� ����� ͦ����� Ħ���� ����� ������ϧ ����� ��� ������������ Ц�
X11.

%prep
%setup -q -n %{_rn}-%{version}

%build
xmkmf
%{__make} includes all \
	CC="%{__cc}" \
	CDEBUGFLAGS="%{rpmcflags}"

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
%{_appdefsdir}/SshAskpass
