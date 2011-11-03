# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/fmtcount
# catalog-date 2009-10-02 20:24:27 +0200
# catalog-license lppl1.3
# catalog-version 1.31
Name:		texlive-fmtcount
Version:	1.31
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
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package fmtcount.sty provides commands that display the
value of a LaTeX counter in a variety of formats (ordinal,
text, hexadecimal, decimal, octal, binary etc). The package
offers some multilingual support; configurations for use in
English (both British and American usage), French, German,
Portuguese and Spanish documents are provided. This package was
originally provided as part of the author's datetime package,
but is now distributed separately.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fmtcount/fc-UKenglish.def
%{_texmfdistdir}/tex/latex/fmtcount/fc-USenglish.def
%{_texmfdistdir}/tex/latex/fmtcount/fc-british.def
%{_texmfdistdir}/tex/latex/fmtcount/fc-english.def
%{_texmfdistdir}/tex/latex/fmtcount/fc-french.def
%{_texmfdistdir}/tex/latex/fmtcount/fc-german.def
%{_texmfdistdir}/tex/latex/fmtcount/fc-italian.def
%{_texmfdistdir}/tex/latex/fmtcount/fc-portuges.def
%{_texmfdistdir}/tex/latex/fmtcount/fc-spanish.def
%{_texmfdistdir}/tex/latex/fmtcount/fmtcount.sty
%doc %{_texmfdistdir}/doc/latex/fmtcount/CHANGES
%doc %{_texmfdistdir}/doc/latex/fmtcount/README
%doc %{_texmfdistdir}/doc/latex/fmtcount/fc-lang.tex
%doc %{_texmfdistdir}/doc/latex/fmtcount/fc-samp.tex
%doc %{_texmfdistdir}/doc/latex/fmtcount/fmtcount-manual.html
%doc %{_texmfdistdir}/doc/latex/fmtcount/fmtcount.pdf
#- source
%doc %{_texmfdistdir}/source/latex/fmtcount/fmtcount.dtx
%doc %{_texmfdistdir}/source/latex/fmtcount/fmtcount.ins
%doc %{_texmfdistdir}/source/latex/fmtcount/fmtcount.perl
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
