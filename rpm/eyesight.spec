Name:           eyesight
Summary:        Hawaii desktop image viewer
Version:        0.1.2
Release:        1
Group:          Applications/System
License:        GPLv2+
URL:            https://github.com/mauios/eyesight
Source:         %{name}-%{version}.tar.xz

BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qtwidgets-devel
BuildRequires:  qt5-qtprintsupport-devel
BuildRequires:  cmake
BuildRequires:  bzip2-devel
BuildRequires:  qt5-qttools-linguist
BuildRequires:  desktop-file-utils
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig


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


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


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
