Name:      observatory-robodimm-server
Version:   observatory
Release:   0
Url:       https://github.com/warwick-one-metre/robodimmd
Summary:   Front end for the ING RoboDIMM seeing monitor for the Warwick La Palma telescopes
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3 python3-Pyro4 python3-warwick-observatory-common

%description

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}

%{__install} %{_sourcedir}/robodimmd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/robodimmd.service %{buildroot}%{_unitdir}

%files
%defattr(0755,root,root,-)
%{_bindir}/robodimmd
%defattr(-,root,root,-)
%{_unitdir}/robodimmd.service

%changelog
