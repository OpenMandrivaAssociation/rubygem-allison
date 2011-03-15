# Generated from allison-2.0.3.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	allison

Summary:	A modern, pretty RDoc template
Name:		rubygem-%{rbname}

Version:	2.0.3
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://blog.evanweaver.com/pages/code#allison
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
A modern, pretty RDoc template.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build -f '(cache|contrib)/'

%install
%gem_install

%clean
rm -rf %{buildroot}

%files
%{_bindir}/allison
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/bin
%{ruby_gemdir}/gems/%{rbname}-%{version}/bin/allison
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/cache
%{ruby_gemdir}/gems/%{rbname}-%{version}/cache/*
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/contrib
%{ruby_gemdir}/gems/%{rbname}-%{version}/contrib/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/contrib/Rakefile
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.css
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.js
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}

