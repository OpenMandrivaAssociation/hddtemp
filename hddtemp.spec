%define         betarel        beta15

Summary:        Hard Drive Temperature Monitoring
Name:           hddtemp
Version:        0.3 
Release:        0.%{betarel}.15
License:        GPLv2
Group:          Monitoring        
Url:            http://www.guzu.net/linux/hddtemp.php
Source0:        http://download.savannah.nongnu.org/releases/hddtemp/hddtemp-%{version}-%{betarel}.tar.bz2
Source1:        http://download.savannah.nongnu.org/releases/hddtemp/hddtemp-%{version}-%{betarel}.tar.bz2.sig
Source2:        http://download.savannah.nongnu.org/releases/hddtemp/hddtemp.db
Source3:        hddtemp.init
Source4:        hddtemp.sysconfig
Source5:        hddtemp.pam
Source6:        hddtemp.consoleapp
Patch0:		hddtemp_0.3-beta15-45.diff
Patch1:		%{name}-0.3-beta15-reg-eip.patch
BuildRequires:  gettext
BuildRequires:  perl
Requires(post,postun):	rpm-helper
Requires:       usermode-consoleonly

%description
hddtemp is a tool that gives you the temperature of your IDE or SCSI hard drive
(that support this feature) by reading S.M.A.R.T. information. Only modern hard
drives have a temperature sensor.

%prep
%setup -qn %{name}-%{version}-%{betarel}
%apply_patches

%build
%configure2_5x \
	--with-db-path=%{_sysconfdir}/hddtemp.db

%make

%install
%makeinstall_std

install -m 0644 %{SOURCE2} -D %{buildroot}%{_sysconfdir}/hddtemp.db
install -m 0755 %{SOURCE3} -D %{buildroot}%{_initrddir}/hddtemp
install -m 0644 %{SOURCE4} -D %{buildroot}%{_sysconfdir}/sysconfig/hddtemp
mkdir -p %{buildroot}%{_bindir}
ln -s consolehelper %{buildroot}%{_bindir}/hddtemp
install -m 0644 %{SOURCE5} -D %{buildroot}%{_sysconfdir}/pam.d/hddtemp
install -m 0644 %{SOURCE6} -D %{buildroot}%{_sysconfdir}/security/console.apps/hddtemp

%find_lang %{name}

%post
%_post_service hddtemp

%preun
%_preun_service hddtemp

%files -f %{name}.lang
%doc ChangeLog README TODO contribs debian/changelog
%{_bindir}/hddtemp
%{_initrddir}/hddtemp
%{_sbindir}/hddtemp
%config(noreplace) %{_sysconfdir}/hddtemp.db
%config(noreplace) %{_sysconfdir}/sysconfig/hddtemp
%config(noreplace) %{_sysconfdir}/pam.d/hddtemp
%config(noreplace) %{_sysconfdir}/security/console.apps/hddtemp
%{_mandir}/man8/hddtemp.8*

