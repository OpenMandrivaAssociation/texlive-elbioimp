Name:		texlive-elbioimp
Version:	21758
Release:	1
Summary:	A LaTeX document class for the Journal of Electrical Bioimpedance
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/elbioimp
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/elbioimp.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/elbioimp.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/elbioimp.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
