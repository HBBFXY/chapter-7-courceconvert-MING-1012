import tokenize
import keyword
from io import StringIO

# 定义输入和输出文件名
INPUT_FILE = 'random_int.py'
OUTPUT_FILE = 'RANDOM_INT.PY'

def process_code(code):
    """
    处理代码字符串，将非关键字的标识符转换为大写。
    """
    # 使用StringIO将字符串包装成类文件对象，以便tokenize处理
    code_io = StringIO(code)
    
    # 生成令牌流
    tokens = tokenize.generate_tokens(code_io.readline)
    
    # 处理每个令牌
    processed_tokens = []
    for token_type, token_string, start, end, line in tokens:
        # 检查令牌是否为标识符 (NAME)
        if token_type == tokenize.NAME:
            # 检查标识符是否不是Python关键字
            if not keyword.iskeyword(token_string):
                # 将非关键字的标识符转换为大写
                processed_token = token_string.upper()
                processed_tokens.append((token_type, processed_token, start, end, line))
            else:
                # 如果是关键字，则保持原样
                processed_tokens.append((token_type, token_string, start, end, line))
        else:
            # 对于其他类型的令牌（如字符串、数字、运算符、括号等），直接添加
            processed_tokens.append((token_type, token_string, start, end, line))
    
    # 将处理后的令牌流转换回代码字符串
    # untokenize返回的是字节串，需要解码为字符串
    processed_code = tokenize.untokenize(processed_tokens).decode('utf-8')
    
    return processed_code

def main():
    try:
        # 读取原始文件内容
        with open(INPUT_FILE, 'r', encoding='utf-8') as f_in:
            original_code = f_in.read()
        
        # 处理代码
        converted_code = process_code(original_code)
        
        # 将处理后的代码写入新文件
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f_out:
            f_out.write(converted_code)
        
        print(f"文件转换成功！\n原始文件: {INPUT_FILE}\n转换后文件: {OUTPUT_FILE}")
    
    except FileNotFoundError:
        print(f"错误：找不到输入文件 '{INPUT_FILE}'。请确保该文件与脚本在同一目录下。")
    except Exception as e:
        print(f"处理过程中发生错误: {e}")

if __name__ == "__main__":
    main()
