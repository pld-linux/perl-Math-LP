#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	LP
Summary:	Math::LP
Summary(pl):	Math::LP
Name:		perl-Math-LP
Version:	0.03
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7807506af8171b95c8d7f536bc341507
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Math-LP-Solve >= 3.02
BuildRequires:	perl-Math-LinearCombination
BuildRequires:	perl-Math-SimpleVariable
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Math-LP-Solve >= 3.02
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Math/LP.pm
%{perl_vendorlib}/Math/LP
%{_mandir}/man3/*
