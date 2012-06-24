Summary:   	Monopoly
Summary(pl): 	Monopoly
Name:      	monopoly
Version:   	1.5.7
Release:   	1
Copyright:      GPL
Group:          Applications/Networking
Group(pl):      Aplikacje/Sieciowe
Source:    	http://dione.ids.pl/~yossa/monopoly/%{name}-%{version}.tar.gz
Patch:		monopoly-makefile.patch
BuildPrereq:	ncurses-devel
BuildRoot: 	/tmp/%{name}-%{version}-root

%define	_sysconfdir	/etc

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
%patch -p0

%build
make monopoly \
	CFLAGS="$RPM_OPT_FLAGS -I/usr/include/ncurses" \
	CFGFILE="%{_sysconfdir}/monopolyrc"

%install
rm -rf $RPM_BUILD_ROOT

make install \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	CFGDIR=%{_sysconfdir}
	
gzip -9nf doc/{CHANGES,README,TODO,TROUBLES,pl/*} 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755) 
%doc doc/{CHANGES,README,TODO,TROUBLES}.gz
%lang(pl) %doc doc/pl

%attr(755,root,root) %{_bindir}/*
%config %{_sysconfdir}/monopolyrc

%changelog
* Sat Jul 03 1999 Piotr Czerwi�ski <pius@pld.org.pl> 
  [1.5.6-1]
- updated to 1.5.6,
- added monopoly-makefile.patch,
- some cleanups.

* Fri Oct 16 1998 Piotr Grochowski <pager@dione.ids.pl>
  [1.5.4-1]
- first relase as PLD package.
