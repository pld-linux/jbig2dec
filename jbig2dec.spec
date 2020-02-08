Summary:	Decoder implementation of the JBIG2 image compression format
Summary(pl.UTF-8):	Implementacja dekodera formatu kompresji obrazu JBIG2
Name:		jbig2dec
Version:	0.17
Release:	1
License:	GPL v2+ with AFPL Ghostscript exception
Group:		Applications/Graphics
#Source0Download: https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/
Source0:	https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs950/%{name}-%{version}.tar.gz
# Source0-md5:	898975d000e004616838a8c6a85dbf39
Patch0:		%{name}-shared.patch
URL:		https://jbig2dec.com/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.7
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
jbig2dec is a decoder implementation of the JBIG2 image compression
format. JBIG2 is designed for lossy or lossless encoding of 'bilevel'
(1-bit monochrome) images at moderately high resolution, and in
particular scanned paper documents. In this domain it is very
efficient, offering compression ratios on the order of 100:1.

This is a decoder only implementation, and currently is in the alpha
stage, meaning it doesn't completely work yet. However, we are
maintaining parity with available encoders, so it is useful for real
work.

The specificication has been published as ISO IEC 14492 and ITU T.88.
These documents completely describe the format and they'll be required
if you want to understand the code and contribute. We prefer the ISO
version, but haven't discovered significant differences between the
two.

JBIG2 also includes the CCITT T.4 and T.6 (group 3 and group 4) fax
encodings, which are documented separately. Their specifications and
T.88 can be obtained from the ITU. The ISO version of JBIG2 can be
obtained through the ISO website.

%description -l pl.UTF-8
jbig2dec to implementacja dekodera formatu kompresji obrazu JBIG2.
JBIG2 został zaprojektowany dla stratnego i bezstratnego kodowania
dwupoziomowych (monochromatycznych, 1-bitowych) obrazów o dość dużej
rozdzielczości, w szczególności skanowanych dokumentów papierowych. W
tej dziedzinie jest bardzo wydajny, oferując współczynniki kompresji
rzędu 100:1.

Jest to implementacja wyłącznie dekodera, aktualnie w stanie alpha, co
oznacza, że jeszcze nie do końca działa. Jednak autorzy utrzymują ją w
parze z dostępnymi koderami, więc jest użyteczna w praktycznych
zastosowaniach.

Specyfikacja została opublikowana jako ISO IEC 14492 oraz ITU T.88. Te
dokumenty całkowicie opisują format i są wymagane do zrozumienia oraz
rozwijania kodu. Autorzy jbig2dec preferują wersję ISO, ale nie
odkryli znaczących różnic między nimi.

JBIG2 obejmuje także kodowania faksowe CCITT T.4 i T.6 (grupa 3 i
grupa 4), które są udokumentowane oddzielnie. Ich specyfikacje oraz
T.88 można zdobyć z ITU. Wersję ISO JBIG2 można zdobyć ze strony WWW
ISO.

%package devel
Summary:	Development files for jbig2dec library
Summary(pl.UTF-8):	Pliki nagłówkowe dla biblioteki jbig2dec
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for jbig2dec library.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla biblioteki jbig2dec.

%package static
Summary:	Static version of jbig2dec library
Summary(pl.UTF-8):	Statyczna wersja biblioteki jbig2dec
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of jbig2dec library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki jbig2dec.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE README
%attr(755,root,root) %{_bindir}/jbig2dec
%attr(755,root,root) %{_libdir}/libjbig2dec.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libjbig2dec.so.0
%{_mandir}/man1/jbig2dec.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libjbig2dec.so
%{_libdir}/libjbig2dec.la
%{_includedir}/jbig2.h
%{_pkgconfigdir}/jbig2dec.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libjbig2dec.a
