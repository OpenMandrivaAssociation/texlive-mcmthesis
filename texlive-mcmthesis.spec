%global tl_name mcmthesis
%global tl_revision 69538

Name:		texlive-%{tl_name}
Epoch:		1
Version:	6.3.3
Release:	%{tl_revision}.1
Summary:	Template designed for MCM/ICM
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mcmthesis
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mcmthesis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mcmthesis.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mcmthesis.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package offers a template for MCM (The Mathematical Contest in
Modeling) and ICM (The Interdisciplinary Contest in Modeling) for
typesetting the submitted paper.

