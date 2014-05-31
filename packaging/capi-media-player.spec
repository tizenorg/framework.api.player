Name:       capi-media-player
Summary:    A Media Player library in Tizen Native API
%if 0%{?tizen_profile_mobile}
Version:    0.1.0
Release:    0
%else
Version:    0.2.0
Release:    0
%endif
Group:      TO_BE/FILLED_IN
License:    TO BE FILLED IN
Source0:    %{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  pkgconfig(dlog)
BuildRequires:  pkgconfig(mm-player)
BuildRequires:  pkgconfig(capi-base-common)
BuildRequires:  pkgconfig(capi-media-sound-manager)
BuildRequires:  pkgconfig(gstreamer-0.10)
BuildRequires:  pkgconfig(mm-ta)
BuildRequires:  pkgconfig(appcore-efl)
BuildRequires:  pkgconfig(elementary)
BuildRequires:  pkgconfig(ecore)
BuildRequires:  pkgconfig(evas)
BuildRequires:  pkgconfig(ecore-x)

Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description


%package devel
Summary:  A Media Player library in Tizen Native API (Development)
Group:    TO_BE/FILLED_IN
Requires: %{name} = %{version}-%{release}

%description devel

%prep
%setup -q


%build
%if 0%{?tizen_profile_wearable}
cd wearable
%else
cd mobile
%endif
MAJORVER=`echo %{version} | awk 'BEGIN {FS="."}{print $1}'`
%cmake . -DFULLVER=%{version} -DMAJORVER=${MAJORVER}


make %{?jobs:-j%jobs}

%install
%if 0%{?tizen_profile_wearable}
cd wearable
%else
cd mobile
%endif
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/license
cp LICENSE.APLv2 %{buildroot}/usr/share/license/%{name}
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%if 0%{?tizen_profile_wearable}
%manifest wearable/capi-media-player.manifest
%else
%manifest mobile/capi-media-player.manifest
%endif
%{_libdir}/libcapi-media-player.so.*
%{_datadir}/license/%{name}

%files devel
%{_includedir}/media/*.h
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libcapi-media-player.so


