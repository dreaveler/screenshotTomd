from openai import OpenAI
 
client = OpenAI(
    api_key="sk-XXXXXXXXX",
    base_url="https://api.moonshot.cn/v1",
)
def ask_moonshot(base64_image):
    completion = client.chat.completions.create(
        model = "moonshot-v1-8k-vision-preview",
        messages = [
            {"role": "system", "content": "你是一个精通markdown语言的专家，你擅长将图片中的数学公式转出为obsidian中的markdown格式，且你的输出是绝对正确的，且只会输出图片中的文字，对于图片中国的土星不做出任何响应，且不会增加、删改图片中的内容，且会自动进行换行。"},
            {"role": "user", "content": [
                {"type":"text" , "text":"你好，请将图片中的文字转成为markdow格式"},
                {"type":"image_url","image_url":{"url": f"data:image/png;base64,{base64_image}"}}
            ]}
        ],
        temperature = 0.3,
    )
    return completion.choices[0].message.content
