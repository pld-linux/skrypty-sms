Summary:	A set of scripts to send SMSes
Summary(pl.UTF-8):	Zestaw skryptów do wysyłania SMS-ów
Name:		skrypty-sms
Version:	1.86
Release:	3
License:	GPL v.2
Group:		Networking/Utilities
Source0:	http://sms.jfiok.org/pub/%{name}-%{version}.tar.gz
# Source0-md5:	27a5a8a5068fd43ef4bbea0adc5304da
URL:		http://sms.jfiok.org/
BuildRequires:	perl-base
Requires:	grep
Requires:	nc
Requires:	perl-Crypt-SSLeay
Requires:	perl-libwww
Requires:	sed
Requires:	smtpdaemon
Requires:	textutils
Requires:	wget
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a set of shell scripts that can be used for
sending SMS messages, forwarding mails to SMS, etc.

%description -l pl.UTF-8
Ten pakiet zawiera zestaw skryptów powłoki, które mogą służyć do
wysyłania komunikatów SMS, przekazywania poczty na SMS itp.

%package bramka-www
Summary:	A script helpful to create a WWW->SMS gate
Summary(pl.UTF-8):	Skrypt użyteczny do stworzenia bramki WWW->SMS
Group:		Networking/Utilities
Requires:	%{name} = %{version}-%{release}
Requires:	metamail

%description bramka-www
This script is meant as a backend for a WWW->SMS gate, should you need
to create such yourself.

%description bramka-www -l pl.UTF-8
Ten skrypt jest backendem dla bramki WWW->SMS, na wypadek potrzeby
stworzenia takowej.

%package dialog
Summary:	A console interface for sending SMSes
Summary(pl.UTF-8):	Konsolowy interfejs do wysyłania SMS-ów
Group:		Networking/Utilities
Requires:	%{name} = %{version}-%{release}
Requires:	dialog

%description dialog
The "sms-dialog" script uses the "dialog" command to create quite a
convenient (?) and functional interface for sending SMS messages.

%description dialog -l pl.UTF-8
Skrypt "sms-dialog" wykorzystuje polecenie "dialog" do stworzenia w
miarę wygodnego (?) i funkcjonalnego interfejsu do wysyłania SMS-ów.

%package nc
Summary:	A simple netcat replacement
Summary(pl.UTF-8):	Prosty zastępnik netcata
Group:		Networking/Utilities
Requires:	telnet
Provides:	nc

%description nc
This quite simple script replaces the netcat program - its only
function is sending a given character stream (received from the
standard input) to a remote server with a given name and reading the
response sending it to the standard output.

%description nc -l pl.UTF-8
Ten w sumie prosty skrypt zastępuje program znany pod nazwą netcat
(nc) - jego jedyną funkcją jest wysyłanie podanego ciągu znaków
(otrzymanego na standardowym wejściu) do zdalnego serwera o podanej
nazwie, oraz odczytanie odpowiedzi i przekazanie je na standardowe
wyjście.

%package nopl
Summary:	A MIME decoder & Polish character remover for skrypty-sms
Summary(pl.UTF-8):	Dekoder MIME i usuwaczka polskich znaków dla skrypty-sms
Group:		Networking/Utilities
Requires:	%{name} = %{version}-%{release}
Requires:	metamail

%description nopl
The "nopl" script decodes fragments of mail headers encoded in
Quoted-Printable or Base64. This means eg. converting
=?ISO-8859-1?Q?=E4u=DFer?= to "äußer". Additionally the script can
convert Polish characters into ASCII characters (ó->o etc.) However,
if we aren't bothered by Polish letters it can be turned off.

%description nopl -l pl.UTF-8
Skrypt "nopl" odkodowuje występujące w nagłówkach listu fragmenty
kodowane jako Quoted-Printable albo Base64. Oznacza to np. zamianę
=?ISO-8859-2?Q?pi=EA=E6?= na "pięć". Dodatkowo skrypt może zamieniać
polskie znaki na znaki ASCII (ą->a itp.), aczkolwiek jeżeli polskie
literki nam nie przeszkadzają, to można to wyłączyć.

%prep
%setup -qn %{name}
%{__perl} -p -i -e 's#/usr/local#%{_prefix}#g' *
%{__perl} -p -i -e 's/CURRENT=.*/CURRENT=%{version}/' check-for-update.sh

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/sms,%{_sysconfdir}}
install nopl bramka-common sms.* $RPM_BUILD_ROOT%{_datadir}/sms
install check-for-update.sh $RPM_BUILD_ROOT%{_bindir}/skrypty-sms-check-for-update
install sms-dialog extras/bramka-{mail,www} powiadom $RPM_BUILD_ROOT%{_bindir}
install nc-emulator $RPM_BUILD_ROOT%{_bindir}/nc
install smsrc $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* CHANGELOG
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/skrypty*
%attr(755,root,root) %{_bindir}/bramka-mail
%attr(755,root,root) %{_bindir}/powiadom
%dir %{_datadir}/sms
%attr(755,root,root) %{_datadir}/sms/bramka-common
%{_datadir}/sms/sms*

%files bramka-www
%defattr(644,root,root,755)
%doc extras/przyklad-bramki.html
%attr(755,root,root) %{_bindir}/bramka-www

%files dialog
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sms-dialog

%files nc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nc

%files nopl
%defattr(644,root,root,755)
%{_datadir}/sms/nopl
