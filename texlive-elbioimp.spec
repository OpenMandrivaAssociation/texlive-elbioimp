# revision 21758
# category Package
# catalog-ctan /macros/latex/contrib/elbioimp
# catalog-date 2011-03-18 18:22:40 +0100
# catalog-license lppl
# catalog-version 1.2
Name:		texlive-elbioimp
Version:	1.2
Release:	9
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

%description
A new document class for writing articles to the Journal of
Electrical Bioimpedance.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2-2
+ Revision: 751390
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.2-1
+ Revision: 718317
- texlive-elbioimp
- texlive-elbioimp
- texlive-elbioimp
- texlive-elbioimp

