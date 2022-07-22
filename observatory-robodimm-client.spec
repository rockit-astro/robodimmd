Name:      observatory-robodimm-client
Version:   20220722
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
mkdir -p %{buildroot}/etc/bash_completion.d
%{__install} %{_sourcedir}/robodimm %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/completion/robodimm %{buildroot}/etc/bash_completion.d/robodimm

%files
%defattr(0755,root,root,-)
%{_bindir}/robodimm
/etc/bash_completion.d/robodimm

%changelog
