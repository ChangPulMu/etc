print("대숭실 은행에 오신걸 환영합니다!\n")

seq = 1                                             #seq가 0이면 while문조차 안들어감으로 임시적으로 1로 초기화

while(seq!=0) :                                 #seq가 종료를 의미하는 0이면 while문내의 문장 종료

    print("\n[ 환전 업무 ] : 1")
    print("[ 적금 업무 ] : 2")
    print("[ 종료 ] : 0\n")

    seq = int(input("원하시는 업무에 따른 번호를 입력해주세요 : "))
    
    if seq==1 :                             #환전 업무일 때

        nation = input("어느 나라 돈[달러, 유로, 엔화]으로 환전하시겠습니까? : ")
        money = int(input("얼마[원화 기준]를 환전하시겠습니까? : "))
        
        if nation=="달러" :               #달러로 환전할 때

            change_money = money*0.00089
            change_nation = "미국 달러"

        elif nation=="유로" :               #유로로 환전할 때

            change_money = money*0.00078
            change_nation = "유럽 유로"

        elif nation=="엔화" :               #엔화로 환전할 때

            change_money = money*0.0968
            change_nation = "일본 엔화"

        print(change_nation, "로 %2f만큼 환전되셨습니다. ^^" %change_money)           #어떤 통화로 얼만큼 환전되었는지 출력

    elif seq==2 :                           #적금 업무일 때

        print("\n단리는 30만원까지, 복리는 10만원까지 각각 5.0%의 이율로 모시겠습니다[24개월 기준] ^^")
        print("숭실대생이시라면 추가 이율 0.25%에 컴퓨팅적 사고 수업 수강중이시라면 복리 20만원까지 적금 가능하십니다 ^^\n")

        category = input("단리, 복리 중 어떤 것을 선택하시겠습니까[단리/복리]? : ")
        songsil = input("숭실대 생이십니까[Y/N]? : ")

        if songsil=="Y" :                   #숭실대생인지 검사
            ans = input("숭실대를 대표할 수 있는 수업은[컴사/숭역진]? : ")
            if ans=="숭역진" :
                print("당신은 참 숭실인이 되기에는 멀었습니다..")
                songsil="N"
            elif ans=="컴사" :
                print("참 숭실인이군요! 환영합니다 ^^")

        comthink = input("컴퓨팅적 사고 수업을 수강중이십니까[Y/N]? : ")

        if comthink=="Y" :                  #컴퓨팅적 사고를 듣는 학생인지 검사
            ans = input("최초의 기계식 컴퓨터를 만든 사람은[파스칼/칸트]? : ")
            if ans=="칸트" :
                print("철학 수업과 착각하셨나봅니다")
                comthink="N"
            elif ans=="파스칼" :
                print("훌륭하군요! 커피를 사드리겠습니다 ^^")

        money = int(input("얼마를 적금드시겠습니까[만 원 단위 숫자만 입력]? : "))

        if category=="단리" :                 #단리의 경우
            
            if money>30 :                   #30만원 초과하면 적금 불가
                print("단리로는 30만원을 초과해서 적금하실 수 없습니다.")
                
            else :
                
                if songsil=="Y" :           #숭실대생이라면 우대 금리 적용
                    final_money = money*0.0525*25 + money*24
                    
                elif songsil=="N" :         #아닌 경우 우대 금리 적용 X
                    final_money = money*0.05*25 + money*24

                print("총 ", final_money, "만큼 만기 때 수령가능하십니다!")                   #적금 만기 때 수령할 수 있는 금액을 출력
                print("감사합니다 ^^")
                    
        elif category=="복리" :               #복리의 경우
            
            if comthink=="Y" :              #컴퓨팅적 사고를 듣는 학생일 때
                
                if money>20 :               #20만원 초과하면 적금 불가
                    print("복리로는 20만원을 초과해서 적금하실 수 없습니다.")

                else :

                    if songsil=="Y" :       #숭실대생이라면 우대 금리 적용
                        final_money = money*24*(1.0525)**2

                    elif songsil=="N" :     #아닌 경우 우대 금리 적용 X
                        final_money = money*24*(1.05)**2

                    print("\n총 ", final_money, "만큼 만기 때 수령가능하십니다!")                   #적금 만기 때 수령할 수 있는 금액을 출력
                    print("감사합니다 ^^")

            elif comthink=="N" :         #컴퓨팅적 사고를 듣지않는 학생일 때
                
                if money>10 :               #10만원 초과하면 적금 불가
                    print("복리로는 10만원을 초과해서 적금하실 수 없습니다.")

                else :
                    
                    if songsil=="Y" :       #숭실대생이라면 우대 금리 적용
                        final_money = money*24*(1.0525)**2

                    elif songsil=="N" :     #아닌 경우 우대 금리 적용 X
                        final_money = money*24*(1.05)**2

                    print("\n총 ", final_money, "만큼 만기 때 수령가능하십니다!")                   #적금 만기 때 수령할 수 있는 금액을 출력
                    print("감사합니다 ^^")
