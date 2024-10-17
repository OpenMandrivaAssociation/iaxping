Summary:	IAX ping tool
Name:		iaxping
Version:	0
Release:	7
License:	BSD
Group:		Monitoring
URL:		https://www.loudhush.ro/tools/
Source0:	http://www.loudhush.ro/opencms/opencms/loudhush/tools/iaxping.c.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Tool to ping an IAX target (checks network connectivity). hacked from the perl
ping tool availble on http://www.voip-info.org/wiki-IAX

%prep

%setup -q -c -T

bzcat %{SOURCE0} > %{name}.c

%build

gcc %{optflags} -o %{name} %{name}.c

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}

install -m0755 %{name} %{buildroot}%{_bindir}/%{name}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root,)
%{_bindir}/%{name}




%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0-6mdv2011.0
+ Revision: 619519
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0-5mdv2010.0
+ Revision: 429486
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0-4mdv2009.0
+ Revision: 247141
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0-2mdv2008.1
+ Revision: 140755
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Mar 29 2007 Olivier Blin <oblin@mandriva.com> 0-2mdv2007.1
+ Revision: 149953
- rebuild because of binary package loss

* Wed Mar 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0-1mdv2007.1
+ Revision: 147620
- Import iaxping

* Thu Jun 15 2006 Oden Eriksson <oeriksson@mandriva.com> 0-1mdv2007.0
- initial Mandriva package

