%define name	qjackctl
%define version 0.2.21
%define release %mkrel 2

Name: 	 	%{name}
Summary: 	A QT gui for the jack audio daemon
Version: 	%{version}
Release: 	%{release}

Source:		http://prdownloads.sourceforge.net/qjackctl/%{name}-%{version}.tar.bz2
Source1:	jackwrapper.sh
URL:		http://sourceforge.net/projects/qjackctl/
License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	qt3-devel jackit-devel ImageMagick libalsa2-devel
Requires:	jackit >= 0.90.0
Provides:	jackwrapper

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
cat %SOURCE1 > $RPM_BUILD_ROOT/%_bindir/jackwrapper
chmod 755 $RPM_BUILD_ROOT/%_bindir/jackwrapper

#menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="%{name}.png" needs="x11" title="QJackCTL" longtitle="Controls the JACK Audio daemon" section="Multimedia/Sound"\
xdg="true"
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=QJackCTL
Comment=Controls the JACK Audio daemon
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Multimedia-Sound;AudioVideo;Audio;
Encoding=UTF-8
EOF


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
%{_bindir}/jackwrapper
%{_menudir}/%name
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
%{_datadir}/applications/mandriva-%{name}.desktop


