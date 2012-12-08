%define upstream_name	 Math-Pari
%define upstream_version 2.01080605

%define pari_version	2.3.3

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 5
Epoch:      1

Summary:    Perl interface to PARI
License:    GPLv2+ or Artistic
Group:      Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Math/%{upstream_name}-%{upstream_version}.tar.gz
Source1:    ftp://megrez.math.u-bordeaux.fr/pub/pari/unix/pari-%{pari_version}.tar.gz

BuildRequires:  perl-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
This package is a Perl interface to famous library PARI for
numerical/scientific/number-theoretic calculations. It allows use of
most PARI functions as Perl functions, and (almost) seamless merging of
PARI and Perl data. See ftp://megrez.math.u-bordeaux.fr/pub/pari for
more information about PARI.

%prep
%setup -q      -n %{upstream_name}-%{upstream_version}
%setup -q -a 1 -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor paridir=pari-%{pari_version} < /dev/null
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
%defattr(644,root,root,755)
%doc README Changes
%{perl_vendorarch}/Math
%{perl_vendorarch}/auto/Math
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1:2.10.806.50-5mdv2012.0
+ Revision: 765476
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1:2.10.806.50-4
+ Revision: 763970
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1:2.10.806.50-3
+ Revision: 676632
- rebuild

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1:2.10.806.50-2
+ Revision: 676526
- rebuild

* Mon May 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1:2.10.806.50-1
+ Revision: 662080
- update to new version 2.01080605

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1:2.10.806.40-3mdv2011.0
+ Revision: 556003
- rebuild for perl 5.12

  + Michael Scherer <misc@mandriva.org>
    - fix License
    - fix permissions

* Thu Mar 04 2010 Jérôme Quelin <jquelin@mandriva.org> 1:2.10.806.40-1mdv2010.1
+ Revision: 514104
- update to 2.01080604

* Sat Dec 12 2009 Jérôme Quelin <jquelin@mandriva.org> 1:2.10.806.30-1mdv2010.1
+ Revision: 477627
- update to 2.01080603

* Thu Nov 12 2009 Jérôme Quelin <jquelin@mandriva.org> 1:2.10.806.20-1mdv2010.1
+ Revision: 465169
- update to 2.01080602

* Sun Nov 08 2009 Jérôme Quelin <jquelin@mandriva.org> 1:2.10.806.10-1mdv2010.1
+ Revision: 462865
- update to 2.01080601

* Sat Nov 07 2009 Jérôme Quelin <jquelin@mandriva.org> 1:2.10.806-1mdv2010.1
+ Revision: 462464
- update to 2.010806
- update to 2.010806

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 2.010801-2mdv2010.0
+ Revision: 440612
- rebuild

* Fri Feb 13 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.010801-1mdv2009.1
+ Revision: 340033
- update to new version 2.010801

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

  + Olivier Thauvin <nanardon@mandriva.org>
    - update internal pari version

* Tue May 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.010800-1mdv2009.0
+ Revision: 201860
- update to new version 2.010800

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - rebuild for perl-5.10.0

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 2.010709-1mdv2008.1
+ Revision: 136283
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Jan 07 2007 Olivier Thauvin <nanardon@mandriva.org> 2.010709-1mdv2007.0
+ Revision: 105109
- 2.010709
- use pari 2.1.7
- disable test on x86_64 (will fix later)
- Import perl-Math-Pari

* Thu Jun 22 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.010706-1mdv2007.0
- New version 2.010706

* Fri Jun 02 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.010705-1mdv2007.0
- New release 2.010705
- spec cleanup

* Mon Mar 20 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.010704-1mdk
- 2.010704

* Wed Feb 01 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.010703-1mdk
- 2.010703

* Thu Nov 24 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.010702-1mdk
- 2.010702

* Thu Nov 10 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.010701-1mdk
- 2.010701

* Mon Oct 31 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.010700-1mdk
- New version 2.010700

* Sat Oct 01 2005 Nicolas L�cureuil <neoclust@mandriva.org> 2.010604-2mdk
- Buildrequires fix

* Sat Sep 24 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.010604-1mdk
- New version

* Thu Jun 30 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.010603-2mdk
- Rebuild

* Thu Jan 20 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 2.010603-1mdk
- New version

* Mon Jan 10 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 2.010602-2mdk
- Better wording in the description

* Mon Jan 10 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 2.010602-1mdk
- New version

* Tue Dec 21 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 2.010601-1mdk
- New version
- Add Changes in documentation

* Mon Dec 13 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 2.010600-1mdk
- New version
- Include the pari sources in the RPM instead of downloading them during compilation
- Remove BuildRequires on pari

