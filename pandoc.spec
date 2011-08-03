%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define f_pkg_name pandoc
%define h_pkg_name pandoc
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: pandoc
Version: 1.8.2.1
Release: alt1
Summary: Markup conversion tool for markdown

Group: Publishing
License: GPLv2+
Url: http://hackage.haskell.org/package/%name
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: http://hackage.haskell.org/packages/archive/%name/%version/%name-%version.tar.gz

BuildRequires: ghc, ghc-doc, ghc-prof, ghc-http, ghc-network, ghc-mtl, ghc-parsec, ghc-syb, ghc-utf8-string, ghc-xml, ghc-texmath, ghc-xhtml, ghc-zip-archive, ghc-texmath, ghc-tagsoup, ghc-dlist, ghc-citeproc-hs, ghc-json, ghc-base64-bytestring
BuildRequires(pre): rpm-build-haskell

%description
Pandoc is a Haskell library for converting from one markup format to another,\
and a command-line tool that uses this library. It can read markdown and\
(subsets of) reStructuredText, HTML, and LaTeX, and it can write markdown,\
reStructuredText, HTML, LaTeX, ConTeXt, Docbook, OpenDocument, ODT, RTF,\
MediaWiki, groff man pages, EPUB, and S5 and Slidy HTML slide shows.

%prep
%setup -q

%build
runghc Setup configure --bindir=%_bindir --libdir=%_libdir --datadir=%_datadir --docdir=%_docdir
runghc Setup build

%install
runghc Setup copy --destdir=%buildroot

%files
%doc BUGS COPYING COPYRIGHT README
%attr(755,root,root) %_bindir/%name
%attr(755,root,root) %_bindir/markdown2pdf
%_datadir/%name-%version
%_libdir/%name-%version
%attr(644,root,root) %_man1dir/*
%attr(644,root,root) %_man5dir/*

%changelog
* Wed Aug 03 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8.2.1-alt1
- 1.8.2.1

* Wed Mar 09 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.6.0.1-alt1
- initial from Fedora
