Summary:	Monopoly - a program for counting ppp (but not only) connections
Summary(pl.UTF-8):   Monopoly program zliczający połączenia ppp (ale nie tylko)
Name:		monopoly
Version:	1.6.5
Release:	4
License:	GPL
Group:		Applications/Networking
#Source0:	http://dione.ids.pl/~yossa/monopoly/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	ec354f580d979d2b2732c19712cdce11
Patch0:		%{name}-po.patch
#URL:		http://dione.ids.pl/~yossa/monopoly/
#URL:		http://www.monopoly.ko.pl/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	slang-devel >= 2.0.0
BuildRequires:	zlib-devel
Requires:	ppp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Monopoly - a program for counting ppp (but not only) connections. It
uses system logs to create its own log file. It can be used from
command line to show daily, monthly and yearly statistics. It also has
ncurses interface - Visual Monopoly. It shows time, date, duration,
cost and speed of every connection. Monopoly is fully configurable and
very comfortable.

%description -l pl.UTF-8
Monopoly - program zliczający połączenia ppp (ale nie tylko). Używa
logów systemowych, aby stworzyć swój własny plik z historią połączeń.
Może być używany z linii poleceń do pokazywania dziennych,
miesięcznych i rocznych statystyk. Posiada także interfejs użytkownika
(w ncurses). Pokazuje datę, czas, długość, koszt oraz prędkość każdego
połączenia. Monopoly jest w pełni konfigurowalne i bardzo wygodne.

%description -l fr.UTF-8
Monopoly - un programme pour compter (mais pas seulement) les
connexions. Il utilise les logs systèmes pour créer son propre fichier
log. Il peut etre utilisé depuis la ligne de commande pour montrer les
statistiques du jours, du mois et de l'année. Il a aussi une interface
ncurses - Visual Monopoly. Elle montre le temps, la date, la durée, le
cout et la vitesse de chaque connexion. Monopoly est entièrement
configurable et très confortable d'utilisation.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal} -I macros
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc doc/{CHANGES,README,TODO,TROUBLES}
%lang(pl) %doc doc/pl

%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/monopolyrc

%{_mandir}/man1/*
