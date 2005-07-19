#
Summary:	Decoder implementation of the JBIG2 image compression format
Name:		jbig2dec
Version:	0.8
Release:	0.1
License:	GPL with clause allowing linking to AFPL Ghostscript
Group:		Applications
#Icon:		-
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	cb8f01ae18987f2cebf6854cdd44c7d0
#Patch0:		%{name}-what.patch
URL:		http://jbig2dec.sourceforge.net
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
jbig2dec is a decoder implementation of the JBIG2 image compression format. JBIG2 is designed for lossy or lossless encoding of 'bilevel' (1-bit monochrome) images at moderately high resolution, and in particular scanned paper documents. In this domain it is very efficient, offering compression ratios on the order of 100:1.
This is a decoder only implementation, and currently is in the alpha stage, meaning it doesn't completely work yet. However, we are maintaining parity with available encoders, so it is useful for real work.
The specificication has been published as ISO IEC 14492 and ITU T.88. These documents completely describe the format and they'll be required if you want to understand the code and contribute. We prefer the ISO version, but haven't discovered significant differences between the two.
JBIG2 also includes the CCITT T.4 and T.6 (group 3 and group 4) fax encodings, which are documented separately. Their specifications and T.88 can be obtained from the ITU. The ISO version of JBIG2 can be obtained through the ISO website.

%package devel
Summary:	Development files for jbig2dec library
Summary(pl):	Nag³ówki dla biblioteki jbig2dec
Group:		Development

%description devel
Development files for jbig2dec library.

%description devel -l pl
Nag³ówki dla biblioteki jbig2dec.


%package static
Summary:	Static version of jbig2dec library
Summary(pl):	Statyczna wersjaa biblioteki jbig2dec
Group:		Libraries

%description static
Static version of jbig2dec library.

%description static -l pl
Statyczna wersjaa biblioteki jbig2dec.

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
# create directories if necessary
#install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}

#%files subpackage
#%defattr(644,root,root,755)
#%doc extras/*.gz
#%{_datadir}/%{name}-ext
