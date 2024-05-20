basket = 20
price = 200
tax = 1.1
erning = 0

while basket > 0:
    count = int(input("몇개를 사시겠어요? "))
    if count > basket:
        print("현재 재고: %d" %basket)
        continue

    pay = str(input("결제 방법을 선택해 주세요. '카드' 혹은 '현금' ")).strip()

    if pay == "카드":
        erning += count * price * tax
    else:
        erning += count * price
    basket -= count

print("총 판매 금액 : %d" %erning)






