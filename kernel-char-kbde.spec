Summary:	Keyboard emulator driver for Linux kernel
Summary(pl.UTF-8):   Sterownik emulatora klawiatury dla jądra Linuksa
Name:		kernel-char-kbde
Version:	1.0.0
Release:	1
License:	GPL
Group:		System Environment/Kernel
Source0:	http://dl.sourceforge.net/kbde/kbde-driver-%{version}.tar.gz
URL:		http://kbde.sourceforge.net/
Obsoletes:	kbde-driver
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Keyboard emulator driver is a Linux kernel module, which allow emulate
keyboard input on the x86 computer.

%description -l pl.UTF-8
Sterownik emulatora klawiatury to moduł jądra Linuksa pozwalający
emulować wejście z klawiatury na komputerach x86.

%prep
%setup -q

%build
%{__make} all

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%depmod %{_kernel_ver}
#kbde_dev="/dev/kbde"
#rm --force $kbde_dev
#mknod --mode=200 $kbde_dev c 11 0

%postun
%depmod %{_kernel_ver}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INSTALL LICENSE NEWS README
/lib/modules/%{module_kernel_version}/misc/kbde.*o*
%{_mandir}/man4/kbde.4*
%{_mandir}/man9/kbde.9*
