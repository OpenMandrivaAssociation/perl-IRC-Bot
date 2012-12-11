%define upstream_name    IRC-Bot
%define upstream_version 0.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Channel Maintenance IRC bot
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/B/BW/BWSMITH/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(POE::Component::IRC)
BuildRequires:	perl(Cache::Cache)
BuildArch:	noarch

%description
A complete bot, similar to eggdrop using POE::Component::IRC. Allows access to
all channel user management modes. Provides !seen functions, a complete help
system, logging, dcc chat interface, and it runs as a daemon process. IRC::Bot
utilizes Cache::FileCache for seen functions, and for session handling.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
%make test

%files
%doc Changes
%{perl_vendorlib}/IRC
%{perl_vendorlib}/auto/IRC
%{_mandir}/*/*

%changelog
* Tue Jul 28 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.80.0-1mdv2010.0
+ Revision: 402565
- rebuild using %%perl_convert_version

* Mon May 11 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.08-1mdv2010.0
+ Revision: 374539
- update to 0.08

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.06-5mdv2009.0
+ Revision: 241567
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-3mdv2008.0
+ Revision: 86513
- rebuild


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-2mdv2007.0
- Rebuild

* Fri Mar 03 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.06-1mdk
- 0.06

* Fri Sep 30 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.04-4mdk
- Fix BuildRequires

* Sat Jun 11 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-3mdk 
- better url
- spec cleanup
- don't ship useless empty directories
- make test in %%check
- buildrequires

* Sun Feb 06 2005 Sylvie Terjan <erinmargault@mandrake.org> 0.04-2mdk
- rebuild for new perl

* Sat Jul 24 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.04-1mdk 
- first mdk release

