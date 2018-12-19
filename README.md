# Data Analysis Project
## Thailand Education Statistics (PISA score performance)
This Project is a part of course 06016314 Problem Solving in Information Technology (2018)
  * Website: https://dwakez.github.io/web
  * Youtube: https://youtu.be/3mlXXMSt8lg
# Details
## Description
__PISA__ หรือ __Programme for International Student Assessment__ คือ โครงการประเมินผลนักเรียนร่วมกับนานาชาติ ริเริ่มโดยองค์การเพื่อความร่วมมือทางเศรษฐกิจและการพัฒนา
หรือ OCED (Organisation for Economic Co-operation and Development)
#### PISA ต่างจากการวัดผลแบบอื่นอย่างไร?
PISA ถูกออกแบบมาเพื่อทดสอบว่า นักเรียนสามารถจะนำสิ่งที่ได้เรียนในห้องเรียน ไปประยุกต์ใช้เพื่อแก้ปัญหาในชีวิต หรือสถานการณ์จริงได้หรือไม่
PISA ไม่สนใจว่านักเรียนจดจำเนื้อหาที่เรียนไปได้มากแค่ไหน แต่ PISA เป็นการทดสอบเพื่อที่จะรู้ว่านักเรียนมีทักษะการอ่านดีพอที่จะอ่านหนังสือ หนังสือพิมพ์ เอกสารราชการ หรือคู่มือสักเล่มหนึ่งเข้าใจหรือไม่
นอกจากนั้น PISA ไม่ได้มีจุดประสงค์ที่จะวัดผลนักเรียนเป็นรายบุคคล แต่ PISA ถูกออกแบบมาเพื่อวัดผลสัมฤทธิ์ในระดับชาติ โดยการวิเคราะห์และขยาย (extrapolate) คะแนนจากกลุ่มตัวอย่าง คะแนนสอบ PISA จะแสดงให้เห็นว่า แต่ละประเทศจัดการศึกษาแก่เด็กนักเรียนของตนเองได้ดีแค่ไหน และเมื่อเทียบกับประเทศอื่น ๆ แล้ว ผลสัมฤทธิ์เป็นอย่างไร
#### เป้าหมายของ PISA
มีจุดประสงค์เพื่อให้สาระข้อมูลและความจริงที่เป็นอยู่ของระบบโรงเรียนในประเทศหรือเขตเศรษฐกิจที่ร่วมดำเนินการในโครงการ เพื่อเป็นกระจกสะท้อนว่าระบบการศึกษาได้เตรียมเยาวชนของชาติให้มีความพร้อมเพียงพอสำหรับการใช้ชีวิตและการทำงานในอนาคตอย่างไร เมื่อเปรียบเทียบกับประเทศอื่นๆ ในโครงการ PISA
#### PISA จะเลือกประเมินกับเด็กที่อายุ 15 ปี
PISA เลือกประเมินนักเรียนอายุ 15 ปี ซึ่งเป็นวัยที่จบการศึกษาภาคบังคับ การสุ่มตัวอย่างนักเรียนทำตามระบบอย่างเคร่งครัด เพื่อประกันว่านักเรียนเป็นตัวแทนของนักเรียนทั้งระบบ อีกทั้งการวิจัยในทุกขั้นตอนต้องอยู่ภายใต้การควบคุมดูแลของ OECD ทุกประเทศต้องทำตามกฎเกณฑ์และวิธีการที่กำหนดอย่างเคร่งครัด เพื่อให้การวิจัยมีคุณภาพอยู่ในระดับเดียวกัน และข้อมูลของทุกประเทศมีมาตรฐานเดียวกัน เพื่อให้สามารถนำมาวิเคราะห์ร่วมกันได้ และตามข้อตกลงในการดำเนินโครงการ PISA ของ OECD ไม่อนุญาตให้เปิดเผยรายชื่อของโรงเรียนกลุ่มตัวอย่าง
#### เหตุที่ PISA เลือกเด็กอายุ 15 ปี แทนที่จะเป็นเด็กอายุ 12 หรือ 17 
เพราะเป็นอายุที่เด็กกำลังจะจบการศึกษาภาคบังคับ ผู้เชี่ยวชาญด้านการศึกษาทั่วโลก ช่วยกันสร้างวิธีทดสอบที่ใช้เวลา 2 ชั่วโมง ซึ่งมุ่งเน้นการวัดผลใน 3 วิชาหลัก ได้แก่ ภาษา คณิตศาสตร์ และวิทยาศาสตร์ ประเทศสมาชิกตัดสินใจที่จะจัดการทดสอบนี้ ทุก 3 ปี และมีการสับเปลี่ยนจุดมุ่งเน้นในการทดสอบใน 3 วิชาหลัก
***
#### จุดประสงค์
นำข้อมูลจาก Dataset มาวิเคราะห์เกี่ยวกับปัจจัยต่างๆ ที่ทำให้คะแนนเพิ่มหรือลด เหตุผลที่เพศชายได้คะแนนมากกว่าเพศหญิงหรือเพศหญิงได้คะแนนมากกว่าเพศชาย เป็นต้น
***
#### ผลลัพธ์
<img src="SVG graph from Pygal/[Mean Score] - Mathematics.svg"><img src="SVG graph from Pygal/[Mean Score] - Reading.svg"><img src="SVG graph from Pygal/[Mean Score] - Science.svg"><img src="SVG graph from Pygal/[Score Distribution] - Mathematics.svg"><img src="SVG graph from Pygal/[Score Distribution] - Reading.svg"><img src="SVG graph from Pygal/[Score Distribution] - Science.svg">
***
#### เครื่องมือที่ใช้ในการวิเคราะห์ข้อมูล
* Python 3
* Pandas
* Pygal
---
# Group Member
|<img src="Profile/sowja.jpg" width="150px" height="150px">|<img src="Profile/nipnew.jpg" width="150px" height="150px">|<img src="Profile/dorn.jpg" width="150px" height="150px">|<img src="Profile/pang.jpg" width="150px" height="150px">|
|:-----:|:-----:|:-----:|:-----:|
|[Dwakez](https://github.com/Dwakez)|[Chattida](https://github.com/Chattida)|[dorn123](https://github.com/dorn123)|[Khunpanggg](https://github.com/Khunpanggg)|
### รายชื่อสมาชิก
61070097  นายนรรณจา โสวรรณ<br/>
61070029  นางสาวฉัตรธิดา แจ้งใจ<br/>
60070026  นายดรณ์ นุตเวช<br/>
61070059  นางสาวณิชาภัทร คชาชีวะ<br/>
# References
[Education Statistics](https://www.kaggle.com/theworldbank/education-statistics?fbclid=IwAR2iMpmOxm0cWc4lpBPuKFkLdDKnKs9jvsSfT9RQ9drKAxRDOrcE32yGbPE)
