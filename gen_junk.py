# gen_junk.py (เวอร์ชันอัปเกรดความโหด)
import os
import random
import string

def random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

os.makedirs("JunkFiles", exist_ok=True)

# 1. ปรับจำนวนไฟล์ตรงนี้ (เช่น 300 ไฟล์)
for i in range(300):
    class_name = f"_gen_{random_string(8)}"
    
    # สร้างไฟล์ .h
    with open(f"JunkFiles/{class_name}.h", "w") as h_file:
        h_file.write("#import <Foundation/Foundation.h>\n")
        h_file.write("#import <UIKit/UIKit.h>\n\n")
        h_file.write(f"@interface {class_name} : NSObject\n")
        
        # 2. ปรับจำนวนฟังก์ชันต่อไฟล์ตรงนี้ (เช่น 50 ฟังก์ชัน)
        for _ in range(50): 
            func_name = random_string(12)
            h_file.write(f"- (void){func_name} __attribute__((used));\n")
        h_file.write("@end\n")
        
    # สร้างไฟล์ .m
    with open(f"JunkFiles/{class_name}.m", "w") as m_file:
        m_file.write(f'#import "{class_name}.h"\n\n')
        m_file.write(f"@implementation {class_name}\n")
        
        # ปรับให้ตรงกับไฟล์ .h ข้างบน
        for _ in range(50):
            func_name = random_string(12)
            m_file.write(f"- (void){func_name} __attribute__((used)) {{\n")
            m_file.write(f"    int x = arc4random() % 100;\n")
            m_file.write(f"    for(int i=0; i<5; i++) {{ x += i; }}\n")
            m_file.write(f"}}\n")
        m_file.write("@end\n")

print("Junk code injection completed successfully!")
