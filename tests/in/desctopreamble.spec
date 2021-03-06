Name:           wireless-regdb

%description
The 802.11 regulatory domain database is used by CRDA and provides
allowed frequency ranges for 802.11 wireless drivers.

%if 0%{?suse_version} == 1110
# _libexecdir points to /usr/lib64 for SLE11
%define _libexecdir %{_prefix}/lib
%endif

%package whatever
Requires:       blabla
#blabla
%install
%make_install

# OURUGLYBUILDPHASE
%build
%configure

%changelog
