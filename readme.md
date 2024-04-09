## 自定义日历
--
### 一、简介
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;一个简单的PYTHON模块，基于自定义数据来创建创建个性化的日历；可以配置节日，假日，工作日或纪念日；当前默认内置中国的节假日信息；任何人都可以基于简单的规则，创建属于自已的日历；  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A simple module that creates personalized calendars based on custom data; Holidays, working days, or anniversaries can be configured; The current default built-in holiday information for China; Anyone can create their own calendar based on simple rules;

- 版本支持 - SUPPORT ：Python >= 3.5  

--
### 二、安装 - INSTALL 
**2.1 WHL安装 - From customcal_xxx.whl**
```
# 下载"customcal_xxx.whl"
# Download "customcal_xxx.whl"

# 安装 - Install
python -m pip install customcal_xxx.whl

# 卸载 - Uninstall
python -m pip uninstall customcal
```
**2.2 源码安装 - Using source code**
```
# 依赖 - Dependencies
python -m pip install setuptools wheel
python -m pip install setuptools wheel -i https://mirrors.aliyun.com/pypi/simple/

# 编译 - Build
python setup.py bdist_wheel

# 安装 - Install
python -m pip install dist/customcal_xxx.whl

# 卸载 - Uninstall
python -m pip uninstall customcal
```

--
### 三、使用方法 - Use  
- [基础用例](doc/1.basicUsage.md) [[ Basic Use Cases ](doc/1.basicUsage_en.md)]
- [实例选项](doc/2.instanceOptions.md) [[ Instance Options ](doc/2.instanceOptions_en.md)]
- [扩展选项](doc/3.extendedOption.md) [[ Extended Options ](doc/3.extendedOption_en.md)]
- [自定义数据文件](doc/4.customDataFile.md) [[ Custom Data File ](doc/4.customDataFile_en.md)]

--
### 常见问题：

1. 等待发现中...