# revision 28068
# category Package
# catalog-ctan /macros/latex/contrib/fmtcount
# catalog-date 2012-10-24 16:07:36 +0200
# catalog-license lppl1.3
# catalog-version 2.02
Name:		texlive-fmtcount
Version:	2.02
Release:	1
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
%{_texmfdistdir}/scripts/fmtcount/fmtcount.perl
%{_texmfdistdir}/tex/latex/fmtcount/fc-UKenglish.def
%{_texmfdistdir}/tex/latex/fmtcount/fc-USenglish.def
%{_texmfdistdir}/tex/latex/fmtcount/fc-american.def
%{_texmfdistdir}/tex/latex/fmtcount/fc-british.def
%{_texmfdistdir}/tex/latex/fmtcount/fc-english.def
%{_texmfdistdir}/tex/latex/fmtcount/fc-francais.def
%{_texmfdistdir}/tex/latex/fmtcount/fc-french.def
%{_texmfdistdir}/tex/latex/fmtcount/fc-frenchb.def
%{_texmfdistdir}/tex/latex/fmtcount/fc-german.def
%{_texmfdistdir}/tex/latex/fmtcount/fc-germanb.def
%{_texmfdistdir}/tex/latex/fmtcount/fc-italian.def
%{_texmfdistdir}/tex/latex/fmtcount/fc-ngerman.def
%{_texmfdistdir}/tex/latex/fmtcount/fc-ngermanb.def
%{_texmfdistdir}/tex/latex/fmtcount/fc-portuges.def
%{_texmfdistdir}/tex/latex/fmtcount/fc-spanish.def
%{_texmfdistdir}/tex/latex/fmtcount/fcnumparser.sty
%{_texmfdistdir}/tex/latex/fmtcount/fcprefix.sty
%{_texmfdistdir}/tex/latex/fmtcount/fmtcount.sty
%doc %{_texmfdistdir}/doc/latex/fmtcount/CHANGES
%doc %{_texmfdistdir}/doc/latex/fmtcount/README
%doc %{_texmfdistdir}/doc/latex/fmtcount/fc-frlargenum.tex
%doc %{_texmfdistdir}/doc/latex/fmtcount/fc-lang.tex
%doc %{_texmfdistdir}/doc/latex/fmtcount/fc-samp.tex
%doc %{_texmfdistdir}/doc/latex/fmtcount/fmtcount.pdf
#- source
%doc %{_texmfdistdir}/source/latex/fmtcount/fmtcount.dtx
%doc %{_texmfdistdir}/source/latex/fmtcount/fmtcount.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar scripts tex doc source %{buildroot}%{_texmfdistdir}
