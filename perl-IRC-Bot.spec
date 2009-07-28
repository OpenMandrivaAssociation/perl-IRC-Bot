%define upstream_name    IRC-Bot
%define upstream_version 0.08

Name:           perl-%{upstream_name}
Version:        %perl_convert_version %{upstream_version}
Release:        %mkrel 1

Summary:        Channel Maintenance IRC bot
License:        GPL+ or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{upstream_name}
Source0:        http://search.cpan.org/CPAN/authors/id/B/BW/BWSMITH/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl(POE::Component::IRC)
BuildRequires:  perl(Cache::Cache)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
A complete bot, similar to eggdrop using POE::Component::IRC. Allows access to
all channel user management modes. Provides !seen functions, a complete help
system, logging, dcc chat interface, and it runs as a daemon process. IRC::Bot
utilizes Cache::FileCache for seen functions, and for session handling.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%check
%make test

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/IRC
%{perl_vendorlib}/auto/IRC
%{_mandir}/*/*
