## 自定义日历
--
### 一、简介
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;一个简单的PYTHON模块，基于自定义数据来创建创建个性化的日历；可以配置节日，假日，工作日或纪念日；当前默认内置中国的节假日信息；任何人都可以基于简单的规则，创建属于自已的日历；
- 版本支持：Python >= 3.5  

--
### 二、安装
**2.1 源码安装**
```
# 安装相关工具
python -m pip install setuptools wheel -i https://mirrors.aliyun.com/pypi/simple/

# 编译
python setup.py bdist_wheel

# 安装
python -m pip install dist/customcal_xxx.whl

# 卸载
python -m pip uninstall customcal
```

--
### 三、使用方法  
- [基础用例](doc/1.basicUsage.md)
- [实例选项](doc/2.instanceOptions_I.md)
- [扩展选项](doc/3.extendedOption.md)
- [自定义数据文件](doc/4.customDataFile.md)

--
### 常见问题：

1. 等待发现中...