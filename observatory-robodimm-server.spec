Name:      observatory-robodimm-server
Version:   1.0.1
Release:   0
Url:       https://github.com/warwick-one-metre/tngd
Summary:   Front end for the ING RoboDIMM seeing monitor for the Warwick La Palma telescopes
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python36, python36-Pyro4, python36-warwick-observatory-common
Requires:  observatory-log-client, %{?systemd_requires}

%description
Part of the observatory software for the Warwick La Palma telescopes.

robodimmd is a Pyro frontend for querying the ING RoboDIMM seeing measurement via http.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}

%{__install} %{_sourcedir}/robodimmd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/robodimmd.service %{buildroot}%{_unitdir}

%post
%systemd_post robodimmd.service

%preun
%systemd_preun robodimmd.service

%postun
%systemd_postun_with_restart robodimmd.service

%files
%defattr(0755,root,root,-)
%{_bindir}/robodimmd
%defattr(-,root,root,-)
%{_unitdir}/robodimmd.service

%changelog
