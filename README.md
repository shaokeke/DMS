### 框架
后端框架：django、sanic、flask

数据库：mysql、mongodb

web服务器：nginx+uwsgi

### 首页展示
1. 大图总数
2. 大图中诊断结果标签数量及占比
3. 大图中片源数量及占比
4. 大图中20X/40X倍数数量及占比

### 病例数据
1.查询
- 查询一条病例数据
    - 通过?id=的方式或/id/的方式
- 查询病例列表
- 分页功能
- 搜索功能：精确搜索/模糊搜索
- 查找病例中出现重复的病理号及重复的次数

2.新增
- 新增一条病例记录

3.修改
- 修改一条更名记录

4.删除
- 删除一条病例记录
- 批量删除

5.文件上传功能
- 支持上传csv,excel格式的文件

6.文件下载功能
- 支持下载csv,excel格式的文件

### 大图数据
1.查询
- 查询一条大图数据
    - 通过?id=的方式或/id/的方式
- 查询大图列表
- 分页功能
- 搜索功能
- 查找大图中出现重复的文件名及重复的次数

2.更新
- 更新数据库中的大图数据
- 修改一条大图数据(只能修改文件名和病理号)
    - 修改文件名会同步修改data_samba中大图的文件名
    - 修改病理号会判断是否与文件名保持一致

3.删除
- 逻辑删除一条大图数据

4.文件下载功能
- 支持下载csv,excel格式的文件

5.显示大图
- 瓦片功能
- 显示切片标签图

6.监控功能
- 自动监控0TIFF下大图的操作，被修改，剪切，删除同步到dms

### 文件更名数据
1.查询
- 查询一条数据
    - 通过?id=的方式或/id/的方式
- 查询多条数据
- 分页功能
- 搜索功能
- 查找更名记录中出现重复的文件名

2.新增
- 增加一条更名记录

3.修改
- 修改一条更名记录

4.文件上传功能
- 支持上传csv,excel格式的文件

### 朱博士诊断记录数据
1.查询
- 查询一条数据
    - 通过?id=的方式或/id/的方式
- 查询多条数据
- 分页功能
- 搜索功能
- 查找朱博士诊断记录中出现重复的病理号

2.新增
- 增加一条朱博士诊断记录

3.修改
- 修改一条朱博士诊断记录

4.文件上传功能
- 支持上传csv,excel格式的文件
