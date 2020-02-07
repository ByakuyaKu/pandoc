%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define ghc_namever %hsc_name%hsc_version
%define f_pkg_name pandoc
%define h_pkg_name pandoc
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: pandoc
Version: 2.7.3
Release: alt1
Summary: Markup conversion tool for markdown

Group: Publishing
License: GPLv2+
Url: http://hackage.haskell.org/package/%name

Source: http://hackage.haskell.org/packages/archive/%name/%version/%name-%version.tar.gz
Source100: pandoc.watch

# Automatically added by buildreq on Mon Dec 24 2012
# optimized out: ghc7.6.1 ghc7.6.1-blaze-builder ghc7.6.1-blaze-html ghc7.6.1-blaze-markup ghc7.6.1-common ghc7.6.1-digest ghc7.6.1-extensible-exceptions ghc7.6.1-hexpat ghc7.6.1-hs-bibutils ghc7.6.1-http ghc7.6.1-json ghc7.6.1-list ghc7.6.1-mtl ghc7.6.1-network ghc7.6.1-pandoc-types ghc7.6.1-parsec ghc7.6.1-regex-base ghc7.6.1-regex-pcre-builtin ghc7.6.1-syb ghc7.6.1-text ghc7.6.1-transformers ghc7.6.1-utf8-string ghc7.6.1-xml ghc7.6.1-zlib libgmp-devel pkg-config
BuildRequires: %ghc_namever-base64-bytestring
BuildRequires: %ghc_namever-random
BuildRequires: %ghc_namever-tagsoup
BuildRequires: %ghc_namever-temporary
BuildRequires: %ghc_namever-texmath
BuildRequires: %ghc_namever-zip-archive
BuildRequires: %ghc_namever-data-default
BuildRequires: zlib-devel

BuildRequires: ghc%ghc_version-glob
BuildRequires: ghc%ghc_version-http
BuildRequires: ghc%ghc_version-hsyaml
BuildRequires: ghc%ghc_version-juicypixels
BuildRequires: ghc%ghc_version-sha
BuildRequires: ghc%ghc_version-aeson
BuildRequires: ghc%ghc_version-aeson-pretty
BuildRequires: ghc%ghc_version-attoparsec
BuildRequires: ghc%ghc_version-blaze-html
BuildRequires: ghc%ghc_version-blaze-markup
BuildRequires: ghc%ghc_version-case-insensitive
BuildRequires: ghc%ghc_version-cmark-gfm
BuildRequires: ghc%ghc_version-doctemplates
BuildRequires: ghc%ghc_version-exceptions
BuildRequires: ghc%ghc_version-haddock-library
BuildRequires: ghc%ghc_version-hslua
BuildRequires: ghc%ghc_version-hslua-module-text
BuildRequires: ghc%ghc_version-hslua-module-system
BuildRequires: ghc%ghc_version-http-client
BuildRequires: ghc%ghc_version-http-client-tls
BuildRequires: ghc%ghc_version-http-types
BuildRequires: ghc%ghc_version-ipynb
BuildRequires: ghc%ghc_version-network
BuildRequires: ghc%ghc_version-network-uri
BuildRequires: ghc%ghc_version-pandoc-types
BuildRequires: ghc%ghc_version-safe
BuildRequires: ghc%ghc_version-scientific
BuildRequires: ghc%ghc_version-skylighting
BuildRequires: ghc%ghc_version-split
BuildRequires: ghc%ghc_version-syb
BuildRequires: ghc%ghc_version-unicode-transforms
BuildRequires: ghc%ghc_version-unordered-containers
BuildRequires: ghc%ghc_version-vector
BuildRequires: ghc%ghc_version-xml
BuildRequires: ghc%ghc_version-zlib


%package -n ghc%ghc_version-pandoc
Summary: Markup conversion tool for markdown
Group: Publishing

%description
Pandoc is a Haskell library for converting from one markup format to
another, and a command-line tool that uses this library. It can read
markdown and (subsets of) reStructuredText, HTML, and LaTeX, and it can
write markdown, reStructuredText, HTML, LaTeX, ConTeXt, Docbook,
OpenDocument, ODT, RTF, MediaWiki, groff man pages, EPUB, and S5 and
Slidy HTML slide shows.

%description -n ghc%ghc_version-pandoc
Pandoc is a Haskell library for converting from one markup format to
another, and a command-line tool that uses this library. It can read
markdown and (subsets of) reStructuredText, HTML, and LaTeX, and it can
write markdown, reStructuredText, HTML, LaTeX, ConTeXt, Docbook,
OpenDocument, ODT, RTF, MediaWiki, groff man pages, EPUB, and S5 and
Slidy HTML slide shows.

%prep
%setup -q

%build
%hs_configure2 --disable-split-objs
%hs_build

%install
%hs_install
%hs_gen_filelist
grep %_libdir %name-files.all > %name-files.lib

ln -s pandoc %buildroot%_bindir/hsmarkdown
install -m 0644 -p -D man/pandoc.1 %buildroot%_man1dir/pandoc.1

%files -n ghc%ghc_version-pandoc -f %name-files.lib

%files
%_bindir/*
%_man1dir/*
%_datadir/*

%changelog
* Wed Feb 07 2020 Rodion Philippov <toga@altlinux.org> 2.7.3-alt1
- Update to 2.7.3 on ghc-8.6.4

* Mon Mar 13 2017 Denis Smirnov <mithraen@altlinux.ru> 1.11.1-alt2
- move pandoc haskell lib to separate subpackage (ALT 31654)

* Tue Jun 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.11.1-alt1.1
- NMU: updated watch file

* Mon May 06 2013 Denis Smirnov <mithraen@altlinux.ru> 1.11.1-alt1
- 1.11.1

* Fri Feb 08 2013 Denis Smirnov <mithraen@altlinux.ru> 1.9.4.5-alt2
- cleanup spec

* Mon Dec 24 2012 Denis Smirnov <mithraen@altlinux.ru> 1.9.4.5-alt1
- 1.9.4.5

* Sun Sep 23 2012 Denis Smirnov <mithraen@altlinux.ru> 1.9.4.2-alt3
- add watch-file for gear-cronbuild

* Sat Jul 28 2012 Denis Smirnov <mithraen@altlinux.ru> 1.9.4.2-alt1
- 1.9.4.2

* Wed May 02 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.9.2-alt1
- 1.9.2

* Mon Mar 19 2012 Denis Smirnov <mithraen@altlinux.ru> 1.9.1.2-alt1
- 1.9.1.2

* Wed Aug 03 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8.2.1-alt1
- 1.8.2.1

* Wed Mar 09 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.6.0.1-alt1
- initial from Fedora
