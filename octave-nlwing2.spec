%define octpkg nlwing2

# Exclude .oct files from provides
%define __provides_exclude_from ^%{octpkglibdir}/.*.oct$

Summary:	Nonlinear aurodynamic computations for Octave
Name:		octave-%{octpkg}
Version:	1.2.0
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/

BuildRequires:	octave-devel >= 3.0.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
This package allows efficient computation of nonlinear aerodynamic
properties of a wing. It employs 2D section data to build a 3D potential vortex
model of the flow. It uses a robust Euler-Newton method to track the change of
flow vorticity quantities as the angle of attack progresses.

This package is part of unmantained Octave-Forge collection.

%prep
%setup -qcT

%build
%octave_pkg_build -T

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*
#%doc %{octpkg}/NEWS
%doc %{octpkg}/COPYING

