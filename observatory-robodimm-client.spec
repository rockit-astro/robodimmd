Name:      observatory-robodimm-client
Version:   1.0.0
Release:   0
Url:       https://github.com/warwick-one-metre/robodimmd
Summary:   Front end for the ING RoboDIMM seeing monitor for the Warwick La Palma telescopes
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python36, python36-Pyro4, python36-warwick-observatory-common

%description
Part of the observatory software for the Warwick La Palma telescopes.

robodimm is a commandline utility that queries the RoboDIMM daemon.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}/etc/bash_completion.d
%{__install} %{_sourcedir}/robodimm %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/completion/robodimm %{buildroot}/etc/bash_completion.d/robodimm

%files
%defattr(0755,root,root,-)
%{_bindir}/robodimm
/etc/bash_completion.d/robodimm

%changelog
