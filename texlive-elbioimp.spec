# revision 21758
# category Package
# catalog-ctan /macros/latex/contrib/elbioimp
# catalog-date 2011-03-18 18:22:40 +0100
# catalog-license lppl
# catalog-version 1.2
Name:		texlive-elbioimp
Version:	1.2
Release:	1
Summary:	A LaTeX document class for the Journal of Electrical Bioimpedance
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/elbioimp
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/elbioimp.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/elbioimp.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/elbioimp.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
A new document class for writing articles to the Journal of
Electrical Bioimpedance.

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
%{_texmfdistdir}/tex/latex/elbioimp/elbioimp.cls
%doc %{_texmfdistdir}/doc/latex/elbioimp/Makefile
%doc %{_texmfdistdir}/doc/latex/elbioimp/README
%doc %{_texmfdistdir}/doc/latex/elbioimp/elbioimp-basis.tex
%doc %{_texmfdistdir}/doc/latex/elbioimp/elbioimp.pdf
%doc %{_texmfdistdir}/doc/latex/elbioimp/test-bib.bib
%doc %{_texmfdistdir}/doc/latex/elbioimp/test-ill.png
%doc %{_texmfdistdir}/doc/latex/elbioimp/test1.tex
#- source
%doc %{_texmfdistdir}/source/latex/elbioimp/elbioimp.dtx
%doc %{_texmfdistdir}/source/latex/elbioimp/elbioimp.ins
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
