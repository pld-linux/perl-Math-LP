#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Math
%define		pnam	LP
%include	/usr/lib/rpm/macros.perl
Summary:	Math::LP
Summary(pl.UTF-8):	Math::LP
Name:		perl-Math-LP
Version:	0.03
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7807506af8171b95c8d7f536bc341507
URL:		http://search.cpan.org/dist/Math-LP/
BuildRequires:	perl-Math-LP-Solve >= 3.02
BuildRequires:	perl-Math-LinearCombination
BuildRequires:	perl-Math-SimpleVariable
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Math-LP-Solve >= 3.02
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl.UTF-8

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

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
