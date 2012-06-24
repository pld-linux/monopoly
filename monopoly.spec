Summary:   	Monopoly
Summary(pl): 	Monopoly
Name:      	monopoly
Version:   	1.6.1
Release:   	2
Copyright:      GPL
Group:          Applications/Networking
Group(pl):      Aplikacje/Sieciowe
Source:    	http://dione.ids.pl/~yossa/monopoly/%{name}-%{version}.tar.gz
BuildRequires:	ncurses-devel >= 5.0
BuildRoot: 	/tmp/%{name}-%{version}-root

%define		_sysconfdir	/etc

%description
Monopoly - a program for counting ppp (but not only) connections. It uses
system logs to create its own log file. It can be used from command line
to show daily, monthly and yearly statistics. It also has ncurses
interface - Visual Monopoly. It shows time, date, duration, cost and speed
of every connection. Monopoly is fully configurable and very comfortable.

%description -l pl
Monopoly - program zliczaj�cy po��czenia ppp (ale nie tylko). U�ywa log�w
systemowych, aby stworzy� sw�j w�asny plik z histori� po��cze�. Mo�e by�
u�ywany z linii polece� do pokazywania dziennych, miesi�cznych i rocznych
statystyk. Posiada tak�e interfejs u�ytkownika (w ncurses). Pokazuje dat�,
czas, d�ugo��, koszt oraz pr�dko�� ka�dego po��czenia. Monopoly jest w
pe�ni konfigurowalne i bardzo wygodne.

%prep
%setup -q

%build
LDFLAGS="-s" ; export LDFLAGS
%configure

make 

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT 
	
gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	doc/{CHANGES,README,TODO,TROUBLES,pl/*} 

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755) 
%doc doc/{CHANGES,README,TODO,TROUBLES}.gz
%lang(pl) %doc doc/pl

%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/monopolyrc

#%{_mandir}/man1/monopoly.1.gz
