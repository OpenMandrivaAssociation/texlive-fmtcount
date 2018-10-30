Name:		texlive-fmtcount
Version:	3.05
Release:	3
Summary:	Display the value of a LaTeX counter in a variety of formats
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fmtcount
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fmtcount.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fmtcount.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fmtcount.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides commands that display the value of a LaTeX
counter in a variety of formats (ordinal, text, hexadecimal,
decimal, octal, binary etc). The package offers some
multilingual support; configurations for use in English (both
British and American usage), French (including Belgian and
Swiss variants), German, Italian, Portuguese and Spanish
documents are provided. This package was originally provided as
part of the author's datetime package, but is now distributed
separately.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/scripts/fmtcount
%{_texmfdistdir}/tex/latex/fmtcount
%doc %{_texmfdistdir}/doc/latex/fmtcount
#- source
%doc %{_texmfdistdir}/source/latex/fmtcount

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar scripts tex doc source %{buildroot}%{_texmfdistdir}
