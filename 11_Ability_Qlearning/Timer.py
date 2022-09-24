import time  #
start1 = time.time()  #タイムスタンプの時刻の表示形式 1970年1月1日0時0分0秒から何秒立っているか
start2 = time.perf_counter()  #time.time()より高精度 time.sleep()の時間を取得 sleep間も処理時間をカウント
start3 = time.process_time()  #time.time()より高精度 現在のプロセスシステムおよびユーザーCPU時間の合計値 sleep間をカウントしない
i = 0
while i < 10000000:
    txt = "HELOO" + str(i)
    i+=1
end1 = time.time()
end2 = time.perf_counter()
end3 = time.process_time()
print(txt)

print(end1 - start1)
print(end2 - start2)
print(end3 - start3)