Summary:	Monopoly - a program for counting ppp (but not only) connections
Summary(pl):	Monopoly program zliczaj±cy po³±czenia ppp (ale nie tylko)
Name:		monopoly
Version:	1.6.5
Release:	2
License:	GPL
Group:		Applications/Networking
Source0:	http://dione.ids.pl/~yossa/monopoly/%{name}-%{version}.tar.gz
URL:		http://dione.ids.pl/~yossa/monopoly/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	slang-devel >= 1.0
BuildRequires:	zlib-devel
Requires:	ppp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc

%description
Monopoly - a program for counting ppp (but not only) connections. It
uses system logs to create its own log file. It can be used from
command line to show daily, monthly and yearly statistics. It also has
ncurses interface - Visual Monopoly. It shows time, date, duration,
cost and speed of every connection. Monopoly is fully configurable and
very comfortable.

%description -l pl
Monopoly - program zliczaj±cy po³±czenia ppp (ale nie tylko). U¿ywa
logów systemowych, aby stworzyæ swój w³asny plik z histori± po³±czeñ.
Mo¿e byæ u¿ywany z linii poleceñ do pokazywania dziennych,
miesiêcznych i rocznych statystyk. Posiada tak¿e interfejs u¿ytkownika
(w ncurses). Pokazuje datê, czas, d³ugo¶æ, koszt oraz prêdko¶æ ka¿dego
po³±czenia. Monopoly jest w pe³ni konfigurowalne i bardzo wygodne.

%description -l fr
Monopoly - un programme pour compter (mais pas seulement) les
connexions. Il utilise les logs systèmes pour créer son propre fichier
log. Il peut etre utilisé depuis la ligne de commande pour montrer les
statistiques du jours, du mois et de l'année. Il a aussi une interface
ncurses - Visual Monopoly. Elle montre le temps, la date, la durée, le
cout et la vitesse de chaque connexion. Monopoly est entièrement
configurable et très confortable d'utilisation.

%prep
%setup -q

%build
rm -f missing
aclocal -I macros
autoconf
automake -a -c -f
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf doc/{CHANGES,README,TODO,TROUBLES,pl/*}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc doc/*.gz
%lang(pl) %doc doc/pl

%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/monopolyrc

%{_mandir}/man1/*
