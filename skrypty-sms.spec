Summary:	A set of scripts to send SMSes
Summary(pl):	Zestaw skryptów do wysy³ania SMSów
Name:		skrypty-sms
Version:	1.62
Release:	4
License:	non-commercial
Group:		Networking/Utilities
Source0:	http://sms.jfiok.org/pub/%{name}.tar.gz
# Source0-md5:	76acd4a51cc5be2e42131d95d5cf23e4
URL:		http://sms.jfiok.org/
Requires:	textutils
Requires:	wget
Requires:	grep
Requires:	nc
Requires:	sed
Requires:	smtpdaemon
BuildRequires:	perl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a set of shell scripts that can be used for
sending SMS messages, forwarding mails to SMS, etc.

%description -l pl
Ten pakiet zawiera zestaw skryptów pow³oki, które mog± byæ u¿yte do
wysy³ania komunikatów SMS, przekazywania poczty na SMS, etc.

%package bramka-www
Summary:	A script helpful to create a WWW->SMS gate
Summary(pl):	Skrypt u¿yteczny do stworzenia bramki WWW->SMS
Group:		Networking/Utilities
Requires:	%{name} = %{version}
Requires:	metamail

%description bramka-www
This script is meant as a backend for a WWW->SMS gate, should you need
to create such yourself.

%description bramka-www -l pl
Ten skrypt jest backendem dla bramki WWW->SMS, na wypadek potrzeby
stworzenia takowej.

%package dialog
Summary:	A console interface for sending SMSes
Summary(pl):	Konsolowy interfejs do wysy³ania SMSów
Group:		Networking/Utilities
Requires:	%{name} = %{version}
Requires:	dialog

%description dialog
The "sms-dialog" script uses the "dialog" command to create quite a
convenient (?) and functional interface for sending SMS messages.

%description dialog -l pl
Skrypt "sms-dialog" wykorzystuje polecenie "dialog" do stworzenia w
miarê wygodnego (?) i funkcjonalnego interfejsu do wysy³ania SMSów.

%package nc
Summary:	A simple netcat replacement
Summary(pl):	Prosty zastêpnik netcata
Group:		Networking/Utilities
Provides:	nc
Requires:	telnet

%description nc
This quite simple script replaces the netcat program -- its only
function is sending a given character stream (received from the
standard input) to a remote server with a given name and reading the
response sending it to the standard output.

%description nc -l pl
Ten w sumie prosty skrypt zastêpuje program znany pod nazw± netcat
(nc) -- jego jedyn± funkcj± jest wysy³anie danego ci±gu znaków
(otrzymanego na standardowym wej¶ciu) do zdalnego serwera o podanej
nazwie, oraz odczytanie odpowiedzi i przekazanie je na standardowe
wyj¶cie.

%package nopl
Summary:	A MIME decoder & Polish character remover for skrypty-sms
Summary(pl):	Dekoder MIME i usuwaczka polskich znaków dla skrypty-sms
Requires:	%{name} = %{version}
Requires:	metamail
Group:		Networking/Utilities

%description nopl
The "nopl" script decodes fragments of mail headers encoded in
Quoted-Printable or Base64. This means e.g. converting
=?ISO-8859-1?Q?=E4u=DFer?= to "äußer". Additionally the script can
convert Polish characters into ASCII character (ó->o etc.) However, if
we aren't bothered by Polish letters it can be turned off.

%description nopl -l pl
Skrypt "nopl" odkodowuje wystêpuj±ce w nag³ówkach listu fragmenty
kodowane jako Quoted-Printable albo Base64 . Oznacza to np. zamianê
=?ISO-8859-2?Q?pi=EA=E6?= na "piêæ". Dodatkowo skrypt mo¿e zamieniaæ
polskie znaki na znaki ascii (±->a itp.), aczkolwiek je¿eli polskie
literki nam nie przeszkadzaj±, to mo¿na to wy³±czyæ.

%prep
%setup -qn %{name}
perl -p -i -e 's#/usr/local#%{_prefix}#g' *
perl -p -i -e 's/CURRENT=.*/CURRENT=%{version}/' check-for-update.sh

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/sms,%{_sysconfdir}}
install nopl bramka-common sms.* $RPM_BUILD_ROOT%{_datadir}/sms
install check-for-update.sh $RPM_BUILD_ROOT%{_bindir}/skrypty-sms-check-for-update
install sms-dialog nc bramka-{mail,www} powiadom $RPM_BUILD_ROOT%{_bindir}
install smsrc $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* CHANGELOG *.html
%config %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/skrypty*
%attr(755,root,root) %{_bindir}/bramka-mail
%attr(755,root,root) %{_bindir}/powiadom
%dir %{_datadir}/sms
%{_datadir}/sms/bramka-common
%{_datadir}/sms/sms*

%files bramka-www
%defattr(644,root,root,755)
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
