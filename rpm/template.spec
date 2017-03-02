Name:           ros-indigo-move-base-to-manip
Version:        1.0.10
Release:        3%{?dist}
Summary:        ROS move_base_to_manip package

Group:          Development/Libraries
License:        See license.txt
URL:            http://wiki.ros.org/move_base_to_manip
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-message-generation
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-move-base-msgs
Requires:       ros-indigo-moveit-ros-planning-interface
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-tf
Requires:       ros-indigo-visualization-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-message-runtime
BuildRequires:  ros-indigo-move-base-msgs
BuildRequires:  ros-indigo-moveit-ros-planning-interface
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-tf
BuildRequires:  ros-indigo-visualization-msgs

%description
Move the robot base until a desired end-effector pose can be reached.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Mar 02 2017 Andy Zelenak <andyz@utexas.edu> - 1.0.10-3
- Autogenerated by Bloom

* Thu Mar 02 2017 Andy Zelenak <andyz@utexas.edu> - 1.0.10-2
- Autogenerated by Bloom

* Thu Mar 02 2017 Andy Zelenak <andyz@utexas.edu> - 1.0.10-1
- Autogenerated by Bloom

* Thu Mar 02 2017 Andy Zelenak <andyz@utexas.edu> - 1.0.10-0
- Autogenerated by Bloom

* Wed Feb 22 2017 Andy Zelenak <andyz@utexas.edu> - 1.0.6-0
- Autogenerated by Bloom

* Tue Feb 21 2017 Andy Zelenak <andyz@utexas.edu> - 1.0.5-0
- Autogenerated by Bloom

* Tue Feb 21 2017 Andy Zelenak <andyz@utexas.edu> - 1.0.3-0
- Autogenerated by Bloom

* Tue Feb 21 2017 Andy Zelenak <andyz@utexas.edu> - 1.0.2-0
- Autogenerated by Bloom

* Tue Feb 21 2017 Andy Zelenak <andyz@utexas.edu> - 1.0.1-1
- Autogenerated by Bloom

* Tue Feb 21 2017 Andy Zelenak <andyz@utexas.edu> - 1.0.1-0
- Autogenerated by Bloom

