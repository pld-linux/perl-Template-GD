#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Template
%define		pnam	GD
Summary:	GD plugins for Template Toolkit - graphics operations
Summary(pl.UTF-8):   Wtyczki GD dla pakietu Template Toolkit - operacje graficzne
Name:		perl-Template-GD
Version:	2.66
Release:	1
# same as perl
License:	GPL v1+ or or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Template/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9052bef9bd799e143990e67422c14b81
URL:		http://search.cpan.org/dist/Template-GD/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl(File::Spec) >= 0.6
BuildRequires:	perl-AppConfig >= 1.52
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-GD >= 1.32
BuildRequires:	perl-GD-Graph >= 1.33
BuildRequires:	perl-GD-Graph3d >= 0.55
BuildRequires:	perl-GD-TextUtil >= 0.80
BuildRequires:	perl-Pod-POM >= 0.1
BuildRequires:	perl-Template-Toolkit >= 2.15
BuildRequires:	perl-Text-Autoformat >= 1.03
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Template-Toolkit >= 2.15
Obsoletes:	perl-Template-Toolkit-Plugin-GD
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GD plugins for Template Toolkit - interface to GD graphics library.

%description -l pl.UTF-8
Wtyczki GD dla pakietu Template Tookit. Stanowią one interfejs do
biblioteki graficznej GD.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
echo "n" | %{__perl} Makefile.PL \
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
%{perl_vendorlib}/Template/Plugin/GD.pm
%{perl_vendorlib}/Template/Plugin/GD
%{_mandir}/man3/*
