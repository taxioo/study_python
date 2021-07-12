file_path = '\\temp\\test_a\\live.txt'


f = open(file_path,"wt", encoding = 'utf-8')
f.write("""삶이 그대를 속일지라도 슬퍼하거나 노하지 말라!
 우울한 날들을 견디면 믿으라, 
 기쁨의 날이 오리니
 
 끝\n""")
f.write("더 추가가능함...\n")
f.write("더 추가가능함...")

f.close()

