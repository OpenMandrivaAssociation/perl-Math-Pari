%define upstream_name Math-Pari
%define upstream_version 2.01080605

%define pari_version 2.3.3

Summary:	Perl interface to PARI
Name:		perl-%{upstream_name}
Epoch:		1
Version:	%perl_convert_version %{upstream_version}
Release:	7
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Math/%{upstream_name}-%{upstream_version}.tar.gz
Source1:	ftp://megrez.math.u-bordeaux.fr/pub/pari/unix/pari-%{pari_version}.tar.gz

BuildRequires:	perl-devel

%description
This package is a Perl interface to famous library PARI for
numerical/scientific/number-theoretic calculations. It allows use of
most PARI functions as Perl functions, and (almost) seamless merging of
PARI and Perl data. See ftp://megrez.math.u-bordeaux.fr/pub/pari for
more information about PARI.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%setup -q -a 1 -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor paridir=pari-%{pari_version} < /dev/null
%make CFLAGS="%{optflags}"

%ifnarch x86_64
%check
%make test
%endif

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorarch}/Math
%{perl_vendorarch}/auto/Math
%{_mandir}/*/*

