%global tl_name fmtcount
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.12
Release:	%{tl_revision}.1
Summary:	Display the value of a LaTeX counter in a variety of formats
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fmtcount
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fmtcount.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fmtcount.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fmtcount.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides commands that display the value of a LaTeX counter
in a variety of formats (ordinal, text, hexadecimal, decimal, octal,
binary etc). The package offers some multilingual support;
configurations for use in English (both British and American usage),
French (including Belgian and Swiss variants), German, Italian,
Portuguese and Spanish documents are provided. This package was
originally provided as part of the author's datetime package, but is now
distributed separately.

