%define	upstream_name    Parse-Syslog
%define	upstream_version 1.10

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Parse Unix syslog files
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/modules/by-module/Parse/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Unix syslogs are convenient to read for humans but because of small differences
between operating systems and things like 'last message repeated xx times' not
very easy to parse by a script.

Parse::Syslog presents a simple interface to parse syslog files: you create a
parser on a file (with new) and call next to get one line at a time with
Unix-timestamp, host, program, pid and text returned in a hash-reference.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
