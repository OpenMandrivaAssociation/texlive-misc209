# revision 18001
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-misc209
Version:	20111103
Release:	1
Summary:	TeXLive misc209 package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/misc209.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive misc209 package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/misc209/bibmods.sty
%{_texmfdistdir}/tex/latex/misc209/example.sty
%{_texmfdistdir}/tex/latex/misc209/hangcaption.sty
%{_texmfdistdir}/tex/latex/misc209/multind.sty
%{_texmfdistdir}/tex/latex/misc209/portland.sty
%{_texmfdistdir}/tex/latex/misc209/psboxit.sty

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
