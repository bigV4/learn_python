import tkinter as tk
root = tk.Tk()

mr, mc = 7, 7

tk.Label(root, text="Find:").grid(row=mr+0, column=mc+0, sticky='e')
tk.Entry(root, width=60).grid(row=mr+0, column=mc+1,
                              padx=2, pady=2, sticky='we', columnspan=9)

tk.Label(root, text="Replace:").grid(row=mr+1, column=mc+0, sticky='e')
tk.Entry(root).grid(row=mr+1, column=mc+1, padx=2,
                    pady=2, sticky='we', columnspan=9)

tk.Button(root, text="Find").grid(
    row=mr+0, column=mc+10, sticky='e' + 'w', padx=2, pady=2)
tk.Button(root, text="Find All").grid(
    row=mr+1, column=mc+10, sticky='e' + 'w', padx=2)
tk.Button(root, text="Replace").grid(
    row=mr+2, column=mc+10, sticky='e' + 'w', padx=2)
tk.Button(root, text="Replace All").grid(
    row=mr+3, column=mc+10, sticky='e' + 'w', padx=2)

tk.Checkbutton(root, text='Match whole word only ').grid(
    row=mr+2, column=mc+1, columnspan=4, sticky='w')
tk.Checkbutton(root, text='Match Case').grid(
    row=mr+3, column=mc+1, columnspan=4, sticky='w')
tk.Checkbutton(root, text='Wrap around').grid(
    row=mr+4, column=mc+1, columnspan=4, sticky='w')

tk.Label(root, text="Direction:").grid(row=mr+2, column=mc+6, sticky='w')
tk.Radiobutton(root, text='Up', value=1).grid(
    row=mr+3, column=mc+6, columnspan=6, sticky='w')
tk.Radiobutton(root, text='Down', value=2).grid(
    row=mr+3, column=mc+7, columnspan=2, sticky='e')


def rgb_to_hex(rgb):
    # RGB格式颜色转换为16进制颜色格式
    if type(rgb) == str:
        RGB = rgb.split(',')            # 将RGB格式划分开来
    else:
        RGB = rgb
    color = '#'
    for i in RGB:
        num = int(i)
        # 将R、G、B分别转化为16进制拼接转换并大写  hex() 函数用于将10进制整数转换成16进制，以字符串形式表示
        color += str(hex(num))[-2:].replace('x', '0').upper()
    print(color)
    return color


def hex_to_rgb(hex):
    # 16进制颜色格式颜色转换为RGB格式
    r = int(hex[1:3], 16)
    g = int(hex[3:5], 16)
    b = int(hex[5:7], 16)
    rgb = str(r)+','+str(g)+','+str(b)
    print(rgb)
    return rgb


# 「零，零」
for r in range(0, mr):
    for c in range(0, mc):
        color1 = (255, c*(256//mc) % 256, r*255//mr % 256)
        color1 = rgb_to_hex(color1)
        print(color1)
        tk.Label(root, text="(%r,%r)" %
                 (r, c), width=4, height=1, bg=color1).grid(row=r, column=c)
# 「零，一」
for r in range(0, mr):
    for c in range(0, mc):
        color1 = (128, c*(256//mc) % 256, r*255//mr % 256)
        color1 = rgb_to_hex(color1)
        print(color1)
        tk.Label(root, text="(%r,%r)" %
                 (r, c+mc), width=4, height=1, bg=color1).grid(row=r, column=c+mc)
# 「零，二」
for r in range(0, mr):
    for c in range(0, mc):
        color1 = (0, c*(256//mc) % 256, r*255//mr % 256)
        color1 = rgb_to_hex(color1)
        print(color1)
        tk.Label(root, text="(%r,%r)" %
                 (r, c+mc*2), width=4, height=1, bg=color1).grid(row=r, column=c+mc*2)
# 「一，零」
for r in range(0, mr):
    for c in range(0, mc):
        color1 = (c*(256//mc) % 256, 255, r*255//mr % 256)
        color1 = rgb_to_hex(color1)
        print(color1)
        tk.Label(root, text="(%r,%r)" %
                 (r+mr, c), width=4, height=1, bg=color1).grid(row=r+mr, column=c)
# 「二，零」
for r in range(0, mr):
    for c in range(0, mc):
        color1 = (c*(256//mc) % 256, r*255//mr % 256, 255)
        color1 = rgb_to_hex(color1)
        print(color1)
        tk.Label(root, text="(%r,%r)" %
                 (r+mr*2, c), width=4, height=1, bg=color1).grid(row=r+mr*2, column=c)

root.mainloop()
