Summary: 	A QT gui for the jack audio daemon
Name: 	 	qjackctl
Version: 	0.3.1a
Release: 	%mkrel 2
License:	GPL
Group:		Sound
URL:		http://sourceforge.net/projects/qjackctl/
Source:		http://prdownloads.sourceforge.net/qjackctl/%{name}-%{version}.tar.gz
BuildRequires:	qt4-devel jackit-devel ImageMagick alsa-lib-devel
BuildRequires:	desktop-file-utils
Requires:	jackit >= 0.90.0
BuildRoot:	%{_tmppath}/%{name}-buildroot

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
rm -rf %{buildroot}

%makeinstall

#menu
desktop-file-install --vendor="" \
  --remove-category="ALSA" \
  --remove-category="JACK" \
  --remove-category="MIDI" \
  --remove-category="Multimedia" \
  --remove-category="Applications" \
  --remove-category="AudioVideo" \
  --remove-category="Qt" \
  --add-category="Audio" \
  --add-category="X-MandrivaLinux-Sound" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

#icons
mkdir -p %{buildroot}/%_liconsdir
convert -size 48x48 icons/%name.png %{buildroot}/%_liconsdir/%name.png
mkdir -p %{buildroot}/%_iconsdir
convert -size 32x32 icons/%name.png %{buildroot}/%_iconsdir/%name.png
mkdir -p %{buildroot}/%_miconsdir
convert -size 16x16 icons/%name.png %{buildroot}/%_miconsdir/%name.png

%clean
rm -rf %{buildroot}

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
