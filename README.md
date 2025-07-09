# Rocket-Rats-Chinese
一个简单的汉化补丁  
汉化效果详情见示例截图  

## 使用方法
0. **不知道插哪了插在这**  
   - 如果先前**使用过其他版本的补丁文件**  
请将`data.win.bak`复原为`data.win`再使用  
1. **下载汉化文件**  
   - 下载`Rocket Rats.[版本号].zip`和`中文配置文件`  
     - 如补丁文件 `Rocket Rats.V1.3.11.000.zip`  
     - 如中文配置文件 `chinese_zh_language_file.json`  
2. **进入游戏目录**  
   - *方法1（Steam）*:  
     右键游戏 → `管理` → `浏览本地文件`  
    - *方法2（手动）*:  
     直接访问：  
     `X:\steam\steamapps\common\Rocket Rats`  
3. **安装汉化**  
   - 安装字体:  
     -  解压`Rocket Rats.[版本号].zip`  
     - 将`解压内容`放入游戏目录，结构应为：  
        ```
        .
        ├── Install.bat
        ├── bspatch.exe
        ├── data.patch
        └── data.win
        ```
     - 运行`Install.bat`文件  
     - 提示完成即可  
4. **放入中文配置文件**  
   - 进入游戏目录`X:\steam\steamapps\common\Rocket Rats\localizations\`  
   - 把`chinese_zh_language_file.json`放进去
5. **游戏内切换语言**  
   - 如果字体改变了说明字体安装成功  
   - 点击`Options` → `Video` → `Language` → `<English>`  
   - 随便哪个方向转,出中文即可  
      - 如果没出中文,说明`中文配置文件`没放对位置  
   
## 注意事项
1. `补丁`运行后会生成`data.win.bak`备份文件,出现问题后把`data.win.bak`重命名为`data.win`即可
   - 如果运行了多次`补丁`,请在steam右键游戏:
   `属性` → `已安装文件` → `验证游戏文件的完整性`
2. 游戏**更新后**会变回英文  
3. 补丁**只对对应版本有效**,更新后请不要使用旧补丁  
4. 曾经在是否保留部分原游戏字体之间纠结,不过为了统一性所以没有全用  
5. 有更好的翻译可以创我  
6. 有bug也请创我   

## **自己汉化**
这部分的内容旨在如果哪天我似了还没有官方中文,你可以自学按以下步骤自己汉化  
(或者现在就想尝尝`银弹X`也行  
*如果要做记得先备份  

**需要工具**:  
- GameMaker(使用时的版本是v2024.8.1.171,下同)
- Python3(Python 3.10.7)
- UndertaleModTool(v0.8.1.1)
  [二次指路,非常好用](https://github.com/UnderminersTeam/UndertaleModTool)

### 创建中文汉化配置
1. 进入游戏目录`X:\steam\steamapps\common\Rocket Rats\localizations\`  
2. 复制`english_en_language_file.json`,找一个风水宝地放着  
3. 把复制的`english_en_language_file.json`文件重命名为`chinese_zh_language_file.json`  
4. 将文件里冒号后的内容汉化  
5. 把`chinese_zh_language_file.json`放入`X:\steam\steamapps\common\Rocket Rats\localizations\`  
6. 进入游戏按`Options` → `Video` → `Language` → `<English>`切换语言,如果切换到第三个文件全部变为"▯"即为成功  

### 先从游戏中获取原字体
1. 进入游戏目录`X:\steam\steamapps\common\Rocket Rats`  
2. 用`UndertaleModTool`打开`data.win`文件  
3. 上边工具栏[`Scripts` → `Community Scripts` → `FontEditor.csx`],选择`fnt_end_result`,点击`OK`  
4. 新窗口上边工具栏[`Edit` → `Export font to ZIP`],选择一个风水宝地保存导出的字体文件  
5. 循环步骤直到导出全部字体
    ```
    .
    ├── fnt_end_result.zip
    ├── fnt_standard.zip
    ├── fnt_title.zip
    └── font_stats.zip
    ```
    - 不想做这一步可以在仓库里的`原始文件`里找到这四个导出字体
6. 之后,在替换字体时,你可以决定保留其中的哪些字体  
   - `fnt_end_result`:游戏结束时"你赢了/游戏结束"字体
   - `fnt_standard`:游戏标准字体,包括菜单,卡片描述,技能树描述
   - `fnt_title`:大一号字体,主要显示于通用升级标题,已获取的升级标题
   - `font_stats`:数据字体,主要用于按下`Tap`键后右上角数据显示

### 创建替换用的字体
1. 打开`GameMaker`,新建一个项目,名称随意
2. 右边右键[`创建` → `字体`],名称和导出的字体一样,同样创建四个
3. 点击[`添加`],在右边把`chinese_zh_language_file.json`里的字全粘贴进去,点击[`增加范围`] (如有需要,可以把`portuguese_pt_language_file.json`的内容也贴进去)
   - 如果想要节省体积,不同的字体可以只粘贴使用到的部分  
   - `fnt_end_result`:只知道有`你赢了`和`游戏结束`  
   - `fnt_standard`:`chinese_zh_language_file.json`全部  
   - `fnt_title`:懒,自己找去  
   - `font_stats`:`chinese_zh_language_file.json`里的`Stats字段下内容`和`按下显示数据`  
   - 然后以上,推荐`字母`和`数字`和`:'"%+`全加上  
4. 然后选择字体,设置大小,以下是我使用的字体和设置,酌情更改  
   - `fnt_end_result`:**方正喵呜体**,字体大小24  
   - `fnt_standard`:**Unifont**,字体大小12  
   - `fnt_title`:**点阵粗宋**,字体大小12  
   - `font_stats`:**全小素**,字体大小6  
   - 其余设置:  
     - `Enable SDF`:`OFF`  
     - `选项`:  
       - `提示`:`单色`  
       - `字形选项`:`禁用自动微调`  
5. 点击[重新生成]依次生成四款字体,然后右键右边字体[在资源管理器中打开]
6. 至此,你就得到了字体纹理和字体位置关系的yy文件  
    - 不想做这一步可以拿仓库里`font`文件夹里的文件  
     `fnt_end_result.png`,`fnt_end_result.yy`  
     `fnt_standard.png`,`fnt_standard.yy`  
     `fnt_title.png`,`fnt_title.yy`  
     `font_stats.png`,`font_stats.yy`  

### 合成字体压缩包
1. 下载仓库里`font`文件夹里的`get_font_png.py`文件  
2. 创建一个`font`文件夹,把`get_font_png.py`放进去  
3. 在`font`文件夹下创建一个`字体文件`文件夹  
   把`创建替换用的字体`步骤取得的`.png`和`.yy`文件放进去  
4. 在`font`文件夹里`右键` → `在终端中打开`  
   运行以下命令:  
   ```
   python get_font_png.py
   ```
   - 这一步前大概还需要装一些`json5`之类的依赖,总之没运行成功就去**deepseek**
5. 这一步会生成一个`切片文件`文件夹,把`.png`文件中的字体切片放在里面 
   - 对于`font_stats`字体,会上下各加4px像素以保证对齐,如果你的字体足够高可以去掉 
6. 打开`切片文件`文件夹,把生成的四个`字体文件夹`找个风水宝地放置
7. 如无特殊需求,可以分别压缩成ZIP了  
   - 如果不幸你有的话,比如我只需要往字体里添加中文部分,那你就把`char=9647`之前的字形文件全删了,然后把对应字体的原字形文件拖进去再压缩
8. 至此,你就得到了用于导入游戏的`字体文件压缩包`  

### 使游戏支持显示中文字体
1. 进入游戏目录`X:\steam\steamapps\common\Rocket Rats`  
2. 用`UndertaleModTool`打开`data.win`文件  
3. 下载仓库内`font`文件夹里的`768x768透明底.png`  
4. 侧边栏找到`Embedded textures`,双击`Texture 6(...)`  
5. 下拉找到`Import`按钮,选择下载的`768x768透明底.png`,点击`打开` 
6. 点击[`Fonts` → `fnt_end_result`],点击右侧`Texture`一栏中的`...`进入`PageItem`  
7. 修改以下各值:
    - `Source position/size`:0,0,768,768
    - `Target position/size`:0,0,768,768
    - `Bounding size`:768,768
8. 如果替换的`fnt_end_result`字形不多可以跳过步骤3,4,5,6,7  
   - 如果后续步骤遇到问题
      `Too many characters`  
      `All characters do not fit in the texture`  
      则需要做  
9. 点击[`Fonts` → `fnt_standard`/`fnt_title`/`font_stats`]点击右侧`Texture`一栏中的`...`进入`PageItem`
10. 依次修改各值:
    - `fnt_standard`
      - `Source position/size`:648,0,376,512  
      - `Target position/size`:0,0,376,512  
      - `Bounding size`:376,512  
    - `fnt_title`  
      - `Source position/size`:648,512,376,512  
      - `Target position/size`:0,0,376,512  
      - `Bounding size`:376,512  
    - `font_stats`  
      - `Source position/size`:0,0,256,256  
      - `Target position/size`:0,0,256,256  
      - `Bounding size`:256,256  
    - 这一步是改字体贴图大小和位置  
11. 上边工具栏[`Scripts` → `Community Scripts` → `FontEditor.csx`],依次选择`fnt_end_result`/`fnt_standard`/`fnt_title`/`font_stats`,点击`OK`   
12. 新窗口上边工具栏[`Edit` → `Import font to ZIP`]导入对应的字体,显示`Successfully   imported`后点击`确定`  
13. 工具栏[`File` → `Save`],显示`Saved`后点击`确定`  
14. 重复步骤直到字体全部替换,`Ctrl+S`操作保存,到这一步就算汉化完成了  

### 生成汉化补丁
1. 如果你要创建汉化补丁,需要下载`bsdiff`文件夹里的`bsdiff.exe`,`bspatch.exe`和`install.bat`文件  
   - 感谢[bsdiff-win](https://github.com/reitowo/bsdiff-win)
2. 终端运行 bsdiff/bsdiff.exe 原data.win 导入字体后data.win data.patch  
   ```
   bsdiff/bsdiff.exe 原始文件/V1.3.11.000.win V1.3.11.000/data.win data.patch
   ```  
3. 生成完毕后`bspatch.exe`,`install.bat`,`data.patch`即为一个汉化补丁
