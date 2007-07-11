%define name	qjackctl
%define version 0.3.0
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	A QT gui for the jack audio daemon
Version: 	%{version}
Release: 	%{release}

Source:		http://prdownloads.sourceforge.net/qjackctl/%{name}-%{version}.tar.bz2
URL:		http://sourceforge.net/projects/qjackctl/
License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	qt4-devel jackit-devel ImageMagick alsa-lib-devel
BuildRequires:	desktop-file-utils
Requires:	jackit >= 0.90.0

%description
JACK Audio Connection Kit - Qt GUI Interface: A simple Qt application to
control the JACK server daemon.

%prep
%setup -q

%build
perl -pi -e 's/\$QTDIR\/lib/\$QTDIR\/%{_lib}/' configure
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

#menu
desktop-file-install --vendor="" \
  --add-category="X-MandrivaLinux-Sound" \
  --remove-category="ALSA" \
  --remove-category="JACK" \
  --remove-category="MIDI" \
  --remove-category="Multimedia" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 icons/%name.png $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 icons/%name.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 icons/%name.png $RPM_BUILD_ROOT/%_miconsdir/%name.png

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README TODO
%{_bindir}/%name
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*


