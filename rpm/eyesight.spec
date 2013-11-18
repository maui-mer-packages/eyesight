Name:           eyesight
Summary:        Hawaii desktop image viewer
Version:        0.1.2
Release:        1
Group:          Applications/System
License:        GPLv2+
URL:            https://github.com/mauios/eyesight
Source:         %{name}-%{version}.tar.xz

BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  cmake
BuildRequires:  bzip2-devel
BuildRequires:  qt5-qttools-linguist
BuildRequires:  desktop-file-utils


%description
Image viewer for the Hawaii desktop.


%prep
%setup -q -n %{name}-%{version}/upstream


%build
%cmake . \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo
make %{?jobs:-j%jobs}


%install
rm -rf %{buildroot}
%make_install

desktop-file-install --delete-original              \
  --dir %{buildroot}%{_datadir}/applications        \
   %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%defattr(-,root,root,-)
%{_bindir}/eyesight
%{_datadir}/applications/eyesight.desktop
%dir %{_datadir}/eyesight
%dir %{_datadir}/eyesight/translations
# These short-named translations probably need renaming upstream, since they
# are not picked up by find_lang
%{_datadir}/eyesight/translations/??.qm
%doc COPYING
%doc README.md
