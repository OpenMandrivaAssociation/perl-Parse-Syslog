%define	upstream_name    Parse-Syslog
%define	upstream_version 1.10

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Parse Unix syslog files
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/modules/by-module/Parse/%{upstream_name}-%{upstream_version}.tar.bz2

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%{perl_vendorlib}/Parse
%{_mandir}/*/*

%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.100.0-1mdv2010.0
+ Revision: 404287
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.10-4mdv2009.0
+ Revision: 258193
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.10-3mdv2009.0
+ Revision: 246273
- rebuild

* Mon Jan 21 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.10-1mdv2008.1
+ Revision: 155670
- update to new version 1.10

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.09-3mdv2008.1
+ Revision: 137160
- spec cleanup

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.09-2mdv2008.1
+ Revision: 137070
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Dec 17 2006 Oden Eriksson <oeriksson@mandriva.com> 1.09-1mdv2007.0
+ Revision: 98326
- Import perl-Parse-Syslog

* Sun Dec 17 2006 Oden Eriksson <oeriksson@mandriva.com> 1.09-1mdv2007.1
- initial Mandriva package (fixes #26912)

