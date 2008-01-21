%define	module Parse-Syslog

Summary:	Parse Unix syslog files
Name:		perl-%{module}
Version:	1.10
Release:	%mkrel 1
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://search.cpan.org/CPAN/modules/by-module/Parse/%{module}-%{version}.tar.bz2
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}

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
%{perl_vendorlib}/Parse
%{_mandir}/*/*
