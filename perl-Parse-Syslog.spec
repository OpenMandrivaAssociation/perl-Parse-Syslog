%define	upstream_name    Parse-Syslog
%define upstream_version 1.11
Name:		perl-%{upstream_name}
Version:	1.11
Release:	1

Summary:	Parse Unix syslog files
License:	GPL
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{upstream_name}
Source0:	https://cpan.metacpan.org/authors/id/D/DS/DSCHWEI/Parse-Syslog-1.11.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Unix syslogs are convenient to read for humans but because of small differences
between operating systems and things like 'last message repeated xx times' not
very easy to parse by a script.

Parse::Syslog presents a simple interface to parse syslog files: you create a
parser on a file (with new) and call next to get one line at a time with
Unix-timestamp, host, program, pid and text returned in a hash-reference.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%{perl_vendorlib}/Parse
%{_mandir}/*/*

