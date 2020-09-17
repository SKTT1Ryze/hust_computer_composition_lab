# python script for generate gb2312 code
if __name__ == '__main__':
    # ０１２３４５６７８９ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ
    s="计科校交１８０１车春池Ｒｕｓｔ大法好"
    code=s.encode("gb2312")
    print(code)