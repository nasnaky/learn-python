#종류
"hello world"
'hello world'
''''hello world'''
"""hello world"""

#문자열 내 작은 따음표 포함("")안에 (')넣기
"나스나키'잘생김"

#문자열 내 큰 따음표 포함('')안에 ("")넣기
'"나스나키" 잘생김 '

#두개를 제외하고 쓸수 있는 방법(\)넣기
"\"나스나키\""
'\'나스나키\''

#줄 바꾸기
"\n"

#윌르 제와하고 바꾸는 방법 
"""
나스나키
잘생김
"""

'''
나스나키
잘생김
'''

#문자열 기본 
a="나스나키"
b="잘생김"

#문자열 더하기
a+b#나스나키잘생김

#문자열 곱하기
a*2#나스나키나스나키



#문자열 길이 구하기
a="fun nasnaky"
len(a)#11

#인댁싱(수정가능)
a="fun nasnaky"
#  01234567890
a[1]#u
a[0]#f
a[11]#y
a[-1]#y(-가 붙으면 뒤에서 부터 센다)

#슬라이싱
a="fun nasnaky"
#  01234567890
a[0:3]#fun  ***(a[0<=a<3])***
a[0:]#fun nasnaky
a[:5]#fun n
a[:]#fun nasnaky

#값 넣기
"fun smart nasnaky %d" % 5
"fun %s nasnaky" % "smart"
a= "smart"
"fun %s nasnaky" % a
a=5
"fun %s nasnaky %d" % ("smart",a)
#%s는 포멧 코드로 아무거나 넣어도 된다.

#포맷 코드와 숫자 사용
"%10s" % 12#          12=공백 10개 후 12
"%0.4f" % 1.123456789 #1.1234


#format 함수 사용
"nasnaky{0}" .format(5)#nasnaky5
"{0}nasnaky".format("smart")#smart nasnaky


#정열
#왼(빈칸 10)
"{0:<10}".format(1)#1          
#오
"{0:>10}".format('A')#          A
#가운데
"{0:^10}".format("A")#     A     

#개수와 찾기
a="fun smart nasnaky"

a.count("n")#3
a.find("f")#0
a.find("o")#-1(없을 시 -1은 반환한다.)

#문자열 삽입
",".join("asdf")#a,s,d,f

#대문자를 소문자로
a="smart"
a.upper()#SMART
#소문자를 대문자로
a="SMART"
a.lower()#smart

#공백 지우기 기본
a=" smart "
#왼 공백지우기
a.lstrip()#smart 
#오 공백지우기
a.rstrip()# smart
#가운데 공백지우기
a.strip()#smart