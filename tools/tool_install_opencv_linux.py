# -*- coding: utf-8 -*-
from .base import BaseTool
from .base import PrintUtils,CmdTask,FileUtils,AptUtils,ChooseTask
from .base import osversion,osarch
from .base import run_tool_file

class Tool(BaseTool):
    def __init__(self):
        self.name = "一键安装opencv4.5.0及opencv_contrib4.5.0"
        self.type = BaseTool.TYPE_INSTALL
        self.autor = 'bingcm'

    def install_nodejs(self):
        PrintUtils.print_info("安装基本依赖")
        CmdTask('sudo apt-get install -y build-essential libgtk2.0-dev libgtk-3-dev libavcodec-dev libavformat-dev libjpeg-dev libswscale-dev libtiff5-dev cmake libeigen3-dev ')
        CmdTask('sudo apt install -y libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev libpng-dev libopenexr-dev libtiff-dev libwebp-dev libgoogle-glog-dev ')
        CmdTask('sudo apt-get install -y python-dev python3-dev libssl-dev')
        PrintUtils.print_info("基本依赖安装完毕，开始下载4.5.0的opencv及opencv_contrib")
        # 根据系统架构下载不同版本的安装包
        # CmdTask('mkdir -p ./env/',os_command=True).run()
        # CmdTask('wget https://gitee.com/opencv/opencv/repository/archive/4.6.0 -O ./env/opencv',os_command=True).run()
        # CmdTask('wget https://gitee.com/opencv/opencv_contrib/repository/archive/4.6.0 -O ./env/opencv_contrib',os_command=True).run()
        PrintUtils.print_info("下载完成,接下来为你解压安装")
        CmdTask("cd env",os_command=True).run()
        CmdTask("unzip opencv",os_command=True).run()
        CmdTask("unzip opencv_contrib",os_command=True).run()
        CmdTask("mv opencv_contrib-4.6.0 opencv-4.6.0",os_command=True).run()
        PrintUtils.print_info("文件解压完毕，开始编译")
        CmdTask("cd opencv-4.6.0/",os_command=True).run()

        CmdTask("cd .cache/",os_command=True).run()
        CmdTask("git clone https://gitee.com/bingcm/opencv_ippiv.git",os_command=True).run()
        CmdTask("mv opencv_ippiv/* ./",os_command=True)
        CmdTask("cd ..",os_command=True).run()

        CmdTask("mkdir build",os_command=True).run()
        CmdTask("cd build",os_command=True).run()



        CmdTask("cmake -D CMAKE_BUILD_TYPE=RELEASE    -D CMAKE_INSTALL_PREFIX=/usr/local    -D ENABLE_NEON=OFF    -D ENABLE_FAST_MATH=ON    -D WITH_GSTREAMER=ON    -D WITH_LIBV4L=ON    -D BUILD_opencv_python2=OFF    -D BUILD_opencv_python3=ON    -D BUILD_TESTS=OFF    -D BUILD_PERF_TESTS=OFF    -D BUILD_EXAMPLES=OFF    -D WITH_TBB=ON    -D BUILD_opencv_world=OFF    -D BUILD_opencv_xfeatures2d=OFF    -D WITH_OPENGL=ON    -D WITH_GTK_2_X=ON    -D OPENCV_ENABLE_NONFREE=ON    -D EIGEN_INCLUDE_PATH='/usr/include/eigen3'    -D OPENCV_EXTRA_MODULES_PATH=../opencv_contrib-4.5.0/modules    -D WITH_XINE=ON    -D WITH_GDAL=ON    -D OPENCV_GENERATE_PKGCONFIG=ON   .. ",os_command=True).run()

        CmdTask("make -j4",os_command=True).run()

    def run(self):
        self.install_nodejs()