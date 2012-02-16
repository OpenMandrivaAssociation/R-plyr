%bcond_without bootstrap
%global packname  plyr
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.7.1
Release:          1
Summary:          Tools for splitting, applying and combining data
Group:            Sciences/Mathematics
License:          MIT
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
%if %{with bootstrap}
Requires:         R-abind R-tcltk R-foreach R-itertools R-iterators 
%else
Requires:         R-abind R-testthat R-tcltk R-foreach R-itertools R-iterators 
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
%if %{with bootstrap}
BuildRequires:    R-abind R-tcltk R-foreach R-itertools R-iterators 
%else
BuildRequires:    R-abind R-testthat R-tcltk R-foreach R-itertools R-iterators 
%endif

%description
plyr is a set of tools that solves a common set of problems: you need to
break a big problem down into manageable pieces, operate on each pieces
and then put all the pieces back together.  For example, you might want to
fit a model to each spatial location or time point in your study,
summarise data by panels or collapse high-dimensional arrays to simpler
summary statistics. The development of plyr has been generously supported
by BD (Becton Dickinson).

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/tests
