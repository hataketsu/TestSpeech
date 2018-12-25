ls = '''Hổ phách	#FFBF00
Xanh berin	#7FFFD4
Xanh da trời	#007FFF
Be	#F5F5DC
Nâu sẫm	#3D2B1F
Đen	#000000
Xanh lam	#0000FF
Nâu	#964B00
Da bò	#F0DC82
Cam cháy	#CC5500
Hồng y	#C41E3A
Đỏ yên chi	#960018
Men ngọc	#ACE1AF
Anh đào	#DE3163
chàm	#007BA7
Xanh nõn chuối	#7FFF00
Xanh cô ban	#0047AB
Đồng	#B87333
San hô	#FF7F50
Kem	#FFFDD0
Đỏ thắm	#DC143C
Xanh lơ (cánh chả)	#00FFFF
Lục bảo	#50C878
Vàng kim loại	#FFD700
Xám	#808080
Xanh lá cây	#00FF00
Vòi voi	#DF73FF
Chàm	#4B0082
Ngọc thạch	#00A86B
Oải hương	#E6E6FA
Vàng chanh	#CCFF00
Hồng sẫm	#FF00FF
Hạt dẻ	#800000
Cẩm quỳ	#993366
Hoa cà	#c8a2c8
Lam sẫm	#000080
Thổ hoàng	#CC7722
Ô liu	#808000
Da cam	#FF7F00
Lan tím	#DA70D6
Lòng đào	#FFE5B4
Dừa cạn	#CCCCFF
Hồng	#FFC0CB
Mận	#660066
Xanh thủy tinh	#003399
Hồng đất	#CC8899
Tía	#660099
Đỏ	#FF0000
Cá hồi	#FF8C69
Đỏ tươi	#FF2400
Nâu đen	#704214
Bạc	#C0C0C0
Nâu tanin	#D2B48C
Mòng két	#008080
Xanh Thổ	#30D5C8
Đỏ son	#FF4D00
Tím	#BF00BF
Trắng	#FFFFFF
Vàng	#FFFF00'''

for i in ls.split('\n'):
    name, color = i.strip().split('\t')
    print('"%s":"%s",' % (name.strip().lower(), color.strip())),
