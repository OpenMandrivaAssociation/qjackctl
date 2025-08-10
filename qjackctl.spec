%global	debug_package	%{nil}
#define _empty_manifest_terminate_build 0

Summary:	A QT gui for the jack audio daemon
Name:	qjackctl
Version:	1.0.4
Release:	1
License:	GPLv2+
Group:	Sound
Url:	https://sourceforge.net/projects/qjackctl/
Source0:	http://downloads.sourceforge.net/qjackctl/files/%{name}-%{version}.tar.gz
BuildRequires: imagemagick
BuildRequires: qmake-qt6
BuildRequires: qt6-qtbase-theme-gtk3
BuildRequires: qt6-qttools
BuildRequires: vulkan-headers
BuildRequires: cmake(qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(Qt6OpenGLWidgets)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6OpenGL)
BuildRequires: cmake(Qt6OpenGLWidgets)
BuildRequires: cmake(Qt6Xml)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(portaudio-2.0)
BuildRequires: pkgconfig(vulkan)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires: pkgconfig(xkbcommon)
Requires:   jackit

%description
JACK Audio Connection Kit - Qt GUI Interface: A simple Qt application to
control the JACK server daemon.

%files -f %{name}.lang
%doc ChangeLog README
%{_bindir}/%{name}
%{_datadir}/applications/org.rncbc.%{name}.desktop
%{_datadir}/%{name}/palette/*.conf
%{_mandir}/man1/%{name}.1*
%{_iconsdir}/hicolor/*x*/apps/org.rncbc.%{name}.png
%{_iconsdir}/hicolor/scalable/apps/org.rncbc.%{name}.svg
%{_datadir}/metainfo/org.rncbc.%{name}.metainfo.xml

#-----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
%cmake -DCONFIG_QT6=ON

%make_build


%install
%make_install -C build

#Fix .desktop file
desktop-file-edit --add-category="Audio" \
	--add-category="X-OpenMandrivaLinux-Sound" \
	--remove-key="X-SuSE-translate" \
	%{buildroot}%{_datadir}/applications/org.rncbc.%{name}.desktop

# Provide more icons sizes other than 32x32
mkdir -p %{buildroot}%{_iconsdir}/hicolor/512x512/apps/
install -m 0644 src/images/%{name}_512x512.png %{buildroot}%{_iconsdir}/hicolor/512x512/apps/org.rncbc.%{name}.png

for size in 16 48 64 128 256; do
	install -d %{buildroot}%{_iconsdir}/hicolor/${size}x${size}/apps
	convert -resize ${size} src/images/%{name}_512x512.png %{buildroot}%{_iconsdir}/hicolor/${size}x${size}/apps/org.rncbc.%{name}.png
done

%find_lang %{name} --with-qt --with-man
