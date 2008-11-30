%define         betarel        beta15

Summary:        Hard Drive Temperature Monitoring
Name:           hddtemp
Version:        0.3 
Release:        %mkrel 0.%{betarel}.9
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
