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
<img src="https://cdn.discordapp.com/attachments/888819175513010256/1223895803857207326/image.png?ex=662df9ca&is=662ca84a&hm=2ba2955e0c46538251831fa3c8f3a89bfb7c27d6178dbd9cd5776efcb99eb2c6&"/>

## หน้าการตั้งค่า
<img src="https://cdn.discordapp.com/attachments/888819175513010256/1223895980403851314/image.png?ex=662df9f4&is=662ca874&hm=d234475f145c9d69fff52ff314ee6d59fe8789b3ee2964c22afd1f716332de4e&"/>
