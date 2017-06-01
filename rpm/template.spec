Name:           ros-kinetic-move-base-to-manip
Version:        1.0.17
Release:        0%{?dist}
Summary:        ROS move_base_to_manip package

Group:          Development/Libraries
License:        See license.txt
URL:            http://wiki.ros.org/move_base_to_manip
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-interactive-markers
Requires:       ros-kinetic-message-generation
Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-move-base-msgs
Requires:       ros-kinetic-moveit-core
Requires:       ros-kinetic-moveit-ros-planning-interface
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-tf
Requires:       ros-kinetic-tf2-geometry-msgs
Requires:       ros-kinetic-visualization-msgs
BuildRequires:  eigen3-devel
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-interactive-markers
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-message-runtime
BuildRequires:  ros-kinetic-move-base-msgs
BuildRequires:  ros-kinetic-moveit-core
BuildRequires:  ros-kinetic-moveit-ros-planning-interface
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-tf
BuildRequires:  ros-kinetic-tf2-geometry-msgs
BuildRequires:  ros-kinetic-visualization-msgs

%description
Move the robot base until a desired end-effector pose can be reached.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Thu Jun 01 2017 Andy Zelenak <andyz@utexas.edu> - 1.0.17-0
- Autogenerated by Bloom

* Thu Jun 01 2017 Andy Zelenak <andyz@utexas.edu> - 1.0.16-0
- Autogenerated by Bloom

* Wed May 31 2017 Andy Zelenak <andyz@utexas.edu> - 1.0.15-0
- Autogenerated by Bloom

* Thu May 04 2017 Andy Zelenak <andyz@utexas.edu> - 1.0.13-0
- Autogenerated by Bloom

* Wed Mar 08 2017 Andy Zelenak <andyz@utexas.edu> - 1.0.12-0
- Autogenerated by Bloom

* Mon Mar 06 2017 Andy Zelenak <andyz@utexas.edu> - 1.0.11-0
- Autogenerated by Bloom

* Thu Feb 23 2017 Andy Zelenak <andyz@utexas.edu> - 1.0.6-2
- Autogenerated by Bloom

* Thu Feb 23 2017 Andy Zelenak <andyz@utexas.edu> - 1.0.6-1
- Autogenerated by Bloom

* Thu Feb 23 2017 Andy Zelenak <andyz@utexas.edu> - 1.0.6-0
- Autogenerated by Bloom

* Tue Feb 21 2017 Andy Zelenak <andyz@utexas.edu> - 1.0.3-0
- Autogenerated by Bloom

* Tue Feb 21 2017 Andy Zelenak <andyz@utexas.edu> - 1.0.2-0
- Autogenerated by Bloom

