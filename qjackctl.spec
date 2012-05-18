Summary:    A QT gui for the jack audio daemon
Name:       qjackctl
Version:    0.3.9
Release:    1

License:    GPLv2+
Group:      Sound
URL:        http://sourceforge.net/projects/qjackctl/
Source:     http://prdownloads.sourceforge.net/qjackctl/%{name}-%{version}.tar.gz
BuildRequires:  qt4-devel jackit-devel imagemagick libalsa-devel
BuildRequires: portaudio-devel
BuildRequires:  desktop-file-utils
Requires:   jackit

%description
JACK Audio Connection Kit - Qt GUI Interface: A simple Qt application to
control the JACK server daemon.

%prep

%setup -q

%build
%configure --enable-jack-version
make

%install
rm -rf %{buildroot}

%makeinstall_std

#menu
desktop-file-install --vendor="" \
  --remove-category="ALSA" \
  --remove-category="JACK" \
  --remove-category="MIDI" \
  --remove-category="Multimedia" \
  --remove-category="Applications" \
  --remove-category="Qt" \
  --add-category="Audio" \
  --add-category="X-MandrivaLinux-Sound" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README TODO
%{_mandir}/man1/*
%{_bindir}/%name
%{_iconsdir}/hicolor/32x32/apps/%name.png
%{_datadir}/applications/*.desktop
%{_datadir}/locale/*.qm
