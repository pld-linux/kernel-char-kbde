%define my_name    kbde-driver
%define my_version 1.0.0
%define my_release 1

%{expand:%%define module_kernel_version %%( if [ "x$MODULE_KERNEL_VERSION" = "x" ]; then uname -r; else echo $MODULE_KERNEL_VERSION; fi)}
Name:          %{my_name}
Version:       %{my_version}
Release:       %{my_release}
License:       GPL
Group:         System Environment/Kernel
Summary:       keyboard emulator driver for kernel %{module_kernel_version}
Packager:      Valery Reznic <valery_reznic@users.sourceforge.net>
Source:        %{name}-%{version}.tar.gz
Url:           http://kbde.sourceforge.net
ExclusiveOs:   Linux
ExclusiveArch: i386
BuildRoot:     %{_builddir}/%{buildsubdir}-install-root

%description
Keyboard emulator driver is a linux kernel module,
which allow emulate keyboard input on the x86 computer.

%prep
%setup

%build
make all

%install
if [ "$RPM_BUILD_ROOT" != "/" ]; then
   rm -rf $RPM_BUILD_ROOT
else
   :
fi
make install DESTDIR="$RPM_BUILD_ROOT"

%clean
if [ "$RPM_BUILD_ROOT" != "/" ]; then
   rm -rf $RPM_BUILD_ROOT
else
   :
fi

%post
/sbin/depmod -a
kbde_dev="/dev/kbde"
rm --force $kbde_dev
mknod --mode=200 $kbde_dev c 11 0

%postun
# I am going neither remove /dev/kbde in the postun nor
# put it in the %%file section - the reason - it is possible to
# have a some similar packages installed on the same system in order
# to support different kernels
/sbin/depmod -a

%files

%defattr(-,root,root)
/lib/modules/%{module_kernel_version}/misc/kbde.*o

%doc %{_mandir}/man4/kbde.4*
%doc %{_mandir}/man9/kbde.9*

%doc AUTHORS
%doc ChangeLog
%doc INSTALL
%doc LICENSE
%doc NEWS
%doc README


%changelog
* Sun Jun  4 2004 <valery_reznic@users.sourceforge.net> 1.0.0-1
- Initial public release.
