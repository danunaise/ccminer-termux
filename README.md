# ccminer verus autostart termux linux(ubuntu)

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
