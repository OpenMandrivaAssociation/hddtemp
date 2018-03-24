%define betarel beta15

Summary:	Hard Drive Temperature Monitoring
Name:		hddtemp
Version:	0.3
Release:	0.%{betarel}.17
License:	GPLv2
Group:		Monitoring
Url:		http://www.guzu.net/linux/hddtemp.php
Source0:	http://download.savannah.nongnu.org/releases/hddtemp/hddtemp-%{version}-%{betarel}.tar.bz2
Source2:	http://download.savannah.nongnu.org/releases/hddtemp/hddtemp.db
Source3:	hddtemp.service
Source4:	hddtemp.sysconfig
Source5:	hddtemp.pam
Source6:	hddtemp.consoleapp
Patch0:		0001-Try-attribute-190-if-194-doesn-t-exist.patch
Patch1:		http://ftp.debian.org/debian/pool/main/h/hddtemp/hddtemp_0.3-beta15-52.diff.gz
# https://bugzilla.redhat.com/show_bug.cgi?id=717479
# https://bugzilla.redhat.com/show_bug.cgi?id=710055
Patch2:		%{name}-0.3-beta15-autodetect-717479.patch
Patch3:		0001-Allow-binding-to-a-listen-address-that-doesn-t-exist.patch
Patch4:		fix-model-length.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1555871
Patch5:		%{name}-user-context-type.patch
BuildRequires:	gettext
BuildRequires:	pkgconfig(libsystemd)
Requires(post,postun):	rpm-helper
Requires:	usermode-consoleonly

%description
hddtemp is a tool that gives you the temperature of your IDE or SCSI hard drive
(that support this feature) by reading S.M.A.R.T. information. Only modern hard
drives have a temperature sensor.

%prep
%setup -qn %{name}-%{version}-%{betarel}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch0 -p1
%patch4 -p1
%patch5 -p1

sed -i -e 's|/etc/hddtemp.db|/usr/share/misc/hddtemp.db|' doc/hddtemp.8

%build
%configure \
	--with-db-path=%{_datadir}/misc/hddtemp.db

%make

%install
%makeinstall_std
install -Dpm 0644 %{SOURCE2} %{buildroot}%{_datadir}/misc/hddtemp.db
install -Dpm 0644 %{SOURCE3} %{buildroot}%{_unitdir}/hddtemp.service
install -Dpm 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/sysconfig/hddtemp
mkdir -p %{buildroot}%{_bindir}
ln -s consolehelper %{buildroot}%{_bindir}/hddtemp
install -m 0644 %{SOURCE5} -D %{buildroot}%{_sysconfdir}/pam.d/hddtemp
install -m 0644 %{SOURCE6} -D %{buildroot}%{_sysconfdir}/security/console.apps/hddtemp

install -d %{buildroot}%{_presetdir}
cat > %{buildroot}%{_presetdir}/86-hddtemp.preset << EOF
enable hddtemp.service
EOF

%find_lang %{name}

%files -f %{name}.lang
%doc ChangeLog README TODO contribs debian/changelog
%{_bindir}/hddtemp
%{_unitdir}/hddtemp.service
%{_sbindir}/hddtemp
%{_datadir}/hddtemp.db
%{_presetdir}/86-hddtemp.preset
%config(noreplace) %{_sysconfdir}/sysconfig/hddtemp
%config(noreplace) %{_sysconfdir}/pam.d/hddtemp
%config(noreplace) %{_sysconfdir}/security/console.apps/hddtemp
%{_mandir}/man8/hddtemp.8*
