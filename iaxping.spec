Summary:	IAX ping tool
Name:		iaxping
Version:	0
Release:	%mkrel 6
License:	BSD
Group:		Monitoring
URL:		http://www.loudhush.ro/tools/
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


