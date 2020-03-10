#
# spec file for package dnscrypt-proxy
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           dnscrypt-proxy
Version:        2.0.39
Release:        0
Summary:	A tool for securing communications between a client and a DNS resolver
# FIXME: Select a correct license from https://github.com/openSUSE/spec-cleaner#spdx-licenses
License:        BSD-3-Clause
# FIXME: use correct group, see "https://en.opensuse.org/openSUSE:Package_group_guidelines"
Group:          Productivity/Networking/DNS/Utilities
Url:            https://dnscrypt.org/
Source:         https://github.com/DNSCrypt/%{name}/releases/download/%{version}/%{name}-linux_x86_64-%{version}.tar.gz
Source1:        dnscrypt-proxy@.service
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{?systemd_requires}
Provides:       dnscrypt = %{version}-%{release}
Obsoletes:      dnscrypt < %{version}-%{release}

%description
dnscrypt-proxy provides local service which can be used directly as your local resolver or as a DNS forwarder,
encrypting and authenticating requests using the DNSCrypt protocol and passing them to an upstream server,
by default Cisco who run this on their resolvers. (It used to be OpenDNS.)

The DNSCrypt protocol uses elliptic-curve cryptography and is similar to DNSCurve, but focuses on
securing communications between a client and its first-level resolver.

While not providing end-to-end security, it protects the local network, which is often the weakest point
of the chain, against man-in-the-middle attacks. It also provides some confidentiality to DNS queries.


%prep
tar xzf %{S:0}

%build

%install
%{__install} -d %{buildroot}%{_sbindir}/ %{buildroot}%{_sysconfdir}/%{name}/ %{buildroot}%{_unitdir}/
%{__install} -m 0755 linux-x86_64/%{name} %{buildroot}%{_sbindir}/%{name}
%{__install} -m 0644 linux-x86_64/example-%{name}.toml %{buildroot}%{_sysconfdir}/%{name}/%{name}.toml
%{__install} -m 0644 %{S:1} %{buildroot}%{_unitdir}/%{name}@.service

%pre
%service_add_pre %{name}@.service

%post
%service_add_post %{name}@.service

%preun
%service_del_preun %{name}@.service

%postun
%service_del_postun %{name}@.service

%files
%defattr(-,root,root)
%{_sbindir}/%{name}
%dir %{_sysconfdir}/%{name}
%config %{_sysconfdir}/%{name}/%{name}.toml
%{_unitdir}/%{name}@.service

%changelog

