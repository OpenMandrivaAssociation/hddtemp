%define         betarel        beta15

Summary:        Hard Drive Temperature Monitoring
Name:           hddtemp
Version:        0.3 
Release:        %mkrel 0.%{betarel}.15
License:        GPLv2
Group:          Monitoring        
URL:            http://www.guzu.net/linux/hddtemp.php
Source0:        http://download.savannah.nongnu.org/releases/hddtemp/hddtemp-%{version}-%{betarel}.tar.bz2
Source1:        http://download.savannah.nongnu.org/releases/hddtemp/hddtemp-%{version}-%{betarel}.tar.bz2.sig
Source2:        http://download.savannah.nongnu.org/releases/hddtemp/hddtemp.db
Source3:        hddtemp.init
Source4:        hddtemp.sysconfig
Source5:        hddtemp.pam
Source6:        hddtemp.consoleapp
Patch0:		hddtemp_0.3-beta15-45.diff
Patch1:		%{name}-0.3-beta15-reg-eip.patch
Requires(post): rpm-helper
Requires(preun): rpm-helper
Requires:       usermode-consoleonly
BuildRequires:  gettext
BuildRequires:  perl
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
hddtemp is a tool that gives you the temperature of your IDE or SCSI hard drive
(that support this feature) by reading S.M.A.R.T. information. Only modern hard
drives have a temperature sensor.

%prep
%setup -q -n hddtemp-%{version}-%{betarel}
%patch0 -p1
%patch1 -p1

%build
%configure2_5x \
    --with-db-path=%{_sysconfdir}/hddtemp.db

%make

%install
%{__rm} -rf %{buildroot}

%makeinstall_std

%{__install} -m 0644 %{SOURCE2} -D %{buildroot}%{_sysconfdir}/hddtemp.db
%{__install} -m 0755 %{SOURCE3} -D %{buildroot}%{_initrddir}/hddtemp
%{__install} -m 0644 %{SOURCE4} -D %{buildroot}%{_sysconfdir}/sysconfig/hddtemp
%{__mkdir_p} %{buildroot}%{_bindir}
%{__ln_s} consolehelper %{buildroot}%{_bindir}/hddtemp
%{__install} -m 0644 %{SOURCE5} -D %{buildroot}%{_sysconfdir}/pam.d/hddtemp
%{__install} -m 0644 %{SOURCE6} -D %{buildroot}%{_sysconfdir}/security/console.apps/hddtemp

%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%post
%_post_service hddtemp

%preun
%_preun_service hddtemp

%files -f %{name}.lang
%defattr(0644,root,root,0755)
%doc ChangeLog README TODO contribs debian/changelog
%attr(0755,root,root) %{_bindir}/hddtemp
%attr(0755,root,root) %{_initrddir}/hddtemp
%attr(0755,root,root) %{_sbindir}/hddtemp
%config(noreplace) %{_sysconfdir}/hddtemp.db
%config(noreplace) %{_sysconfdir}/sysconfig/hddtemp
%config(noreplace) %{_sysconfdir}/pam.d/hddtemp
%config(noreplace) %{_sysconfdir}/security/console.apps/hddtemp
%{_mandir}/man8/hddtemp.8*


%changelog
* Sun May 15 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3-0.beta15.14mdv2011.0
+ Revision: 674844
- fix build (fedora)
- mass rebuild

* Thu Aug 19 2010 Stéphane Téletchéa <steletch@mandriva.org> 0.3-0.beta15.13mdv2011.0
+ Revision: 571333
- Update drive search so newer nomenclature aka sda instead of hda is also searched
- Add a wildcard for searching all drives, a better heuristics detection would be better, but enough for now

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3-0.beta15.12mdv2010.1
+ Revision: 519823
- rebuild
- small fix
- added 2 models

* Sun Oct 04 2009 Oden Eriksson <oeriksson@mandriva.com> 0.3-0.beta15.11mdv2010.0
+ Revision: 453469
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sun Nov 30 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3-0.beta15.9mdv2009.1
+ Revision: 308452
- sync with debian (since the debian maintainer=upstream developer)

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.3-0.beta15.8mdv2009.0
+ Revision: 140746
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Nov 18 2007 David Walluck <walluck@mandriva.org> 0.3-0.beta15.8mdv2008.1
+ Revision: 109790
- fix bug #28793

* Mon Oct 22 2007 David Walluck <walluck@mandriva.org> 0.3-0.beta15.7mdv2008.1
+ Revision: 101082
- install hddtemp.db directly
- use %%{makeinstall_std}
- remove hddtemp-hddtemp-db-hdt-t7k250-250-wdc-re-160.patch (include directly into hddtemp.db)
- update to latest hddtemp.db (14-Sep-2007)
- add support for WDC WD1600YS-01S(|H0)

* Fri Jul 27 2007 David Walluck <walluck@mandriva.org> 0.3-0.beta15.7mdv2008.0
+ Revision: 56257
- add patch for Hitachi T7K250 250GB SATA

* Thu Jun 28 2007 David Walluck <walluck@mandriva.org> 0.3-0.beta15.6mdv2008.0
+ Revision: 45405
- update hddtemp-db-wd-re-160 patch for newer firmware


* Mon Feb 05 2007 David Walluck <walluck@mandriva.org> 0.3-0.beta15.5mdv2007.0
+ Revision: 116179
- add sources
- add patch for SATA under newer kernels
  add patch for WD Caviar RE 160 GB in hddtemp.db
  update source URL
  add tarball signature
  more consistent file list
  macros
- Import hddtemp

* Fri Sep 15 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.3-0.beta15.4mdv2007.0
- clean initscript (should fix #25694)

* Tue Aug 29 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.3-0.beta15.3mdv2007.0
- add /dev/hda to sysconfig file (modifies S3, fixes #18421)
- cosmetics

* Mon Jul 31 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.3-0.beta15.2mdv2007.0
- add two new disks (updated S1, from Pierre Jarillon)

* Mon May 29 2006 Oden Eriksson <oeriksson@mandriva.com> 0.3-0.beta15.1mdv2007.0
- 0.3-0beta15
- new S1

* Mon Jan 09 2006 Olivier Blin <oblin@mandriva.com> 0.3-0.beta14.5mdk
- split Requires(X,Y)
- fix typo in initscript

* Mon Jan 09 2006 Olivier Blin <oblin@mandriva.com> 0.3-0.beta14.4mdk
- fix copy/paste suckiness in initscript

* Mon Jan 09 2006 Olivier Blin <oblin@mandriva.com> 0.3-0.beta14.3mdk
- convert parallel init to LSB
- fix requires(post,preun)

* Sat Dec 31 2005 Couriousous <couriousous@mandriva.org> 0.3-0.beta14.2mdk
- Add parallel init stuff

* Tue Oct 04 2005 Lenny Cartier <lenny@mandriva.com> 0.3-0.beta14.1mdk
- beta14

* Tue Mar 15 2005 Tibor Pittich <Tibor.Pittich@mandrake.org> 0.3-0.beta12.2mdk
- update hddtemp.db
- remove suid bit
- add init script, config file and pam/consolehelper from fedora
- add gettext into buildrequires

* Thu Feb 17 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.3-0.beta12.1mdk
- 0.3-beta12
- update url
- update hddtemp.db
- don't ship license file as it's GPL

* Thu Mar 11 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.3-0.beta11.1mdk
- 0.3-beta11

