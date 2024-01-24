Name:		texlive-mcmthesis
Version:	69538
Release:	1
Summary:	Template designed for MCM/ICM
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mcmthesis
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mcmthesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mcmthesis.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mcmthesis.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package offers a template for MCM (The Mathematical Contest
in Modeling) and ICM (The Interdisciplinary Contest in
Modeling) for typesetting the submitted paper.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/mcmthesis
%{_texmfdistdir}/tex/latex/mcmthesis
%doc %{_texmfdistdir}/doc/latex/mcmthesis

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
