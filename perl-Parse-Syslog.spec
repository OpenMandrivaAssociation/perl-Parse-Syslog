%define	module Parse-Syslog

Summary:	Parse::Syslog - Parse Unix syslog files
Name:		perl-%{module}
Version:	1.09
Release:	%mkrel 2
License:	GPL
Group:		Development/Perl
URL:		http://www.cpan.org/
Source0:	http://search.cpan.org/CPAN/authors/id/D/DS/DSCHWEI/%{module}-%{version}.tar.bz2
Buildrequires:	perl-devel
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Unix syslogs are convenient to read for humans but because of small differences
between operating systems and things like 'last message repeated xx times' not
very easy to parse by a script.

Parse::Syslog presents a simple interface to parse syslog files: you create a
parser on a file (with new) and call next to get one line at a time with
Unix-timestamp, host, program, pid and text returned in a hash-reference.

%prep

%setup -q -n %{module}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor

%make

%install
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{perl_vendorlib}/Parse/Syslog.pm
%{_mandir}/*/*


