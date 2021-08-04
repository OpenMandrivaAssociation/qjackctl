#define debug_package          %{nil}
%define _empty_manifest_terminate_build 0

Summary:    A QT gui for the jack audio daemon
Name:       qjackctl
Version:    0.9.4
Release:    1

License:    GPLv2+
Group:      Sound
URL:        http://sourceforge.net/projects/qjackctl/
Source:     http://downloads.sourceforge.net/qjackctl/files/%{name}-%{version}.tar.gz
BuildRequires:	imagemagick
BuildRequires:  qmake5
BuildRequires:  qt5-qtchooser
BuildRequires:	qt5-qttools
BuildRequires:  qt5-linguist
BuildRequires:  qt5-linguist-tools
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(portaudio-2.0)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	pkgconfig(Qt5Xml)

Requires:   jackit

%description
JACK Audio Connection Kit - Qt GUI Interface: A simple Qt application to
control the JACK server daemon.

%prep
%setup -q

%build
%configure \
	--enable-jack-version \
	--enable-debug

%make_build

%install
%make_install

#menu
desktop-file-install --vendor="" \
  --add-category="Audio" \
  --add-category="X-MandrivaLinux-Sound" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%files
%doc AUTHORS ChangeLog README TODO
%{_mandir}/man1/*
%{_bindir}/%name
%{_iconsdir}/hicolor/*x*/apps/%name.png
%{_iconsdir}/hicolor/scalable/apps/qjackctl.svg
%{_datadir}/applications/*.desktop
%{_datadir}/qjackctl
%{_mandir}/fr/man1/qjackctl.1.*
%{_datadir}/metainfo/%{name}.appdata.xml

%changelog
* Fri May 18 2012 Frank Kober <emuse@mandriva.org> 0.3.9-1
+ Revision: 799563
- new version 0.3.9

* Fri Dec 23 2011 Frank Kober <emuse@mandriva.org> 0.3.8-2
+ Revision: 744720
- Disable broken qmake qt version check for now
- rebuild to enable Jack Session with jack 1.9.8

* Sat Jul 02 2011 Frank Kober <emuse@mandriva.org> 0.3.8-1
+ Revision: 688537
- new version 0.3.8 (featuring jack-session versioning)

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.6-2mdv2011.0
+ Revision: 614674
- the mass rebuild of 2010.1 packages

* Wed Mar 10 2010 Frank Kober <emuse@mandriva.org> 0.3.6-1mdv2010.1
+ Revision: 517281
- new version 0.3.6

* Thu Nov 26 2009 Jérôme Brenier <incubusss@mandriva.org> 0.3.5-1mdv2010.1
+ Revision: 470272
- new version 0.3.5
- drop P0 (merged upstream)

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.3.4-3mdv2010.0
+ Revision: 442557
- rebuild

* Thu Jan 01 2009 trem <trem@mandriva.org> 0.3.4-2mdv2009.1
+ Revision: 323187
- fix licence (rpmlint warning)
- add patch to fix the save of profile without any change

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Sat Dec 06 2008 trem <trem@mandriva.org> 0.3.4-1mdv2009.1
+ Revision: 311185
- new release 0.3.4

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.3.2-4mdv2009.0
+ Revision: 259953
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.3.2-3mdv2009.0
+ Revision: 247774
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Dec 28 2007 Austin Acton <austin@mandriva.org> 0.3.2-1mdv2008.1
+ Revision: 138718
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Aug 05 2007 Oden Eriksson <oeriksson@mandriva.com> 0.3.1a-2mdv2008.0
+ Revision: 59093
- fix the menu

* Tue Jul 31 2007 Oden Eriksson <oeriksson@mandriva.com> 0.3.1a-1mdv2008.0
+ Revision: 57218
- 0.3.1a

* Wed Jul 11 2007 Austin Acton <austin@mandriva.org> 0.3.0-1mdv2008.0
+ Revision: 51160
- buildrequires desktop-file-utils
- new version
- yay for qt4
- drop my beloved jackwrapper (I will always love you)

* Sat Jul 07 2007 Austin Acton <austin@mandriva.org> 0.2.23-1mdv2008.0
+ Revision: 49293
- drop debian menu
- use bundled desktop file
- new version

* Thu Jun 14 2007 Austin Acton <austin@mandriva.org> 0.2.22-1mdv2008.0
+ Revision: 39339
- new version

* Fri May 25 2007 Austin Acton <austin@mandriva.org> 0.2.21-3mdv2008.0
+ Revision: 31109
- oops, fix buildrequires for x86_64

* Wed May 23 2007 Austin Acton <austin@mandriva.org> 0.2.21-2mdv2008.0
+ Revision: 30372
- buildrequires alsa to force linking (closes #30881)


* Thu Mar 15 2007 Austin Acton <austin@mandriva.org> 0.2.21-1mdv2007.1
+ Revision: 144158
- new release
- Import qjackctl

* Mon Sep 11 2006 Emmanuel Andry <eandry@mandriva.org> 0.2.20.10-0.20060518.2mdv2007.0
- xdg menu

* Fri May 19 2006 Austin Acton <austin@mandriva.org> 0.2.20.10-0.20060518.1mdk
- go cvs for freebob support
- mkrel

* Thu Mar 09 2006 Lenny Cartier <lenny@mandriva.com> 0.2.20-1mdk
- 0.2.20

* Fri Mar 03 2006 Austin Acton <austin@mandriva.org> 0.2.19a-1mdk
- New release 0.2.19a

* Mon Nov 21 2005 Lenny Cartier <lenny@mandriva.com> 0.2.19-1mdk
- 0.2.19

* Sat Sep 24 2005 Couriousous <couriousous@mandriva.org> 0.2.18-2mdk
- Fix x86_64 build

* Wed Jul 20 2005 Austin Acton <austin@mandriva.org> 0.2.18-1mdk
- New release 0.2.18

* Sat Jun 18 2005 Lenny Cartier <lenny@mandriva.com> 0.2.17-1mdk
- 0.2.17

* Wed Jun 15 2005 Austin Acton <austin@mandriva.org> 0.2.16-1mdk
- New release 0.2.16

* Wed Feb 09 2005 Lenny Cartier <lenny@mandrakesoft.com> 0.2.15a-1mdk
- 0.2.15a

* Sun Feb 06 2005 Austin Acton <austin@mandrake.org> 0.2.15-1mdk
- 0.2.15

* Mon Jan 24 2005 Lenny Cartier <lenny@mandrakesoft.com> 0.2.14-1mdk
- 0.2.14

* Sun Nov 21 2004 Austin Acton <austin@mandrake.org> 0.2.13-1mdk
- 0.2.13

* Wed Oct 13 2004 Austin Acton <austin@mandrake.org> 0.2.12a-1mdk
- 0.2.12a

* Sat Oct 09 2004 Austin Acton <austin@mandrake.org> 0.2.12-1mdk
- 0.2.12

* Sat Sep 11 2004 Austin Acton <austin@mandrake.org> 0.2.11-1mdk
- 0.2.11

* Tue Jul 20 2004 Austin Acton <austin@mandrake.org> 0.2.9-2mdk
- add jackwrapper

* Mon Jul 05 2004 Austin Acton <austin@mandrakesoft.com> 0.2.9-1mdk
- 0.2.9

* Mon Apr 05 2004 Austin Acton <austin@mandrake.org> 0.2.7-1mdk
- 0.2.7



