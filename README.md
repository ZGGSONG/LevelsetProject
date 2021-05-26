## INTRODUCE

LevelSet SoftWare

## How To Use It?

1. 安装环境
```shell
brew install python redis
```
2. 安装依赖
```shell
pip install -r requirements.txt
```
3. 配置redis

    在`src`-`redis_drive.py`和`redis_drive_db1.py`分别配置你自己的redis信息以连接数据库

4. 运行`main.py`即可


<details>
<summary>s</summary>

## 开发过程

> 参考文献：CV、LBF、DRLSE模型、Redis、PSNR、SSIM

- 目录结构
```
.
├── levelsetproject
└── src
    ├── main.py
    ├── img
    ├── lsca
    └── relevantinfo
        ├── cv
        ├── drlse
        └── rsf
```

- [x] **基本需求**
    - [x] 选择图像
    - [x] 输入参数
    - [x] 调用算法输出分割图像 
---
- [x] **新增需求**
    - [x] 输出多张分割图像
    - [x] 资料整合使用文件管理器打开    
    - [x] 参数意义
    - [ ] 分割效果评价指标
        - PSNR(峰值信噪比)
        - SSIM(结构相似性)

</details>