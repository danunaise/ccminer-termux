# ccminer verus autostart termux linux(ubuntu)

#### *Command คำสั่งภายใน*<br>
startminer : เริ่มการขุด <br>
editminer  : แก้ไขข้อมูล<br>
update : อัปเดตโปรแกรมขุด<br>

```
termux-setup-storage
```
```
pkg update -y
```
ต่อจากนี้ให้ตอบ N ทั้งหมด

```
pkg install proot-distro -y && proot-distro install ubuntu && pkg install nano && pkg install wget -y && pkg install python3 && cd /data/data/com.termux/files/usr/etc && nano profile
```

เลื่อนลงไปล่างสุด ใส่คำสั่ง
```
proot-distro login ubuntu
```

```
apt-get update -y && apt-get install git -y && git clone https://github.com/danunaise/ccminer-termux.git && cd ccminer-termux && chmod +x setup.sh && sh setup.sh
```

หลังเปิด bash.bashrc
เพิ่มคำสั่ง startminer
ctrl+x ตอบ yes เพื่อ save และ กด enter เพื่อออก

หลังทำเสร็จให้ กดค้างที่หน้าจอ เลือกที่ more... และ kill process
ที่สำคัญอย่าลืม กดเปิด Keep screen on ไว้เพื่อให้โปรแกรมขุดทำงานตลอดโดยที่ไม่พักหน้าจอ

## หน้าจอการทำงาน
<img src="https://media.discordapp.net/attachments/888819175513010256/1223895803857207326/image.png?ex=661b84ca&is=66090fca&hm=fe7f2ecd5911f8620c1bee34b1a5f247f1a6286dbb49ca57a8c57c59cc4530f1&=&format=webp&quality=lossless&width=360&height=662"/>

## หน้าการตั้งค่า
<img src="https://media.discordapp.net/attachments/888819175513010256/1223895980403851314/image.png?ex=661b84f4&is=66090ff4&hm=9c15fc7b9d17b3726e8e7fda2f116d01caacf070e91ac6f724888bd0c6d3c06e&=&format=webp&quality=lossless&width=356&height=661"/>
