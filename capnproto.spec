
%define longhash %(git log | head -1 | awk '{print $2}')
%define shorthash %(echo %{longhash} | dd bs=1 count=12)

Name:           capnproto-c++
Version:        0.5
Release:        0.strato.%{shorthash}
Summary:        A data interchange format and capability-based RPC system

License:        BSD
URL:            http://capnproto.org/

%description
Capâ€™n Proto is an insanely fast data interchange format and
capability-based RPC system. Think JSON, except binary. Or think
Protocol Buffers, except faster. In fact, in benchmarks, Capâ€™n Proto is
INFINITY TIMES faster than Protocol Buffers.


%package devel
Summary: development headers

%description devel
This package static libraries and include file of capnproto

%build
cp -avr %{TOP}/build/install/* .


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_libdir}
mkdir -p $RPM_BUILD_ROOT/%{_includedir}
cp -avr include/capnp $RPM_BUILD_ROOT/%{_includedir}
cp -avr include/kj $RPM_BUILD_ROOT/%{_includedir}
cp -av lib/libcapnp* $RPM_BUILD_ROOT/%{_libdir}
cp -av lib/libkj* $RPM_BUILD_ROOT/%{_libdir}
cp -av bin/capnp* $RPM_BUILD_ROOT/%{_bindir}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_bindir}/capnp*
%{_libdir}/libcapnp*.so
%{_libdir}/libkj*.so

%files devel
%{_includedir}/capnp/*
%{_includedir}/kj/*
%{_libdir}/libcapnp*.a
%{_libdir}/libkj*.a


