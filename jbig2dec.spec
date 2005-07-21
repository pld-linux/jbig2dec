Summary:	Decoder implementation of the JBIG2 image compression format
Summary(pl):	Implementacja dekodera formatu kompresji obrazu JBIG2
Name:		jbig2dec
Version:	0.8
Release:	0.1
License:	GPL with clause allowing linking to AFPL Ghostscript
Group:		Applications
Source0:	http://dl.sourceforge.net/jbig2dec/%{name}-%{version}.tar.gz
# Source0-md5:	cb8f01ae18987f2cebf6854cdd44c7d0
URL:		http://jbig2dec.sourceforge.net/
BuildRequires:	automake
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

%description -l pl
jbig2dec to implementacja dekodera formatu kompresji obrazu JBIG2.
JBIG2 zosta³ zaprojektowany dla stratnego i bezstratnego kodowania
dwupoziomowych (monochromatycznych, 1-bitowych) obrazów o do¶æ du¿ej
rozdzielczo¶ci, w szczególno¶ci skanowanych dokumentów papierowych. W
tej dziedzinie jest bardzo wydajny, oferuj±c wspó³czynniki kompresji
rzêdu 100:1.

Jest to implementacja wy³±cznie dekodera, aktualnie w stanie alpha, co
oznacza, ¿e jeszcze nie do koñca dzia³a. Jednak autorzy utrzymuj± j± w
parze z dostêpnymi koderami, wiêc jest u¿yteczna w praktycznych
zastosowaniach.

Specyfikacja zosta³a opublikowana jako ISO IEC 14492 oraz ITU T.88. Te
dokumenty ca³kowicie opisuj± format i s± wymagane do zrozumienia oraz
rozwijania kodu. Autorzy jbig2dec preferuj± wersjê ISO, ale nie
odkryli znacz±cych ró¿nic miêdzy nimi.

JBIG2 obejmuje tak¿e kodowania faksowe CCITT T.4 i T.6 (grupa 3 i
grupa 4), które s± udokumentowane oddzielnie. Ich specyfikacje oraz
T.88 mo¿na zdobyæ z ITU. Wersjê ISO JBIG2 mo¿na zdobyæ ze strony WWW
ISO.

%package devel
Summary:	Development files for jbig2dec library
Summary(pl):	Pliki nag³ówkowe dla biblioteki jbig2dec
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for jbig2dec library.

%description devel -l pl
Pliki nag³ówkowe dla biblioteki jbig2dec.

%package static
Summary:	Static version of jbig2dec library
Summary(pl):	Statyczna wersja biblioteki jbig2dec
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of jbig2dec library.

%description static -l pl
Statyczna wersja biblioteki jbig2dec.

%prep
%setup -q

%build
#%%{__libtoolize}
%{__aclocal}
%{__autoconf}
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
%doc LICENSE README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
