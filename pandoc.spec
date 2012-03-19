%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define f_pkg_name pandoc
%define h_pkg_name pandoc
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: pandoc
Version: 1.9.1.2
Release: alt1
Summary: Markup conversion tool for markdown

Group: Publishing
License: GPLv2+
Url: http://hackage.haskell.org/package/%name
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: http://hackage.haskell.org/packages/archive/%name/%version/%name-%version.tar.gz

# Automatically added by buildreq on Tue Mar 20 2012
# optimized out: ghc7.4.1 ghc7.4.1-blaze-builder ghc7.4.1-blaze-html ghc7.4.1-common ghc7.4.1-digest ghc7.4.1-hs-bibutils ghc7.4.1-json ghc7.4.1-mtl ghc7.4.1-network ghc7.4.1-pandoc-types ghc7.4.1-parsec ghc7.4.1-regex-base ghc7.4.1-regex-pcre-builtin ghc7.4.1-syb ghc7.4.1-text ghc7.4.1-transformers ghc7.4.1-utf8-string ghc7.4.1-xml ghc7.4.1-zlib libgmp-devel pkg-config
BuildRequires: ghc7.4.1-alex ghc7.4.1-base64-bytestring ghc7.4.1-c2hs ghc7.4.1-citeproc-hs ghc7.4.1-cpphs ghc7.4.1-happy ghc7.4.1-highlighting-kate ghc7.4.1-http ghc7.4.1-random ghc7.4.1-tagsoup ghc7.4.1-temporary ghc7.4.1-texmath ghc7.4.1-zip-archive zlib-devel

%description
Pandoc is a Haskell library for converting from one markup format to another,\
and a command-line tool that uses this library. It can read markdown and\
(subsets of) reStructuredText, HTML, and LaTeX, and it can write markdown,\
reStructuredText, HTML, LaTeX, ConTeXt, Docbook, OpenDocument, ODT, RTF,\
MediaWiki, groff man pages, EPUB, and S5 and Slidy HTML slide shows.

%prep
%setup -q

%build
rm -f man/man1/pandoc.1
runghc Setup configure --bindir=%_bindir --libdir=%_libdir --datadir=%_datadir --docdir=%_docdir
runghc Setup build

%install
runghc Setup copy --destdir=%buildroot

%files
%doc BUGS COPYING COPYRIGHT README
%attr(755,root,root) %_bindir/%name
%_datadir/%name-%version
%_libdir/%name-%version
%attr(644,root,root) %_man1dir/*
%attr(644,root,root) %_man5dir/*

%changelog
* Mon Mar 19 2012 Denis Smirnov <mithraen@altlinux.ru> 1.9.1.2-alt1
- 1.9.1.2

* Wed Aug 03 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8.2.1-alt1
- 1.8.2.1

* Wed Mar 09 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.6.0.1-alt1
- initial from Fedora
