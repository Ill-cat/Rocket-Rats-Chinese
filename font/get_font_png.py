import os
import json5
import shutil
from PIL import Image

def clear_directory(dir_path):
    """清空目标目录"""
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)
    os.makedirs(dir_path, exist_ok=True)

def process_font(font_name, needs_padding=False):
    """处理单个字体文件"""
    try:
        # 1. 读取 .yy 文件中的 glyphs 数据
        yy_file = os.path.join("字体文件", f"{font_name}.yy")
        with open(yy_file, "r", encoding="utf-8") as f:
            data = json5.load(f)
            glyphs = data["glyphs"]

        # 2. 打开原字体 PNG (确保是RGBA模式以支持透明)
        png_file = os.path.join("字体文件", f"{font_name}.png")
        img = Image.open(png_file).convert("RGBA")

        # 3. 创建输出目录
        output_dir = os.path.join("切片文件", font_name)
        clear_directory(output_dir)

        exported_count = 0
        padding = 4 if needs_padding else 0  # 只有font_stats需要上下各加4px
        
        # 4. 遍历 glyphs，切割并添加留白（如果需要）
        for char_code, glyph in glyphs.items():
            try:
                # 提取元数据
                x, y = glyph["x"], glyph["y"]
                w, h = glyph["w"], glyph["h"]
                shift = glyph.get("shift", 0)
                offset = glyph.get("offset", 0)
                
                # 不再跳过小像素字符
                if needs_padding:
                    # 对于font_stats，创建带留白的新画布
                    new_h = h + 2 * padding
                    new_img = Image.new("RGBA", (w, new_h), (0, 0, 0, 0))
                    char_img = img.crop((x, y, x + w, y + h))
                    new_img.paste(char_img, (0, padding))
                    final_img = new_img
                    # 调整shift值以保持垂直居中
                    shift += padding
                else:
                    # 其他字体直接裁剪
                    final_img = img.crop((x, y, x + w, y + h))
                
                # 生成文件名
                filename = f"char={char_code};shift={shift};offset={offset}.png"
                output_path = os.path.join(output_dir, filename)
                
                # 保存图像
                final_img.save(output_path)
                exported_count += 1
                
                # 调试信息：显示小尺寸字符
                if w <= 3 or h <= 3:  # 只是显示，不跳过
                    char_str = chr(int(char_code)) if char_code.isdigit() else f"编码{char_code}"
                    print(f"小尺寸字符处理: 字体={font_name}, 字符='{char_str}', 尺寸={w}x{h}")
                
            except Exception as char_error:
                char_str = chr(int(char_code)) if char_code.isdigit() else f"编码{char_code}"
                print(f"处理字体 {font_name} 的字符失败: 编码={char_code}, 字符='{char_str}', 错误: {str(char_error)}")
                continue

        print(f"字体 {font_name} 处理完成: 成功导出 {exported_count}/{len(glyphs)} 个字符")
        return True
        
    except Exception as e:
        print(f"处理字体 {font_name} 时出错: {str(e)}")
        return False

def export_all_fonts():
    """处理所有字体文件"""
    # 确保字体文件目录存在
    if not os.path.exists("字体文件"):
        print("错误: '字体文件' 目录不存在")
        return False
    
    # 确保切片文件目录存在
    os.makedirs("切片文件", exist_ok=True)
    
    # 定义要处理的字体列表及其是否需要padding
    fonts_to_process = [
        ("font_stats", True),    # 需要上下4px空隙
        ("fnt_end_result", False),
        ("fnt_standard", False),
        ("fnt_title", False)
    ]
    
    all_success = True
    for font_name, needs_padding in fonts_to_process:
        if not process_font(font_name, needs_padding):
            all_success = False
    
    return all_success

if __name__ == "__main__":
    export_all_fonts()