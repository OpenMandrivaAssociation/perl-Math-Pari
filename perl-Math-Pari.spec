%define module		Math-Pari
%define	name		perl-%{module}
%define	version		2.010800
%define pariversion	2.1.7
%define	release		%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:        Perl interface to PARI
License:        GPL or Artistic
Group:          Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/modules/by-module/Math/%{module}-%{version}.tar.bz2
Source1:        ftp://megrez.math.u-bordeaux.fr/pub/pari/unix/pari-%{pariversion}.tar.bz2
BuildRequires:  perl-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
This package is a Perl interface to famous library PARI for
numerical/scientific/number-theoretic calculations. It allows use of
most PARI functions as Perl functions, and (almost) seamless merging of
PARI and Perl data. See ftp://megrez.math.u-bordeaux.fr/pub/pari for
more information about PARI.

%prep
%setup -q -n %{module}-%{version}
%setup -q -a 1 -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor paridir=pari-%{pariversion} < /dev/null
%make CFLAGS="%{optflags}"

%ifnarch x86_64
%check
%{__make} test
%endif

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorarch}/Math
%{perl_vendorarch}/auto/Math
%{_mandir}/*/*


