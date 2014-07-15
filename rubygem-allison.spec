# Generated from allison-2.0.3.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	allison

Summary:	A modern, pretty RDoc template
Name:		rubygem-%{rbname}
Version:	2.0.3
Release:	3
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
mkdir -p .%{ruby_gemdir}
gem install -V --local --install-dir .%{ruby_gemdir} \
               --force --rdoc %{SOURCE0}

%install
mkdir -p %{buildroot}%{ruby_gemdir}
mkdir -p %{buildroot}%{_bindir}
cp -rf .%{ruby_gemdir}/* %{buildroot}%{ruby_gemdir}
pushd %{buildroot}
ln -s ../../%{ruby_gemdir}/gems/%{rbname}-%{version}/bin/allison ./%{_bindir}/allison
popd


%files
%{_bindir}/allison
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%{ruby_gemdir}/bin/allison
%{ruby_gemdir}/cache/*
%{ruby_gemdir}/gems/%{rbname}-%{version}/*
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}
