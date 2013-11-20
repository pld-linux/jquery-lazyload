%define		plugin	lazyload
Summary:	jQuery plugin for lazy loading images
Name:		jquery-%{plugin}
Version:	1.9.1
Release:	1
License:	MIT
Group:		Applications/WWW
Source0:	https://github.com/tuupola/jquery_lazyload/archive/%{version}/%{plugin}-%{version}.tar.gz
# Source0-md5:	7ecf440856495018d0d26c8a7660ac65
URL:		http://www.appelsiini.net/projects/lazyload
Requires:	jquery
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
Lazy Load delays loading of images in long web pages. Images outside
of viewport wont be loaded before user scrolls to them. This is
opposite of image preloading.

Using Lazy Load on long web pages containing many large images makes
the page load faster. Browser will be in ready state after loading
visible images. In some cases it can also help to reduce server load.

Lazy Load is inspired by YUI ImageLoader Utility by Matt Mlinac.

%prep
%setup -qn jquery_%{plugin}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_examplesdir}/%{name}-%{version}}

cp -p jquery.%{plugin}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
cp -p jquery.%{plugin}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.js
ln -s %{plugin}-%{version}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.src.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.min.js

# package also scrollstop in this package
cp -p jquery.scrollstop.min.js $RPM_BUILD_ROOT%{_appdir}/scrollstop-%{version}.min.js
cp -p jquery.scrollstop.js $RPM_BUILD_ROOT%{_appdir}/scrollstop-%{version}.js
ln -s scrollstop-%{version}.js $RPM_BUILD_ROOT%{_appdir}/scrollstop.src.js
ln -s scrollstop-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/scrollstop.js
ln -s scrollstop-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/scrollstop.min.js

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.textile
%{_appdir}
