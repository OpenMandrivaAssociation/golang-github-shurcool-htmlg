# Run tests in check section
%bcond_without check

%global goipath         github.com/shurcooL/htmlg
%global commit          d01228ac9e50f5ab7eee96dcf692117607ef516e

%global common_description %{expand:
htmlg contains helper funcs for generating HTML nodes and rendering them. 
Context-aware escaping is done just like in html/template, making it safe 
against code injection.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Generate and render HTML nodes with context-aware escaping
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(golang.org/x/net/html)
BuildRequires: golang(golang.org/x/net/html/atom)

%if %{with check}
BuildRequires: golang(github.com/shurcooL/component)
%endif

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gitd01228a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 23 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.2.20180420gitd01228a
- Unbootstrap

* Sat Mar 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180420gitd01228a
- First package for Fedora

